# Write a Python program to create a simple Bank Management System using conditional statements. 
# The program should allow the user to:

# 1. Check account balance
# 2. Deposit money
# 3. Withdraw money
# Display appropriate messages for invalid choices, invalid amounts, and insufficient balance.

Balance=5000
print("------------MENU (Choice)------------")
print("1. BALANCE",end="    ")
print("2. DEPOSIT",end="    ")
print("3. WITHDRAWAL")

#Taking Choice as Input
Choice=int(input("Enter your choice :"))

#Checking conditions and performing operations
if Choice==1:
    print("Your balance is",Balance,"Rs")
elif Choice==2:
    Amount=int(input("Enter your deposit amount:"))

    if Amount>0:
        Balance=Balance+Amount
        print("Deposit Successful !!!")
        print("Your updated balance is ",Balance,"Rs")
    else :
        print("Amount must be greater than 0")

elif Choice==3:
     Amount=int(input("Enter your withdrawal amount:"))
     if Amount>0 and Amount<= Balance:
        Balance=Balance-Amount
        print("Withdrawal Successful !!!")
        print("Your remaining balance is ",Balance,"Rs")
     elif Amount==0:
         print("Enter valid amount for withdrwal")
     else:
         print("Insufficient Amount")
else:
    print("Please enter valid choice ")
