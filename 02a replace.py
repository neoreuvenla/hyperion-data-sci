# variable to hold string manipulations
raw_phrase = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
cleaned_phrase = raw_phrase.replace("!", " ")
upper_phrase = cleaned_phrase.upper()
backwards_phrase = cleaned_phrase[::-1]

# print the three string variations variables
print("Phrase with no excalmation marks:")
print(cleaned_phrase)

print("\nPhrase in upper case:")
print(upper_phrase)

print("\nPhrase backwards:")
print(backwards_phrase)