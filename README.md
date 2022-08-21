# Article-Sentiment-Analysis
Using python, train sentiment analysis model(s) for an article dataset of over 20,000 articles  and as well as develop a web-app to take in the input of any title plus article text and return the relevant sentiment analysis values you can take out (Prediction).

Sentiment analysis is the contextual mining of words that reveals the social sentiment of a brand and aids businesses in determining if the product they are producing will find a market.
For this assignment, I attempted to train my model in two methods:

Rule Based Approach:
In this attempt text mining is used to demonstrate how to use Python to compute two scores: sentiment polarity and subjectivity. It may determine whether the text contains positive or negative feedback by looking at the polarity, which ranges from -1 to 1 (negative to positive). 

Files:
SentimentAnalysis.ipynb

Automatic Approach:
This strategy utilizes the machine learning method. Predictive analysis is first performed once the datasets have been trained. Word extraction from the text is the subsequent procedure. Creating a model using MultinomialNB,GaussianNB.
This method has been used for the Webapp, using NLTK and deployed using Heroku.


Files:
  index.html  ## homepage file
  result.html ## to show prediction
  styles.css  ## css file
  app.py  ## main flask file
  Sentiment Analysis Webapp.ipynb
  cv.pkl
  senta.pkl
