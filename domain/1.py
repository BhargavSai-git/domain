a=int(input("enter a lower number"))
b=int(input("enter higher number"))
for i in range(a,b):
    c=0
    for j in range (2,i):
        if(i%j==0):
            c=c+1
    if(c==0):
        print(i, end=" ")
