#Take a number from the user and check the number is even or odd.
num=int(input("Enter a number :"))
if num%2 == 0:
    print(num,"is even number.")
else:
    print(num,"is odd number.")

#Take a age from user and check the user is eligible for for voting or not.
age=int(input("\nEnter your age :"))
print("Age :",age)
if age >= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")

#Take a number from the user and check which number is bigger.
num1=int(input("\nEnter a first number :"))
num2=int(input("Enter a second number :"))
if num1>num2 :
    print(num1,"is biggesr than",num2)
else:
    print(num2,"is biggesr than",num1)