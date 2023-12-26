#Ways to sort list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print(sorted(list,key=itemgetter('age','name')))