# Iterative:- When  a loop excutes until condition becomes false
# Recursion:- Using function within the function called itself.

#Iterative

# def factorial_iterative(n):
#     """
#     :param n: Interger
#     :return: n*n-1*n-2*n-3....1
#     """
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#         #print(fac)
#     return fac
#
# num=int(input("Enter Factorial no"))
# print(factorial_iterative(num))
#
# #Recursion
#
# def factorial_recursion(n):
#     if n==1:
#         return 1
#     elif n>1:
#         return n*factorial_recursion(n-1)
# num=int(input("Enter Factorial no"))
# print(factorial_recursion(num))


# Fabonacci Series
def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


num=int(input("Enter your no"))
if num <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(num):
       print(Fibonacci(i))
#print(Fibonacci(num))