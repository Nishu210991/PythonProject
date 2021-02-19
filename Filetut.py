f = open("Nishu.txt", "rt")
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

f.close()

# Write in File
# f= open("Nis.txt", "w") #w is only for writing mode.replaced all content while executing.
# f.write("Nishu is an Angel")
# f.close()

#Append in file
f= open("Nis.txt", "a") #w is only for writing mode.replaced all content while executing.
f.write("Nishu is an Angel\n")
f.close()