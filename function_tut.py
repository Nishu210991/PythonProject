#Lambda function

# minus=lambda x,y: x-y
# #or
# def minus (x,y):
#     return x-y #Replaced these 2 sentences using Lambda
#
# print(minus(10,6))


#Using function
# def a_first(a):
#     return a[1]
#
# a= [[1,4],[8,88],[10,7]]
# a.sort(key=a_first) # take function as input
# print(a)


#Using Lambda Function

# a= [[1,4],[8,88],[2,1]]
# a.sort(key=lambda x:x[1])
# print(a)


#Using Sort() function

# cars=['BMW','VW', 'Fortuner', 'Safari']
# cars.sort()
# cars.sort(reverse=True)
# print(cars)

# def my_func(e):
#     return len(e)
# cars=['BMW','VW', 'Fortuner', 'Safari']
# cars.sort(reverse=True,key=my_func)
# print(cars)
