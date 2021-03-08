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

Scorpions_Group= Employee("Scorpions","Group")    #object
Capricorn_Group=Employee("Capricorn", "Group")

print(Scorpions_Group.explain())
print(Scorpions_Group.email)

Scorpions_Group.fname="Aries"
print(Scorpions_Group.email)
Scorpions_Group.email="nishu.chauhan@scorpionsgroup.com"
print(Scorpions_Group.fname)
print(Scorpions_Group.lname)
print(Scorpions_Group.email)

del Scorpions_Group.email
print(Scorpions_Group.email)