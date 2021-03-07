class Dad:
    Badmitton=5

class Son(Dad):
    Dance=2
    #Badmitton = 10
    def isdance(self):
        return f"Yes I can dance {self.Dance} anytime."

class GrandSon(Son):
     Dance = 10
     #Badmitton = 15   # 1st search in its own class(Grandson) then Son then  Dad
     def isdance(self):
         return f"Yeah! I can dance {self.Dance} like Madhuri Dixit."


Dada=Dad()
Beta=Son()
Pota=GrandSon()

print(Pota.isdance())
print(Beta.isdance())
print(Pota.Badmitton)
