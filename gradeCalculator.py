#Program to create grade calculator in Python
s1=95
s2=92
s3=91
s4=90
s5=2
s6=7
total=s1+s2+s3+s4+s5+s6
avg=total/6
print(avg)

if avg>=90:
    print("A+")
elif avg>=80:
    print("A")
elif avg>=70:
    print("B+")
elif avg>=60:
    print("B")
else:
    print("Pass")      