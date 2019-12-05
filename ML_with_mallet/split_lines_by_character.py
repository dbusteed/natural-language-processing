#!/usr/bin/python3

import re

chars = ['JERRY', 'GEORGE', 'KRAMER', 'ELAINE']

lines = {
    'JERRY': [],
    'GEORGE': [],
    'KRAMER': [],
    'ELAINE': [],
}

# corpus from https://github.com/luonglearnstocode/Seinfeld-text-corpus
with open('corpus.txt', 'r') as f:
    for line in f:
        try:
            char,text = line.split(': ')
            if char in chars:

                # get rid of acting directions
                text = re.sub(r'\(.*\)', '', text)

                lines[char].append(text)
        except:
            pass

for char,char_lines in lines.items():
    for i,line in enumerate(char_lines):
        with open(f'sein_mallet/{char}/{i}.txt', 'w', encoding='utf8') as f:
            f.write(line)