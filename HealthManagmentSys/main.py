import datetime
def getdate():
    datetime.datetime.now()
    return datetime.datetime.now()

#print(getdate())


def function():

  try:
    L1 = ['1-Annu', '2-Jeet']
    print(L1)
    Client_name = int(input("enter your Client no: "))
    name = (L1[Client_name-1])
    #print(name)


    if name=="1-Annu":
       var=int(input("What do you want to Enter 1-Lock or 2-Retrive: "))

       if var==1:
           lock=int(input("what do you want to lock 1-Diet or 2-Exec:"))
           if lock==1:
              diet=open("Annu_Diet.txt", "a")
              d_txt=input("Enter your Diet")
              diet.write(str(getdate()) +" : "+d_txt +"\n")
              print(name,":", d_txt, ":", getdate(),"Diet successfully entered")
           elif lock==2:
               exe = open("Annu_Exe.txt", "a")
               e_txt = input("Enter your Execise")
               exe.write(str(getdate()) + " : " + e_txt + "\n")
               print(name,":" ,e_txt,":", getdate(), "Excercise successfully entered")

       elif var==2:
            lock_print=int(input("what do you want to print 1-Diet or 2-Exec"))
            if lock_print==1:
                diet_p=open("Annu_Diet.txt", "r")
                print(diet_p.read())

            elif lock_print==2:
                exe_p1=open("Annu_Exe.txt", "r")
                print(exe_p1.read())

    elif name=="2-Jeet":
        var = int(input("What do you want to Enter 1-Lock or 2-Retrive: "))

        if var == 1:
            lock = int(input("what do you want to lock 1-Diet or 2-Exec:"))
            if lock == 1:
                diet = open("Jeet_Diet.txt", "a")
                d_txt = input("Enter your Diet")
                diet.write(str(getdate()) + " : " + d_txt + "\n")
                print(name, ":", d_txt, ":", getdate(), "Diet successfully entered")
            elif lock == 2:
                exe = open("Jeet_Exe.txt", "a")
                e_txt = input("Enter your Execise")
                exe.write(str(getdate()) + " : " + e_txt + "\n")
                print(name, ":", e_txt, ":", getdate(), "Excercise successfully entered")

        elif var == 2:
            lock_print = int(input("what do you want to print 1-Diet or 2-Exec"))
            if lock_print == 1:
                diet_p = open("Jeet_Diet.txt", "r")
                print(diet_p.read())

            elif lock_print == 2:
                exe_p1 = open("Jeet_Exe.txt", "r")
                print(exe_p1.read())


        diet.close()
        exe.close()


  except Exception as e:
    #print(e)
    print("Enter InValid Input")



function()