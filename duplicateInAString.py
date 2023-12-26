#Python – Find all duplicate characters in string
from collections import Counter

def find_dup_char(input):
    count=Counter(input)
    
    for keys,values in count.items():
        if values>1:
         print(keys)



input = 'geeksforgeeks'
find_dup_char(input)