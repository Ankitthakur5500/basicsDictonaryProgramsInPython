#Find common elements in three sorted arrays by dictionary intersection

def common_element(ar1,ar2,ar3):
    l1,l2,l3=len(ar1),len(ar2),len(ar3)
    i,j,k=0,0,0
    common = []
    while(i<l1 and j<l2 and k<l3):
        if ar1[i]==ar2[j]==ar3[k]:
            common.append(ar1[i])
            i+=1
            j+=1
            k+=1
        elif ar1[i]<ar2[j]:
            i+=1    
        elif ar2[j]<ar3[k]:
            j+=1
        else:
           k+=1 
    return common


ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
print(common_element(ar1,ar2,ar3))