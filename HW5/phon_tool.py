## DAVIS BUSTEED 
## 09/2019

## IMPORTS
from nltk.corpus import cmudict
from sys import argv
import argparse

## CONSTANTS
RIME_FACTOR = 3

## FUNCTIONS
def get_rhymes(word):
    
    if len(word.split()) != 1:
        print('please only enter a single word')
        return

    try:
        prons = d_ents[word]
    except:
        print(f'"{word}" not found in CMUDict...')
        return

    # the different prounciations can 
    # give repeat rhymes, so use a set
    rhymes = set()

    for pron in prons:
        rime = pron[-RIME_FACTOR:]
        
        for w,p in l_ents:
            if p[-RIME_FACTOR:] == rime:
                rhymes.add(w)

    for r in sorted(rhymes):
        print(r)


def get_phones(word):

    for w in word.split():
    
        try:
            # only gonna deal with the first set of phones
            print(d_ents[w][0]) 
        except:
            print(f'"{w}" not found in CMUDict...')
    
## SETUP
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--rhyme', dest='rhyme', help='provide a word to find its rhymes')
parser.add_argument('-p', '--phones', dest='phones', help='provide a word/sentence to see its phonemes')
args = parser.parse_args()

## START
l_ents = cmudict.entries() # "list" of entries
d_ents = cmudict.dict()    # "dict" of entries

# if they are using command line args, single usage mode
if len(argv) > 1:
    
    if args.rhyme:
        get_rhymes(args.rhyme)
    
    if args.phones:
        get_phones(args.phones)

# interactive mode with repeating menu and options
else:
    inp = ''
    while inp != 'q':
        print('\n(1) Find phonemes\n(2) Find rhyming words\n(q) Quit\n')

        inp = input('?: ')

        if inp == '1':
            word = input('\nEnter a word or sentence (no punctuation): ')
            print('')
            get_phones(word)
        
        elif inp == '2':
            word = input('\nEnter a word to find its rhymes: ')
            print('')
            get_rhymes(word)