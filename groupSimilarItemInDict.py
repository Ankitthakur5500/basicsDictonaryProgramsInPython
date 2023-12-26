#Python – Group Similar items to Dictionary Values List
from collections import defaultdict
 
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
 
res = defaultdict(list)
print(res)
for ele in test_list:
     
    res[ele].append(ele)
 
print(res)