#HealthmanagementSystem
#For 3 Client

#L1 = ["Compiler", "Kali", "Python"]
#L2 = ["1-Diet", "2-Exercise"]
#user_name = int(input("Enter the number for User"))
#print(L1[user_name])

def myfunc():
    def getdate():
        import datetime
        return datetime.datetime.now()

    user_name1= input("Enter user name")
    print("what you want to Enter, Exercise or Diet")
    Diet_exc=int(input("For Diet 1 or for Ecercise 2"))

    if Diet_exc==1:
      user_diet = input("Enter Client Diet")
      print("Diet of " ,user_name1 + "is" , user_diet + "Eaten at " , getdate())
      user_exe = input("Enter Client Exercise")
      print(user_exe)

myfunc()

def getdate():
    import datetime
    return datetime.datetime.now()

#print(getdate())