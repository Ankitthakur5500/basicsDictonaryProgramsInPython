#Python program to find the sum of all items in a dictionary
dict = {'a': 100, 'b': 200, 'c': 300}
sum=0
for x in dict.values():
    sum+=x
print(sum)