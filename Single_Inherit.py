#Single Inherite

class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole): #init is a constructor.
        self.name= aname
        self.salary= asalary
        self.role= arole


    def printdetails(self):
        return f"Employee Name is{self.name}.Salary is {self.salary} and Role is {self.role}"


    @classmethod
    def change_leave(cls, newleaves):
        cls.no_of_leaves= newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_point(string):
        print("This is a function which prints only this statement." +string)

class programmer(Employee):
    def __init__(self,aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=alanguages
    def prit_pro(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role} and knows {self.language}"
    #pass

Nishu = Employee("Nishu", 115000, "Developer")
Rishu = Employee("Rishu", 15000, "Trainer")

Aana= programmer(" Aana", 25000, "Programmer", ["Python","C"])
Ross= programmer(" Ross", 20000, "Programmer",["Python", "C", "Java"])

print(Aana.prit_pro())
print(Ross.prit_pro())

#print(Aana.print_point("Hey"))
#print(Aana.printdetails())