#Python – Key with maximum unique values
test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
unique_counts = [(keys,len(set(values))) for keys,values in test_dict.items()]
print(unique_counts)
max_key = max(unique_counts)[0]
print(max_key)  