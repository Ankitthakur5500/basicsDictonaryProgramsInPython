#Python program to find the sum of all items in a dictionary
dictionary={'a': 100, 'b':200, 'c':300}
list=[]
# for x in dictionary:
#     list.append(dictionary[x])
# final=sum(list)
# print(final)
sum=0
for x in dictionary.values():
    sum+=x
print(sum)