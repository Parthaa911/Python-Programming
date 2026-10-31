#Factorial of a number
num=int(input("Enter a number: "))
fact= 1
i= 1

while i <= num:
    fact= fact*i
    i += 1

print("Factorial: ",fact)


#Reverse the number
num=int(input("Enter a numbe: "))
reverse= 0

while num > 0 :
    digit= num % 10
    reverse= reverse * 10 + digit
    num= num // 10
print("Reverse number: ",reverse)


#Palindrome number 
num=int(input("Enter a numbe: "))
original= num
reverse= 0

while num > 0 :
    digit= num % 10
    reverse= reverse * 10 + digit
    num= num // 10

if original == reverse:
    print(reverse," is palindrome number")
else :
    print(reverse,"is not palindrome number")
    

#Sum of the digits
num=int(input("Enter a number: "))
total= 0

while num > 0:
    digit= num % 10
    total= total + digit
    num= num // 10

print("Sum of digits: ",total)


#Count number of digit
num=int(input("Enter a number: "))
count= 0

if num == 0:
    count= 1

while num > 0 :
    num = num // 10
    count +=1
print("Total digits: ",count)

