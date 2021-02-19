#Slicing
L = ['red', 'green', 'blue', 'yellow', 'black']
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2][1])
print(L[2][2][1])

L = ['a', 'b', 'c', 'd', 'e', 'f']
print(L[1:-1])

#Function
a=66
b=66
c= sum((a,b)) #sum function should be tuple or list.this is also iterable.Builtin function
print(c)

#user Define Function
def function1(a,b):
    average= (a+b)/2
    print(average)

function1(5,6)

#function store in variable

def function2(a,b):
    """This is a function which is calculating the avreage of two numbers.""" #this is called docstring
    average= (a+b)/2
    #print(average)
    return average

v=function2(5,6)      #for storing a function value in a variable,have to return value.
print(v)
# help(function2) #Same as docstring but its also showing function argument.

# if we dont know that what is excuting in function2 then we use docstring.

print(function2.__doc__)

#try Except Exception
print("Enter no 1")
num1 = input()
print("Enter no 2")
num2 = input()
try:
    print("The value is",
          int(num1)+int(num2))

except Exception as e:
    print(e)

print("This line is very important")




