# task 20 - intro to natural language processing
# purpose - tokenise sentences and investigate found entities

import spacy

# load the spacy english language model
nlp = spacy.load('en_core_web_sm')

# list of garden path sentences
gardenpathSentences = [
    "The man whistling tunes pianos.",
    "The man who hunts ducks out on weekends.",
    "Mary gave the child a Band-Aid.", 
    "That Jill is never here hurts.",  
    "The cotton clothing is made of grows in Mississippi."]

# iterate over each sentence and print the sentence, tokens, entities
for sentence in gardenpathSentences:

    # tokenise the current sentence
    tokenised_sentence = nlp(sentence)

    # print the original sentence for clarity
    print("\nSENTENCE:", sentence)
    
    # print the sentence tokens and their word classes separated with /
    tokens = " / ".join([f"{token.text} {token.pos_}" for token in tokenised_sentence])
    print("TOKENS:", tokens)
    
    # print any named entites recognised
    if not tokenised_sentence.ents:  # if no entities
        print("ENTITIES: None found")
    
    else:  # if entities found
        # prints in the format entity word (entity code: entity explanation)
        entities = " / ".join([f"{ent.text} ({ent.label_}: {spacy.explain(ent.label_)})"
                            for ent in tokenised_sentence.ents])
        print("ENTITIES:", entities)
    
    print("\n" + "-" * 100)  # seperator for clarity

# Entity 1: 
# - PERSON, which encompasses both real and fictional people (eg. Jill)
# - The label was fairly self explanatory, but it was helpful to know it included fictional people too

# Entity 2: 
# - GPE, which encompasses countries, cities, and states (eg. Mississippi)
# - The acronym wasn't clear on its own, but made sense with the explanation from spacy.explain

# Entity Note:
# It was interesting to read about the issues spaCy may have with some trademarked brand names,
# especially where they have become a generalised term for a product, like Band-Aid and Hoover