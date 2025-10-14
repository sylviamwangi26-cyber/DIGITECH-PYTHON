#define a function
# def get_pass(name, age):
#     if age>= 17 :
#         return f"{name},you are not allowed to go in!!"
#     else:
#         return f"{name},you are allowed to go in!!"
    
# #regenerate the name and age
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))

# final = get_pass(user_name, user_age)
# print(final)





def get_access():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        if age<=17:
            return f"{name},you are allowed to go in!!"
        else:
            print(f"{name},you are not allowed to go in!!")
    except ValueError:
        print("weka number usieke maneno")

get_access()