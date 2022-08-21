# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:14:06 2022

@author: Anil munde
"""

from flask import Flask,render_template,request
import pickle
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

###Loading model and cv
cv = pickle.load(open('cv.pkl','rb'))
model = pickle.load(open('senta.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        new_senta = request.form['senta']
        new_senta = re.sub('[^a-zA-Z]', ' ', new_senta)
        new_senta = new_senta.lower()
        new_senta = new_senta.split()
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        new_senta = [ps.stem(word) for word in new_senta if not word in set(all_stopwords)]
        new_senta = ' '.join(new_senta)
        new_corpus = [new_senta]
        new_X_test = cv.transform(new_corpus).toarray()
        pred = model.predict(new_X_test)
        return render_template('result.html',prediction=pred)

if __name__ == "__main__":
    app.run(debug=True)   
    