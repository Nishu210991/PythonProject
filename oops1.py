class Employee:
    no_of_leaves=8
    pass

Nishu= Employee()
Rishu=Employee()

Nishu.name="Nishu Chauhan"
Nishu.Sal= 115000
Nishu.Role="Developer"

Rishu.name="Rishu Chauhan"
Rishu.Sal= 15000
Rishu.Role="SOftware Engineer"
print(Rishu.Sal)
print(Nishu.Sal)

print(Rishu.no_of_leaves) #same for both employee
print(Employee.no_of_leaves)

#Now change leaves for Rishu
print(Rishu.__dict__)
Rishu.no_of_leaves=10  #Create instance variable, Class Variable is accessed by instance
print(Rishu.__dict__)  #Show in Dictionary
print(Employee.__dict__)
Employee.no_of_leaves=15
print(Employee.__dict__)