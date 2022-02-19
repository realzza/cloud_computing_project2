from flask import Flask
import pickle
import numpy as np
import pandas as pd
from flask import request
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# prediction function
def ValuePredictor(to_predict_list):
    # tokenizing    
    models = pickle.load(open("tween_m.pkl", "rb"))
    countVect = models[0]
    tfidf_trans = models[1]
    clf = models[2]
    X_sample_counts = countVect.transform(to_predict_list)
    X_sample_tfidf = tfidf_trans.transform(X_sample_counts)
    result = clf.predict(X_sample_tfidf)
    return result[0]
 
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        request_dict = request.get_json()
        request_pred = ValuePredictor(list(request_dict.values()))
        print(request_pred)
        if request_pred == 0:
            return {"is_american":"I am not from the US"}
        else:
            return {"is_american":"I am from the US"}
    
    else:
        return "fuck you"
        # to_predict_list = request.form.to_dict()
        # print(to_predict_list)
        # to_predict_list = list(to_predict_list.values())
        # to_predict_list = list(map(int, to_predict_list))
        # result = ValuePredictor(to_predict_list)       
        # if int(result)== 1:
        #     prediction ='Income more than 50K'
        # else:
        #     prediction ='Income less that 50K'           
        # return render_template("result.html", prediction = prediction)
        
