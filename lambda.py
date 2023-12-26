#Ways to sort list of dictionaries by values in Python – Using lambda function
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print(sorted(list,key=lambda i:(i['age'],i['name'])))