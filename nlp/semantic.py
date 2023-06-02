# task 21a - semantic similarity (nlp)
# purpose - to compare similarity of words and sentences

# compulsory task 1 ###############################################################
# q1 "write a note about what you found interesting about the similarities between cat, 
# monkey and banana":
# the similarities of the original word list (cat, monkey, banana) is interesting
# on two levels. firstly, the similarities indicated match what would be expected
# from common sense: a cat and monkey are similar because they are animals but a 
# cat and a banana are not similar at all. secondly, and perhaps more interestingly,
# the en_core_web_md model seems to be able to reflect more contextual information: 
# although a monkey and banana are not the same type of thing, they are frequently
# associated together in media and general human thought and scored appropriately, 
# whereas cats and bananas are rarely, if ever, portrayed together and so recieve 
# a lower similarity score. 
#
# q2 run the example file with ‘en_core_web_sm’ and write a note on what you notice 
# is different from the model 'en_core_web_md':
# generally, the en_core_web_sm model has higher similarity scores than the 
# en_core_web_md models. the md model has larger vocabulary size and word vectors,
# than the sm model. the consequence is that the en_core_web_sm model is likely to 
# be less capable of nuanced semantic understanding. this is best illustrated in 
# the words apple and boat: While the en_core_web_sm model, given its established 
# limitations, provides a relatively high similarity score of 0.755, the 
# en_core_web_md model better recognizes their semantic dissimilarity, resulting 
# in a much lower score of 0.023. this is also present in sentence similarity
# evaluations. en_core_web_md gives higher similarity scores for sentences with 
# overlapping content, while en_core_web_sm returns relatively lower results due
# to its inability to capture extended nuance
###################################################################################

# imports
import spacy 
import warnings

# suppress a warning from the sm model, if used, which clutters output
warnings.filterwarnings("ignore", category=UserWarning)

# select either small or medium model for use
nlp = spacy.load('en_core_web_md')  
#nlp = spacy.load('en_core_web_sm')  

# similarity with spacy ###########################################################

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("cat and monkey = ", word1.similarity(word2))
print("banana and monkey = ", word3.similarity(word2))
print("banana and cat = ", word3.similarity(word1))

word4 = nlp("boat")
word5 = nlp("slowly")
word6 = nlp("apple")

print("boat and slowly = ", word4.similarity(word5))
print("apple and slowly = ", word6.similarity(word5))
print("apple and boat = ", word6.similarity(word4))

# working with vectors ############################################################

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# working with sentences ##########################################################

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)