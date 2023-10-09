import random
rd=random.randint(1,9)
ges=0
c=0
while ges != rd and ges != "exit":
     ges=int(input("Enter a guess between 1 to 9:-"))
     if ges == "exit":
        break

     ges=int(ges)
     c+=1
     if ges<rd:
        print("To low")

     elif ges>rd:
        print("To high")

     else:
        print("RIGHT")
        print("You took only",c,"tries")
input()              