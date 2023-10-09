unit=int(input("Enter Unit: "))
first100=(unit-100)
bill100=first100*5
secound100=(first100-175)*10
if (unit<=100):
    print("No Charge")
if(unit>=100):
    unit=unit-100
    print(unit)
    if(unit<=100):
        print("your Bill ",first100)
    if(unit>=100):
        print("your Bill ",bill100+secound100)

