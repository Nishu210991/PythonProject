import os
#print(dir(os)) #dir will tell what methods u can apply on os.

#-----working directory---

#print(os.getcwd()) #getcwd-->current working directory
#os.chdir("C://")
#print(os.getcwd())  #now read the C directory file.
#cant open because it is not present in the c directory.If we remove above chdir function then we can open it .
#f=open("Nishu.txt")

#print(os.listdir()) # show all file's name list which is presnet in this dir.
#print(os.listdir("C://")) #show all C dir file list
#os.mkdir("Test") #make an folder

#os.makedirs("Test/that") #make 2 folders
#os.rename("Test", "Test1")  #Rename the folder name
#print(os.environ.get(('Home')))
#print(os.path.join("C://", "Nishu.txt")) #join path in right way.

#print(os.path.exists("C://")) #it will tell the directory is exists or not.

print(os.path.isfile("Nishu.txt"))

