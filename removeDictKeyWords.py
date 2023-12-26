#Python – Remove Dictionary Key Words
test_str = 'gfg is best for geeks'
test_dict = {'geeks': 1, 'best': 6}

for key in test_dict:
    if key in test_str.split():
        test_str=test_str.replace(key," ")

print(test_str)