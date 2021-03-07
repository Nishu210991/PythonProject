#Overriding--If somthing is override it will not be execute..
class A:
    classvar1 = "I am in Class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instace os class A"
        self.special="Special"

class B(A):
    classvar2="I am in Class B"
    classvar1 = "I am in Class B" #Attribute override--

    def __init__(self):      #constructor override
        super().__init__()   #super is used for super class constructor, Attribute, method(like class A)
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instace os class B"
        #super().__init__()  #no use of super because its showing class A values
        print(super().classvar1)

a=A()      #intances of class A
b=B()
print(b.classvar1, b.special, b.classvar1, b.var1)