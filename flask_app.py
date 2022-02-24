from flask import Flask
import urllib.request
import pickle
import numpy as np
import pandas as pd
from flask import request
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# prediction function
def ValuePredictor(to_predict_list):
    # download model
    urllib.request.urlretrieve("https://raw.githubusercontent.com/realzza/cloud_computing_project2/master/tween_m.pkl", "tweet_model.pkl")
    # tokenizing    
    models = pickle.load(open("tweet_model.pkl", "rb"))
    countVect = models[0]
    tfidf_trans = models[1]
    clf = models[2]
    X_sample_counts = countVect.transform(to_predict_list)
    X_sample_tfidf = tfidf_trans.transform(X_sample_counts)
    result = clf.predict(X_sample_tfidf)
    return result[0]
 
app = Flask(__name__)

@app.route('/api/american', methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        request_dict = request.get_json()
        request_pred = ValuePredictor(list(request_dict.values()))
        print(request_pred)
        if request_pred == 0:
            return {"is_american": 0, "version": "0.2.2", "model_date": "2022-02-24"}
        else:
            return {"is_american": 1, "version": "0.2.2", "model_date": "2022-02-24"}
    
    else:
        return "hi"
        
