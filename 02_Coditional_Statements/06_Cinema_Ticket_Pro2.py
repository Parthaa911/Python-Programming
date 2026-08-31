# Write a Python program to create a Cinema Ticket Calculator that calculates the total ticket price
# based on the customer's age, day of booking, and number of tickets.

# 1. Children (below 12 years): Ticket price is $6.
# 2. Adults (12–64 years): Base ticket price is $12.
# 3. On Saturday and Sunday, add a $2 surcharge per ticket.
# 4. On Wednesday, give a $3 discount per ticket.
# 5. Senior Citizens (65 years and above):
# 6. Get a 50% discount on the base ticket price.
# 7. On Saturday and Sunday, add a $2 surcharge per ticket.

print("==========Cinema Ticket Calculator===========")

#Taking Input (Day,Age and No. of Tickets)
day=input("Enter Day :")
age=int(input("Enter Age:"))
tickets=int(input("Enter no of tickets :"))
price=12
discount=0
surcharge=0

#Checking Conditions
if  age<12:
    category='Children'
    price=6

elif age>=65:
    category='Senior Citizens'
    discount=(price*50)/100

    if day=="saturday" or day=='sunday':
        surcharge=2

else :
    category='Adult'
    if day=="saturday" or day=='sunday':
            surcharge=2
    elif day=='wednesday':
         discount=3

#Calculations
Total= (price - discount + surcharge)*tickets

#Print Ticket
print(f"=======Movie Ticket ({day})=======")
print("Age            :  ",age)
print("Category       :  ",category)
print("Base Price     : $", price)
print("Discount       : $", discount,"x",tickets)
print("Surcharge      : $", surcharge,"x",tickets)
print("No. of Tickets :  ", tickets)
print("----------------------------")
print("Total Price  : $", Total)





 
