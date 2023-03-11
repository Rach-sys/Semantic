# Compare cat, monkey and banana using similarity
# Tokenisation
# Use a for loop to retrieve each variation once e.g cat cat, cat apple, cat monkey and cat banana
# There is only 1.0 similarity between the same two options
# A warning message is received when using the en_core_web_sm model

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
