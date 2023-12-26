#Python | Sort Python Dictionaries by Key or Value
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
myKeys = list(myDict.keys())
print(myKeys)
myKeys.sort()
print(myKeys)
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)
