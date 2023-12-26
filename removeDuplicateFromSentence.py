#Python | Remove all duplicates words from a given sentence
from collections import Counter

strin = []
def duplicate(input):
    data = Counter(input.split())
    for key,value in data.items():
        if value==1:
             strin.append(key)
        
input='Python is great and Java is also great'
duplicate(input)
strg = " ".join(strin)
print(strg)
