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
    def from_str(cls, string):
        # params=string.split("-")
        # print(params)
        # return  cls(params[0], params[1], params[2])
          return cls(*string.split("-")) #alternative method for passing the arguments without using params."Args Used"




Nishu= Employee("Nishu", 115000, "Developer")
Rishu= Employee("Rishu", 15000, "Trainer")
Aana=Employee.from_str("AAna-1500-Student")  #using ssplit function we can pass these argument.

Nishu.change_leave(35)
print(Nishu.no_of_leaves)  # change for both employee's leaves

Rishu.change_leave(34)
#print(Rishu.no_of_leaves)

