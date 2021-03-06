#Single Inherite

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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_point(string):
        print("This is a function which prints only this statement." +string)



Nishu = Employee("Nishu", 115000, "Developer")  #Object Nishu And Rishu
Rishu = Employee("Rishu", 15000, "Trainer")

class Player:
    no_of_game=4
    def __init__(self, name, game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game}."

class Coolprogrammer(Employee, Player): #values takes acc to order of constructor
    language="C++"
    def printlang(self):
        print(self.language)

Sachin= Player("Sachin",["Cricket"])
Vihaan= Coolprogrammer(" Vihaan", 250000, "CoolProgrammer") #1st given employee dats y passing argumnt acc to employee
detail= Vihaan.printdetails()
print(detail)
Vihaan.printlang()