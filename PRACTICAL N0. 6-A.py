'''A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: "The quick brown fox jumps over the lazy dog".
Your task here is to write a function to check a sentence to see if it is a pangram or not.'''

import string
import sys

def ispangram(str1,alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Python Programming"))

print("This programme is  done by 'Farooq Hussain'")