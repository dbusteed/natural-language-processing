from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

CORPUS_PATH = 'reviews'

file_names = os.listdir(CORPUS_PATH)

sid = SentimentIntensityAnalyzer()

for file_name in file_names:
    text = open(os.path.join(CORPUS_PATH,file_name), 'r').read()
    scores = sid.polarity_scores(text)
    print(f"{file_name}    {scores['compound']}")