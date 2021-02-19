#f = open("Nishu.txt", "rt")
# content = f.read()
# print(content)

# content = f.read(3)
# print(content)   #Starting 3 charcter (Nis)

# content = f.read(3)
# print(content)   #next 3 charcter (hu )

# for line in f:
#     print(line, end="") #Read code line by line
    # Nishu is a good Girl.She is very beautiful and Intelligent..

# print(f.readline()) #Read only 1 line (Nishu is a good Girl.)
# print(f.readline()) #Read  2nd line   (She is very beautiful and Intelligent..)
# print(f.readlines()) #print list
#['Nishu is a good Girl.\n', 'She is very beautiful and Intelligent..']
#f.close()

# Write in File
# f= open("Nis.txt", "w") #w is only for writing mode.replaced all content while executing.
# f.write("Nishu is an Angel")
# f.close()

#Append in file
#f= open("Nis.txt", "a") #w is only for writing mode.replaced all content while executing.
# f.write("Nishu is an Angel\n")
#a=f.write("Nishu is an Angel\n") # if we want to know how many charcter we inserted.(return value)
#print(a)
#f.close()

#Handle Read and Write Both
# f= open("Nishu.txt", "r+")
# print(f.read())
# f.write("Thanks\n")

# To know the pointer location
# f= open("Nishu.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())

#Reset the file pointer
# f= open("Nishu.txt")
# print(f.readline())
# print(f.seek(0))
# print(f.readline())
# print(f.seek(11))
# print(f.readline())

#Open File with Block(No need to close the file. It includes both open and close.)

with open("Nishu.txt") as f:
    a=f.read(4)
    print(a)  #Nish

