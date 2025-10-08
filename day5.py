#we are performing the for loop in our programs

for number in range(10):
    print(number)

for number in range(10):
    if number % 2 == 0:
     print(number)

    # we are performig the while loop in our programs
     
trial = 3
attempt = 0
while attempt < trial:
  value = input (" Enter your password")
  if value == "sylvia1234":
     print("log in successfully")
     break
  else:
     print("the password is wrong try again")
     attempt=1
else:
   print("you failed mumber of attempts are over")
       
