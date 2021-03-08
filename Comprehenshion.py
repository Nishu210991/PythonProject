# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)

#------List Comprehensive-----
# ls=[i for i in range(100) if i%3==0]  #list Comprehensions
# print(ls)

#------Dictionary Comprehensive-----
# dict1 ={i:f"item{i}" for i in range (100) if i%5==0}
# dict2 ={i:f"item{i}" for i in range (10)}
# dict2={value:key for key,value in dict2.items()} #for Reversing the valuse of dictionary
# print(dict1, "\n",  dict2)

#------Sets Comprehensive-----
# dresses={dress for dress in ["Dress1","Dress1","Dress1","Dress1","Dress2","Dress2","Dress2"]}
# print(dresses)
# print(type(dresses)) #here using introspection


#------Generators Comprehensive-----
even= (i for i in range (100) if i%2==0) # Generator Compreshensive
#print(type(even))
print(even.__next__())  #can traverse only once
print(even.__next__())
print(even.__next__())

# for item in even:
#     print(item)





