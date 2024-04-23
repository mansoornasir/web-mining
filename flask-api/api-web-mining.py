from flask import Flask, request, jsonify
import pandas as pd 
import spacy 
import requests 
from bs4 import BeautifulSoup
nlp = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)
from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake


app = Flask(__name__)

# Sample data (can be replaced with a database)
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Flask Development", "author": "Jane Smith"}
]

# Read all books
@app.route('/ner', methods=['GET'])
def get_ner():
    data = request.get_json()
    content = data["content"]

    doc = nlp(content)

    for ent in doc.ents:
        # print(ent.text, ent.start_char, ent.end_char, ent.label_)
        return jsonify(ent.text, ent.start_char, ent.end_char, ent.label_)


# Read all books
@app.route('/tf', methods=['GET'])
def get_tf():
    data = request.get_json()
    # assign documents

    d1 = data["d1"]
    d2 = data["d2"]
    d3 = data["d3"]

    # return data
    # merge documents into a single corpus
    string = [d1, d2, d3]

    # create object
    tfidf = TfidfVectorizer()

    # get tf-df values
    result = tfidf.fit_transform(string)

    # get idf values
    # print('\nidf values:')
    # for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
    #     print(ele1, ':', ele2)

    # get indexing
    # print('\nWord indexes:')
    # return str(tfidf.vocabulary_)

    # display tf-idf values
    # print('\ntf-idf value:')
    # return (str(result))

    # in matrix form
    # print('\ntf-idf values in matrix form:')
    # return (str(result.toarray()))

@app.route('/rake', methods=['GET'])
def get_rake():
    r = Rake()
    data = request.get_json()
    content = data["content"]
    r.extract_keywords_from_text(content)
    # Extraction given the list of strings where each string is a sentence.
    # r.extract_keywords_from_sentences(<list of sentences>)

    # To get keyword phrases ranked highest to lowest.
    # print(r.get_ranked_phrases()[0:5])

    # To get keyword phrases ranked highest to lowest with scores.
    return(r.get_ranked_phrases_with_scores()[0:5])


if __name__ == '__main__':
    app.run(debug=True)
