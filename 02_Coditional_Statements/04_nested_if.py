#Check username and password and display whether the login is successful or not.

username = "sam"
password = "sam@123"

u_username = input("Enter username :")

if u_username == username :
    u_password = input("Enter Password :")
    if u_password == password:
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")


#Voting eligibility Based on country (nested_if)
country=input("Enter your country name :").lower() #To convert string into lower case
age=int(input("Enter your age :"))

if country == "india":
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")

elif country == "greece":
    if age >= 17:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")

elif country == "argentina":
    if age >= 16:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")
else:
    print("Country not supported")


