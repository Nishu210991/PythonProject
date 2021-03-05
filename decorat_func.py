# def function():
#     print("Hey Designer!")
#
# func2=function
#
# del function #before deleting this function, function already copied in func2
# func2()


# def function(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=function(0) # if we are passing 0 return <built-in function print>
# print(a)

# def executor(func):
#     func("Hello")
#
# executor(print)  #we can use the function within a function, cant use sum bcz it takes integer value

def dec1(func1):
    def nowexe():
        print("Good to See you")
        func1()
        print("Great!You are a good Developer.")
    return nowexe
@dec1
def who_is_nishu():
    print("Nishu Chauhan")
#who_is_nishu()

#who_is_nishu =dec1(who_is_nishu)  # can b replaced by @dec1 (short form of decorators)

who_is_nishu()