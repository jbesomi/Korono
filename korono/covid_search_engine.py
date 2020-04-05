import string
import nltk
from nltk.corpus import stopwords
from rank_bm25 import BM25Okapi
import pandas as pd
import numpy as np


# adapted from https://www.kaggle.com/dgunning/building-a-cord19-research-engine-with-bm25
english_stopwords = list(set(stopwords.words("english")))


class CovidSearchEngine:
    """
    Simple CovidSearchEngine.

    Usage:

    cse = CovidSearchEngine(metadata_df) # metadata_df is a pandas dataframe with 'title' and 'abstract' columns
    search_results = cse.search("What is coronavirus", num=10) # Return `num` top-results
    """

    def remove_special_character(self, text):
        """
        Remove all special character from text string
        """
        return text.translate(str.maketrans("", "", string.punctuation))

    def tokenize(self, text):
        """
        Tokenize with NLTK

        Rules:
            - drop all words of 1 and 2 characters
            - drop all stopwords
            - drop all numbers
        """
        words = nltk.word_tokenize(text)
        return list(
            set(
                [
                    word
                    for word in words
                    if len(word) > 1
                    and not word in english_stopwords
                    and not word.isnumeric()
                ]
            )
        )

    def preprocess(self, text):
        """
        Clean and tokenize text input
        """
        return self.tokenize(self.remove_special_character(text.lower()))

    def __init__(self, corpus: pd.DataFrame):
        self.corpus = corpus
        self.columns = corpus.columns
        raw_search_str = (
            self.corpus.abstract.fillna("") + " " + self.corpus.title.fillna("")
        )
        self.index = raw_search_str.apply(self.preprocess).to_frame()
        self.index.columns = ["terms"]
        self.index.index = self.corpus.index
        self.bm25 = BM25Okapi(self.index.terms.tolist())

    def search(self, query, num):
        """
        Return top `num` results that better match the query
        """
        search_terms = self.preprocess(query)
        doc_scores = self.bm25.get_scores(search_terms)  # get scores

        ind = np.argsort(doc_scores)[::-1][:num]  # sort results

        results = self.corpus.iloc[ind][self.columns]  # Initialize results_df
        results["score"] = doc_scores[ind]  # Insert 'score' column
        results = results[results.score > 0]
        return results.reset_index()
