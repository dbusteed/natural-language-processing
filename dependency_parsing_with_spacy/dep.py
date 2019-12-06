import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

# example from class
# doc = nlp('The boy put the tortoise on the rug.')

# 1 Nephi 1:3
# doc = nlp('And I know that the record which I make is true; and I make it with mine own hand; and I make it according to my knowledge.')

# Hamlet
# doc = nlp("To be, or not to be- that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles, And by opposing end them. To die- to sleep- No more; and by a sleep to say we end The heartache, and the thousand natural shocks That flesh is heir to.")

# Review from Google Maps
# doc = nlp('I HATE this school so so much. I feel like I made the worst decision by coming to this school. When I wake up every morning, the first thing come up in my mind is whatever homework is due, and the last thing I do everyday is to finish typing all the essays I have from the classes. I feel like I can not breath from those pressures. I encourage everyone please DO NOT come to BYU, it is worse than going to hell!!!!')

# New York Times headline + first line
# doc = nlp('Trump Orders Withdrawal of U.S. Troops From Northern Syria. Defense Secretary Mark T. Esper said Sunday that President Trump ordered a withdrawal of American forces from northern Syria, a decision that will effectively cede control of the area to the Syrian government and Russia, and could allow a resurgence of the Islamic State.')

for sent in doc.sents:
    for token in sent:
        print(f'{token.text:<20} {token.dep_}')
    print()   

displacy.serve(list(doc.sents), style='dep')