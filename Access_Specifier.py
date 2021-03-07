# Public---For all(Outer)
# Protected--For only that class or drived from the same class(Home)
# Private----For only class(room)

#Single Inherite

class Employee:
    no_of_leaves=8
    var=8         #Access Specifier Public
    _protect=10   #Access Specifier Protected
    __private=15  #Access Specifier Private

    def __init__(self, aname, asalary, arole): #init is a constructor.
        self.name= aname
        self.salary= asalary
        self.role= arole


    def printdetails(self):
        return f"Employee Name is{self.name}.Salary is {self.salary} and Role is {self.role}"


    @classmethod #instances
    def change_leave(cls, newleaves):
        cls.no_of_leaves= newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_point(string):
        print("This is a function which prints only this statement." +string)



emp = Employee("Nishu", 115000, "Developer")

print(emp._protect)
print(emp._Employee__private)

