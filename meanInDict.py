#Python – Dictionary Values Mean
test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10} 
sum=0
length=len(test_dict)
for x in test_dict.values():
    sum+=x
mean = sum/length
print(mean)
