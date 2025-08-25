n=int(input("enter any num :"))
num=[]
while(n!=1 or n not in num):
    num.append(n)
    n=sum([int(i)*int(i) for i in str(n)])
print(num)
if n==1:
    print("round")
else:
    print("no")