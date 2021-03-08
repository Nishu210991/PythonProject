f1= open("Nishu.txt")
f= open("Nis.txt")

try:
    f2=open("doesnot.txt")
    f = open("Nis.txt")

except Exception as e:
    print(e)  #print exception

else:   #in end or exception command , only 1 comd will run
    print("This will run when excetion is not execute.")

finally:  #this command execute in the end
    print("Finally, Print Anyway")
    f.close()
    f1.close()


print("Important Note")