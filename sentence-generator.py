import random

noun_list = ["dog", "cat", "giraffe", "computer", "donut", "cup of coffee", "teacher", "sister", "robot", "blowfish", "laptop", "Nintendo Switch"]
verb_list = ["jumps", "runs", "sleeps", "acts", "sings", "codes", "eats", "cries", "laughs", "skips", "hops"]
adjective_list = ["green", "tired", "gorgeous", "incandescent", "bright", "smart", "kind", "confused", "resolute", "happy", "brave", "calm", "ugly"]
adverb_list = ["lazily", "happily", "gleefully", "sadly", "energetically", "dejectedly", "resignedly", "actively", "purposefully", "practically"]
preposition_list = ["under", "over", "through", "behind", "beneath", "next to", "atop", "astride", "beside", "around"]
article_list = ["a", "the"]

#make myself a function for generating noun phrases
def noun_phrase():
    return random.choice(article_list) + " " + \
    random.choice(adjective_list) + " " + \
    random.choice(noun_list)

def verb_phrase():
    return random.choice(adverb_list) + " " + \
    random.choice(verb_list)

def prepositional_phrase():
    return random.choice(preposition_list) + " " + \
    noun_phrase()

def sentence():
    return noun_phrase() + " " + verb_phrase() + \
    " " + prepositional_phrase()

#try out noun phrase generator a few times
print(sentence())
