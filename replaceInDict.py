#Python – Replace words from Dictionary
test_str = 'geekforgeeks best for geeks'
lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
temp=[]
for word in test_str.split():
    temp.append(lookp_dict.get(word,word))
string = " ".join(temp)
print(string)