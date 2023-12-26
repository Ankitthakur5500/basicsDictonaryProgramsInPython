test_list = ["Gfg", "is", "Best"]
  
subs_dict = {
    "Gfg" : [5, 6, 7], 
    "is" : [7, 4, 2], 
}
 
K = 2
 
for i in range(len(test_list)):
    if test_list[i] in subs_dict:
        test_list[i] = subs_dict[test_list[i]][K]
 
print("The list after substitution : " + str(test_list))