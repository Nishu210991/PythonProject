l1=["Chokha", "Aloo", "Baati", "Ice-cream"]

#Noraml Syntax
# i=1
# for item in  l1:
#     if i%2 !=0:
#         print(f"Please Buy it: {item}")
#     i+=1

#Enumerate Function

for index, item in enumerate(l1):
    if index%2==0:
        print(f"Python,Please buy it for me in the evening: {item}")