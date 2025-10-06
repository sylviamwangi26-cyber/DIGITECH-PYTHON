#login validation, this program checks on the user inputs and validate it.

print("This program needs the credetials to verify them to give grant access")
print() #create space

#define the username

# username="sylvia"
# password="sylvia1234"

#have an agent to make the code run perfectly
# if  username =="sylvia"and password=="sylvia1234":
#     print("Signin successful")
# else:
#     print("Wrong credentials")

#inputs
username= input("Enter your username: ")
password= input("Enter your password: ")

if username== "sylvia" and password=="sylvia1234":
    print("Signin successful")
elif username !="sylvia" and password=="sylvia1234":
    print("Wrong username")
elif username =="sylvia" and password!= "sylvia1234":
    print("Wrong password")

else:
    print("Wrong credentials")



    
