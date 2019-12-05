import re

raw = open('raw_tweets.txt', 'r', encoding='utf8').read()
raw = raw.split('<NEWTWEET>')

raw = list(map( lambda t: re.sub(r'\u3000', ' ', t), raw ))
raw = list(map( lambda t: re.sub(r'\n', ' ', t), raw ))

raw = [t for t in raw if len(t) > 1]
raw = [t for t in raw if not re.match(r'^RT', t)]

with open('clean_tweets.txt', 'a', encoding='utf8') as f:
    for t in raw:
        f.write(t)
        f.write('\n')