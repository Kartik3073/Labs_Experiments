Physics=int(input("Enter Physics Marks: "))
Chemistry=int(input("Enter Chemistry Marks: "))
Maths=int(input("Enter Maths Marks: "))
English=int(input("Enter English Marks: "))
Hindi=int(input("Enter Hindi Marks: "))
suplymentry=0
if(Physics<=35):
    print("Supplymentry in Physics")
    suplymentry+=1
if(Chemistry<=35):
    print("Supplymentry in Chemistry")
    suplymentry+=1
if(Maths<=35):
    print("Supplymentry in Maths")
    suplymentry+=1
if(English<=35):
    print("Supplymentry in English")
    suplymentry+=1
if(Hindi<=35):
    print("Supplymentry in Hindi")
    suplymentry+=1
percentage=((Physics+Chemistry+Maths+English+Hindi)/500)*100
print(percentage)
if(suplymentry==3):
    print("fail")
else:  
    if(percentage>=75):
        print(" Excellent: Grade A")
    elif (percentage>=60):
        print("Good : Grade B")
    elif (percentage>=50):
        print("can do Much Better : Grade c")
    elif(percentage>=33):
        print("Pass : Grade d")
    else:
        print("fail....")
    
    