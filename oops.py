# Classes--Template
# Object-- Instance of the class

#  Dry--> Dont Repeat Yourself

# get_no_of_award(Nishu)


class Student:
  pass

Nishu=Student()
Nis=Student()
#print(Nishu, Nis) # both are different object

Nishu.name="Nishu Chauhan"
Nishu.section= "A"
Nis.std= 123
Nis.subjects=["Hindi", "English"]
print(Nishu.section, Nis.std, Nis.subjects)