from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.corpus import subjectivity
from nltk.sentiment.util import *
from nltk import word_tokenize
from random import shuffle

import os

CORPUS_PATH = 'reviews'

file_names = os.listdir(CORPUS_PATH)

pos_docs = []
neg_docs = []

for file_name in file_names:
    text = open(os.path.join(CORPUS_PATH, file_name), 'r').read()
    text = word_tokenize(text)
    if 'pos' in file_name:
        pos_docs.append((text, 'pos'))
    else:
        neg_docs.append((text, 'neg'))

shuffle(pos_docs)
shuffle(neg_docs)

train_docs = pos_docs[:5] + neg_docs[:5]
test_docs = pos_docs[5:] + neg_docs[5:]

sentim_analyzer = SentimentAnalyzer()

all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in train_docs])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(train_docs)
test_set = sentim_analyzer.apply_features(test_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

for k,v in sorted(sentim_analyzer.evaluate(test_set).items()):
    print(f'{k}: {v}')