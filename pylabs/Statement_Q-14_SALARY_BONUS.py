salary=int(input("Enter The salary: "))
years=int(input("Enter The years of employement: "))
if(years>10):
    print(" your Bonus For 10%: ",salary*0.10)
elif(years>=6 and years<=10):
    print(" your Bonus For 8%: ",salary*0.08)
elif(years<6):
    print(" your Bonus For 5%: ",salary*0.05)
