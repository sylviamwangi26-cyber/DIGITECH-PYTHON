password = " python 1234"
user = input("Enter your password: ")
if user == password:
    print("Access granted")
else:
    print("Access denied")
if user != password:
    print("Access denied, try again later")
    exit()

  
