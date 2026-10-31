#Print numbers between 1 to 5 using while loop
print("Numbers between 1 to 5 :")
num=1
while  num <=5:
    print(num)
    num += 1

#Print even numbers between 1 to 10 using while loop
print("\nEven numbers between 1 to 10 :")
num=2
while num<=10:
    print(num)
    num += 2

#print sum of 1 to 5
print(("\nSum of 1 to 5"))
num=1
total=0
while num <= 5:
    total += num
    num +=1
print("Total :",total)

#Print simple menu using  while loop 
while(True):
    choice=input("\nContinue ?(y/n) :")
    if choice == "y":
        print("Hello !!!")
        continue
    elif choice=="n":
        break
    else:
        print("Enter valid input")

