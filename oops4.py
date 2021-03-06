#Static Method..

class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole): #init is a constructor.
        self.name= aname
        self.salary= asalary
        self.role= arole


    def printdetails(self):
        return f"Employee Name is{self.name}.Salary is {self.Sal} and Role is {self.Role}"


    @classmethod
    def change_leave(cls, newleaves):
        cls.no_of_leaves= newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_point(string):
        print("This is a function which prints only this statement." +string)


Nishu= Employee("Nishu", 115000, "Developer")
Rishu= Employee("Rishu", 15000, "Trainer")
Aana=Employee.from_dash("Aana-1500-Student")  #using ssplit function we can pass these argument.

Nishu.change_leave(35)
print(Nishu.no_of_leaves)  # change for both employee's leaves

Rishu.change_leave(34)

Aana.print_point(" This is used for increasing the efficiency.")

