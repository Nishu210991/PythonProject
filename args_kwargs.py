# def function_arg(normal, *args, **kwargs):
#     for item in args:
#         print(item) #Tuple format
#     for key, value in kwargs.items():
#         print(key, value)
#
# name = ["Nishu", "Dikshu" , "Golu", "Dev Pratap"]
#
# normal= "This is meeee....." #normal parameter should be first in the argument.
#
# kw= {"Nishu":"Sweet", "Dikshu":"Cute", "Golu":"Smart"}
#
# function_arg(normal, *name, **kw)

import time

#Time Module(Calculate the Execution time)
initial= time.time()
print(initial)

k=0
while k<5:
    print("Nishu is a innocent girl", time.time()-initial, "Second")
    k+=1

initial2=time.time()
for i in range(5):
    print("Nishu is a sweet girl", time.time()-initial2, "Second")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)


