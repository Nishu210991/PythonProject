class Employee:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}.{lname}@scorpionsgroup.com"

    def explain(self):
        return f"My Group name is {self.fname} {self.lname}"

    @property  #Decorator-->Avoid to add function after email()..
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@scorpionsgroup.com"

    @email.setter
    def email(self,string):
        print("Changed email")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

NishuSingh=Employee("Nishu", "Singh")
print(NishuSingh.email)
print(type(NishuSingh))  #object Introspection
print(type("This is me"))
print(id(NishuSingh))  #object Introspection
print(id("This is me"))
o="This is me"
print(dir(o))          #show all functions that you can apply on it
print(dir(NishuSingh)) #show all functions that you can apply on it

import inspect
print(inspect.getmembers(NishuSingh))