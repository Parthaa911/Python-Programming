#Factorial of Number 
num=int(input("Enter a number: "))
fact=1

for i  in range(1,num+1):
    fact=fact*i

print("Factorial: ",fact)



#Reverse a Number 
num=int(input("Enter a number: "))
reverse= ""

for digit in str(num):
    reverse= digit + reverse

print("Reverse Number: ",reverse)



#Palindrome Number
num=int(input("Enter a number: "))
reverse= ""

for digit in str(num):
    reverse= digit + reverse

if str(num) == reverse:
    print(reverse,"is palindrome number.")
else:
    print(reverse,"is not palindrome number.")


#Sum of digit
num=int(input("Enter a number :"))
total= 0

for digit in str(num):
    total = total + int(digit)

print("Sum of digits: ",total)


#Count number of digits
num=int(input("Enter a number: "))
count= 0

for digit in  str(num):
    count += 1

print("Total digits: ",count)


