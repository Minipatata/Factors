num_user=int(input("Please enter any desired number"))
factors=[]
for i in range(1,num_user+1):
    if num_user % i==0:
        factors.append(i)
print(factors)