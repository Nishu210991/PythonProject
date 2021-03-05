# numbers=["3","5","4"]
# numbers=list(map(int, numbers))
# for i in range(len(numbers)):
#     numbers[i]= int(numbers[i])
#     print(numbers[i])

# numbers[2]= numbers[2]+1
# print(numbers[2])


# def sq(a):
#     return a*a
#
# num=[2,3,4,5,6,7]
# square=list(map(sq, num))
# print(square)

#Using Lambda Function (one liner code function)
# num=[2,3,4,5,6,7]
# square=list(map(lambda x: x*x, num))
# print(square)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func=[square, cube]
#
# #num=[2,3,4,5,6]
# for i in range(5):
#     val=list(map(lambda x:x(i), func))
#     print(val)

#Using Filter Function
#
# list1=[2,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return  num>5
#
# gr_than_5=list(filter(is_greater_5, list1))
# print(gr_than_5)

#----------------REDUCE------------
from functools import reduce

list1=[2,3,4,5,6]
num= reduce(lambda x,y: x+y, list1)
print(num)

# num=0
# for i in list1:
#     num=num+i
# print(num)  #2+3=5+9=14+6=20

