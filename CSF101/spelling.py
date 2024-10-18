#########

#Sonam Sangay Yoezer
#A
#02240366

#########

#Dzongkha NPL, 
# #Chat GPT, 
# Youtube.

########

import re

spell = ()

text = input("366.txt")
words = text.split()

misspelled = spell.unknown(words)

if misspelled:
    print("spelling mistake")

    corrected_word = spell.correction(word)
    print(f"{word}={corrected_word}")

else:
    print("no mistake")
