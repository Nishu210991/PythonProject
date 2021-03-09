# a= input("What is your name?")
# b=input("what is your Salary")
#
# # ----Errors Raise before excuting the code
# if int(b)==0:
#     raise ZeroDivisionError("b is 0, no need to run the program")
# if a.isnumeric():
#     raise Exception("Numeric value is not allowed")
#
# print(f"Hello {a}")
c=input("Enter your Name")

try:
    print(a)
    
except Exception as e:
    if c=="Nishu":
        raise ValueError("Already Blocked")
    print("Exception Handled")

