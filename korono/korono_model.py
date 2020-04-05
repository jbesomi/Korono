"""
LIBRARIES
"""

import torch
import re

"""
SETTINGS
"""

NUM_CONTEXT_FOR_EACH_QUESTION = 10


"""
Transformers
"""


def answer_question(question, context, model, tokenizer, torch_device):
    """
    Answer questions
    """

    print("question: ", question)
    print("context: ", context)
    print("model: ", model)
    print("tokenizer: ", tokenizer)

    encoded_dict = tokenizer.encode_plus(
        question,
        context,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        return_token_type_ids=True,
        max_length=256,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=False,  # Construct attn. masks.
        return_tensors="pt",  # Return pytorch tensors.
    )

    print("encoded_dict:", encoded_dict)

    input_ids = encoded_dict["input_ids"].to(torch_device)

    start_scores, end_scores = model(input_ids)

    all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    answer = tokenizer.convert_tokens_to_string(
        all_tokens[torch.argmax(start_scores) : torch.argmax(end_scores) + 1]
    )

    answer = answer.replace("[CLS]", "")

    return answer


from transformers import BartTokenizer, BartForConditionalGeneration


def get_summary(text, model, tokenizer, torch_device):
    """
    Get summary
    """

    tokenizer_summarize = BartTokenizer.from_pretrained("bart-large-cnn")
    model_summarize = BartForConditionalGeneration.from_pretrained("bart-large-cnn").to(
        torch_device
    )

    model_summarize.to(torch_device)
    # Set the model in evaluation mode to deactivate the DropOut modules
    model_summarize.eval()

    answers_input_ids = tokenizer_summarize.batch_encode_plus(
        [text], return_tensors="pt", max_length=1024
    )["input_ids"]

    answers_input_ids = answers_input_ids.to(torch_device)

    summary_ids = model_summarize.generate(
        answers_input_ids, num_beams=4, max_length=5, early_stopping=True
    )

    return tokenizer_summarize.decode(
        summary_ids.squeeze(),
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )


"""
Main
"""


def create_output_results(
    question, all_contexts, all_answers, summary_answer=None, summary_context=None
):
    """
    Return a dictionary of the form

    {
        question: 'what is coronavirus',
        results: [
            {
                'context': 'coronavirus is an infectious disease caused by',
                'answer': 'infectious disease'
                'start_index': 18
                'end_index': 36
            },
            {
                ...
            }
        ]
    }

    Start and end index are useful to find the position of the answer in the context
    """

    def find_start_end_index_substring(context, answer):
        search_re = re.search(re.escape(answer.lower()), context.lower())
        if search_re:
            return search_re.start(), search_re.end()
        else:
            return 0, len(context)

    output = {}
    output["question"] = question
    output["summary_answer"] = summary_answer
    output["summary_context"] = summary_context
    results = []
    for c, a in zip(all_contexts, all_answers):

        span = {}
        span["context"] = c
        span["answer"] = a
        span["start_index"], span["end_index"] = find_start_end_index_substring(c, a)

        results.append(span)

    output["results"] = results

    return output


def get_all_context(query, cse, num_results):
    """
    Search in the metadata dataframe and return the first `num` results that better match the query
    """

    papers_df = cse.search(query, num_results)
    return papers_df["abstract"].str.replace("Abstract", "").tolist()


def get_all_answers(question, all_context, model, tokenizer, torch_device):
    """
    Return a list of all answers, given a question and a list of context
    """

    all_answers = []

    for context in all_context:
        all_answers.append(
            answer_question(question, context, model, tokenizer, torch_device)
        )
    return all_answers


def get_results(
    question,
    cse,
    summarize=False,
    num_results=NUM_CONTEXT_FOR_EACH_QUESTION,
    verbose=True,
):
    """
    Return dict object containg a list of all context and answers related to the (sub)question
    """

    if verbose:
        print("Getting context ...")
    all_contexts = get_all_context(question, cse, num_results)

    if verbose:
        print("Answering to all questions ...")
    all_answers = get_all_answers(question, all_contexts)

    summary_answer = ""
    summary_context = ""
    if verbose and summarize:
        print("Adding summary ...")
    if summarize:
        summary_answer = get_summary(all_answers)
        summary_context = get_summary(all_contexts)

    if verbose:
        print("output.")

    return create_output_results(
        question, all_contexts, all_answers, summary_answer, summary_context
    )
