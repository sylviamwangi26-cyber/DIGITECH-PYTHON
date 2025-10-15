number = int(input("Enter a number: "))
print("You entered:", number)

if number > 100:
    print("The number is greater than 100")
elif number < 100:
    print("The number is less than 100")
else:
    print("The number is equal to 100")
 
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
