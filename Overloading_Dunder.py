class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole): #init is a constructor.
        self.name= aname
        self.salary= asalary
        self.role= arole


    def printdetails(self):
        return f"Employee Name is{self.name}.Salary is {self.salary} and Role is {self.role}"


    @classmethod #instances
    def change_leave(cls, newleaves):
        cls.no_of_leaves= newleaves

    def __add__(self, other):  #special add method. called dunder add.its helps to overload operator
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return self.printdetails()


emp1=Employee(" Nishu", 450, "Programmer")
emp2=Employee(" Rishu", 45, "Hairdresser")
print(emp1+emp2) # cant identify throw error
print(emp1/emp2)
print(emp1)  #it calls repr method.but if str method is available give 1st priority to str.
