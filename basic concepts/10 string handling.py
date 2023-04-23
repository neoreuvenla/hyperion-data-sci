# task 11 - string handling
# purpose - alternates capital characters and words in a given string

user_string = input("Enter a string:\t\t")  # prompts user for a string


# functionality one - converting alternating characters

alternate_characters = "" # string to hold converted characters

i = 0  
while i < len(user_string):  # loops while characters exist to be converted
    
    if i % 2 == 0:  # converts to upper case if the current position is even
        alternate_characters += user_string[i].upper()

    else:  # converts to lower case if the current position is odd
        alternate_characters += user_string[i].lower()
    
    i += 1  # increments to allow iteration over the string

print("\nAlternate Characters:\t{}".format(alternate_characters)) 


# functionality two - converting alternating words

split_words = user_string.split()  # splits original string into a list
alternate_words = []               # empty list to hold converted words

j = 0
while j < len(split_words):  # loops while words exist to be converted
    
    if j % 2 == 0:  # converts to lower case if the current position is even
        alternate_words.append(split_words[j].lower())

    else:  # converts to upper case if the current position is odd
        alternate_words.append(split_words[j].upper())

    j += 1  # increments to allow iteration over the list

print("Alernate Words:\t\t" + " ".join(alternate_words))  # joins and prints