<h1 align="center">👑 Korono</h1>

<p align="center">A Question-Answering system for COVID-19 papers</p>

<p align="center">
  <a href="https://github.com/jbesomi/korono/stargazers">
    <img src="https://img.shields.io/github/stars/jbesomi/korono.svg?colorA=orange&colorB=orange&logo=github"
         alt="GitHub stars">
  </a>
  <a href="https://korono.readthedocs.io/">
      <img src="https://readthedocs.org/projects/korono/badge/?version=latest"
           alt="ReadTheDoc">
    </a>
  <a href="https://pypi.org/search/?q=korono">
      <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/korono">
  </a>
  <a href="https://github.com/jbesomi/korono/issues">
        <img src="https://img.shields.io/github/issues/jbesomi/korono.svg"
             alt="GitHub issues">
  </a>
  <a href="https://github.com/jbesomi/korono/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/jbesomi/korono.svg"
             alt="GitHub license">
  </a>  
</p>

<p align="center">
   <a href="#why">Introduction</a> •
   <a href="#getting-started">Getting started</a> •
   <a href="#under-the-hoods">Under the hoods</a> •
   <a href="#server-and-client-api">Server and Client API</a>
</p>

<p align="center">
    <img src="github/ai-coronavirus.png" width="700">
</p>


<h2 align="center">Introduction</h2>

**information.** The amount of documents related to COVID-19 is increasing exponentially. With such a massive amount of information, it's getting harder for the research community to find the relevant pieces of information.

**Search-engine-on-steroids.** Korono is a question-answering platform conceived to facilitate the research of information regarding COVID-19. You can think of Korono as a search-engine-on-steroids.

**Working principle.** Korono engine is composed of two phases: the search engine phase and the question-answering phase. In the first place, given a query `q`, the search engine returns all relevant papers from that query. Later on, the answer is extracted from each paper and displayed.

<h2 align="center">Getting started</h2>

You can either use the online version (coming soon) or run your own server.

Run a server locally:
```
./run_server.sh
```

Run client and ask a question:
```python
> from korono import client
> client.get_answers("What is coronavirus?")
```

<h2 align="center">Under the hoods</h2>


**Search engine**. The search engine use a ranking algorithm known as Okapi BM25, where BM stands for _best matching_. BM25 is a bag-of-words retrieval function that sort documents based on the query terms appearing in each document.

**Question answering**. The questions are extracted from the corpus using [Transformers](https://transformer.huggingface.co/), large neural networks language models. As of now, only the `distilbert-base-uncased-distilled-squad` model is supported. Soon, we plan to extend support.

<h2 align="center">Server and Client API</h2>

#### Server API

- `load_data.get_df()`
   Returns the underline dataset.

- `load_data.get_metadata_df()`
   Returns the CORD-19 metadata pandas DataFrame.

- `korono_model.answer_question(question, context)`
   Given a question and a context, returns the answer.

- `korono.model.get_summary(text)`
   Given a text, the model returns the abstractive summary.

- `korono_model.find_start_end_index_substring(context, answer)`
   Return the start and end index, if they exists, of the `answer` string in the `context` string.

#### Client API


- `client.get_answers_json(question)`
   Return a JSON object of the form:
```json
      {
         'results': {[
               {
               'context': 'coronavirus is an infectious disease',
               'question': 'what is coronavirus?'
               'answer': 'an infectious disease',
               },
         ]}
      }
```

- `client.get_answers(question)`
   Return a list of all answers.
