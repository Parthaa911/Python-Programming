# Write a Python program to calculate an Electricity Bill based on the number of units consumed.

# 1. For 1–100 units, charge ₹5 per unit.
# 2. For 101–300 units, charge ₹7 per unit.
# 3. For above 300 units, charge ₹10 per unit.
# 4. If the number of units is invalid (0 or negative), display an error message.
# 5. Calculate the total bill amount.
# 6. If the bill amount is greater than ₹2000, add a 5% surcharge.
# 7. Display the units consumed, rate applied, bill amount, surcharge (if applicable), and final total bill.

print("-----------Electricity Bill -------------")
unit=int(input("Enter No. of unit :"))  #Taking no. of units as input
print("Units :",unit)

#Rate
if unit>0 and unit<=100 :
    rate=5
elif unit>100 and unit<=300 :
    rate=7
elif unit>300 :
    rate=10  
else:
    print("Invalid Input")
    exit()
print(f"Rate Applied : {rate} per Unit")

#Calculating bill amount
bill=unit*rate
print("Bill :",bill)


if bill>2000:
     print("5% Surcharge on  Bill Rs  Greater than 2000")
     surcharge=(bill*5)/100
     print("Surcharge :",surcharge)
     total = bill+surcharge
     print("Total Bill :",total)

else:
     print("Total Bill :",bill)