class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole): #init is a constructor.
        self.name= aname
        self.salary= asalary
        self.role= arole


    def printdetails(self):
        return f"Employee Name is{self.name}.Salary is {self.salary} and Role is {self.role}"

Nishu= Employee("Nishu", 115000, "Developer")   # to given the argument to employee called inststructor.
#these arguments goes to init.
Rishu=Employee(" Rishu", 15000, "Developer")

Nishu.name=" Nishu Chauhan"
Nishu.Sal= 115000
Nishu.Role="Developer"
#
# Rishu.name=" Rishu Singh"
# Rishu.Sal= 15000
# Rishu.Role="SOftware Engineer"

print(Nishu.printdetails())
print(Rishu.printdetails())


print(Nishu.salary)