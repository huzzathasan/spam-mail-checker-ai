# pip install scikit-learn pandas joblib

# import all needed module
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import joblib

# load dataset
df = pd.read_csv('data.csv')

# preprocess data
df['Text'] = df["Text"].str.lower() # convert to lowercase
text = df['Text'].to_list()
lebel = df['Label'].to_list()

# Encode lebel
encoder = LabelEncoder()
encode_level = encoder.fit_transform(lebel)

# create a model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
    ('classifier', MultinomialNB())
])

# train model 
model.fit(text, lebel)

# save model
joblib.dump({
    'model': model,
    'encoder': encoder
}, "model-spam-mail-checker-1k-params.joblib")


"""
# try to test
load_model_data = joblib.load('model-spam-mail-checker-1k-params.joblib')
model = load_model_data['model']
res = model.predict(["Hello there!"])[0]
print(res) # output: 0 or 1; 0 = not spam 1 = spam
"""