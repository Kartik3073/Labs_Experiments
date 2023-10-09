price=int(input("Enter Bike Price: "))
if(price>100000):
    print(" Tax Price 15% ",price*0.15)
elif(price>50000 and price<=100000):
    print(" Tax Price 10% ",price*0.10)
elif(price<=50000):
    print(" Tax Price 5% ",price*0.5)