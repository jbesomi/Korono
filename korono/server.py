import os

from korono import covid_search_engine
from korono import load_data
from korono import korono_model

from transformers import DistilBertTokenizer
from transformers import DistilBertForQuestionAnswering
import torch

from flask import Flask
from flask import jsonify

app = Flask(__name__)

verbose = True

if app.debug and os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    print("Indexing database ... ")
    metadata_df = load_data.get_metadata_df()
    cse = covid_search_engine.CovidSearchEngine(metadata_df)

    torch_device = "cuda" if torch.cuda.is_available() else "cpu"

    print("Code running on: {}".format(torch_device))

    # "bert-large-uncased-whole-word-masking-finetuned-squad"
    model_name = "distilbert-base-uncased-distilled-squad"

    model = DistilBertForQuestionAnswering.from_pretrained(model_name)
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)

    model = model.to(torch_device)
    model.eval()

elif not app.debug:
    print("Indexing database ... ")
    metadata_df = load_data.get_metadata_df()
    cse = covid_search_engine.CovidSearchEngine(metadata_df)

    torch_device = "cuda" if torch.cuda.is_available() else "cpu"

    print("Code running on: {}".format(torch_device))

    # "bert-large-uncased-whole-word-masking-finetuned-squad"
    model_name = "distilbert-base-uncased-distilled-squad"

    model = DistilBertForQuestionAnswering.from_pretrained(model_name)
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)

    model = model.to(torch_device)
    model.eval()


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ask/<string:question>", methods=["POST"])
def show_post(question):
    # show the post with the given id, the id is an integer
    if verbose:
        print("Getting context ...")
    all_contexts = korono_model.get_all_context(question, cse, num_results=10)

    if verbose:
        print("Answering to all questions ...")
    all_answers = korono_model.get_all_answers(
        question, all_contexts, model, tokenizer, torch_device
    )

    return jsonify(
        korono_model.create_output_results(question, all_contexts, all_answers)
    )
