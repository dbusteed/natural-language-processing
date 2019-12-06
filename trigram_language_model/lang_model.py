## IMPORTS
from nltk.corpus import reuters, brown
from nltk import trigrams
import json
import sys
import os

## CONSTANTS
MODEL_FILE = 'model'

## FUNCTIONS
def get_freq(words):
    words = words.lower().split()[:2]
    words = tuple(words)

    if len(words) != 2:
        print('\nplease enter exactly two words...')
        return

    try:
        for res in model[words][:10]:
            print(f'{res[0]} -- {res[1]:4.3f}')
    except KeyError:
        print(f'sequence "{words[0]} {words[1]}" not found...')

## READ or BUILD THE MODEL
if os.path.exists(MODEL_FILE):

    print('\nusing previous model file (delete it, and restart if changes were made)')
    model = json.loads( open(MODEL_FILE, 'r', encoding='utf8').read() )

    if len(model) == 0:
        print('\nmodel file is empty, delete the file then restart script')
        sys.exit(1)

    for k in model.copy().keys():
        new_k = tuple(k.split('__&&__'))
        model[new_k] = model.pop(k)

else:

    print('\nno model found...')
    print('\nbuilding language model...')

    model = {}

    for sent in reuters.sents() + brown.sents():
        for w1, w2, w3 in trigrams(sent):     
            w1, w2, w3 = w1.lower(), w2.lower(), w3.lower()
            if (w1, w2) not in model:
                model[(w1, w2)] = {w3: 1}
            else:
                if w3 not in model[(w1, w2)]:
                    model[(w1, w2)][w3] = 1
                else:
                    model[(w1, w2)][w3] += 1

    for v in model.values():
        v['<MAX>'] = max(v.values())

    t = list(model.items())

    t = sorted(t, key=lambda x: x[1]['<MAX>'], reverse=True)

    model = dict(t)

    for k,v in model.items():
        v.pop('<MAX>', None)
        model[k] = sorted(v.items(), key=lambda x: x[1], reverse=True)

    for k,v in model.items():
        summ = 0
        t = []
        for _,c in model[k]:
            summ += c
        for w,c in model[k]:
            t.append((w, c/summ))
        model[k] = t

    # save the model file for next time
    # but json doesn't like tuple keys, so gotta combine
    out_model = model.copy()
    for k in out_model.copy().keys():
        new_k = '__&&__'.join(k)
        out_model[new_k] = out_model.pop(k)

    with open(MODEL_FILE, 'w', encoding='utf8') as f:
        f.write(json.dumps(out_model))

    print('\nmodel saved to file')

while True:

    query = input('\nEnter two words seperate by space (or \'q\' to exit)\n: ')

    if query == 'q':
        sys.exit(0)
    else:
        get_freq(query)