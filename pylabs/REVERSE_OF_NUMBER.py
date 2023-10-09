a=int(input("Enter Number "))
num=0
sum=0
while(a!=0):
    num=int(a%10) #4 5
    sum=sum*10+num #4*10+0=40 40+50
    a=int(a/10)
print(sum)