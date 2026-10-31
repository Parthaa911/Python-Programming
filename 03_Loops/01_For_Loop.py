#Print numbers between 1 to 10 using for loop
print("Numbers between 1 to 10 :")
for i in range(1,11):
    print(i)

#Print even numbers between 1 to 10 using for loop
print("\nEven numbers between 1 to 10 :")
for i in range(1,11):
    if i % 2 ==0:
        print(i)

#Print odd numbers between 1 to 10 using for loop
print("\nOdd numbers between 1 to 10 :")
for i in range(1,11):
    if i % 2 != 0:
        print(i)

#Print 5 table using  for loop
print("\nTable of 5 :")
num=5
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#List of Fruits and Print each Fruit using for loop
print("\nFruits: ")
for i in ['Apple','Banana','Grape','Mango','Watermelon']:
    print(i)

#Print 5th and 7th table side by side using for loop
print("\nTable of 5  and 7:")
num1=5
num2=7
for i in range(1,11):
    print(f"{num1} x {i} = {num1*i}" ,end= "     ")
    print(f"{num2} x {i} = {num2*i}")