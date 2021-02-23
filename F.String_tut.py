import math
# F String

me = 'Nishu Chauhan'

# a1= "This is %s"%me #Not Relevant, less Readability
# print(a1)

a= 21

# a2= "This is %s %s"%(me, a) #Not Readable(pass tuple)
# print(a2)

# b="This is {} {}"
# a3=b.format(me, a) # Readability Mashup
# print(a3)
# b="This is {1} {0}" #pass indexing parameter
# a3=b.format(me, a) # Readability Mashup
# print(a3)

#F String
"""It is a simple and relevant way to adding a string. It is used for concatenate the long string and insert 
the variable within a string"""

# a4= f"This is {me} {a}"
# print(a4)

# a5= f"This is {me} {a} {4*5} {10+20}"
# print(a5)

# Adding Maths Calculation

# a6= f"This is {me} {a} {math.cos(65)}"
# print(a6)





