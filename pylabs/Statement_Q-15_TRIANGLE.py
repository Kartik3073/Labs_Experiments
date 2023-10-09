num1=int(input("Enter Side Number1: "))
num2=int(input("Enter Side Number2: "))
num3=int(input("Enter Side Number3: "))
if(num1==num2 and num1==num3):
    print("The Triangle Is Equilatoral")
elif(num1==num2 or num1==num3):
    print("The Triangle Is Isosceles")
else:
    print("The Triangle Is Scalene")