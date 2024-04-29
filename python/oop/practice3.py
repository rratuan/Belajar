# encapsulation (getter and setter versi 1)

class Human:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    # method getter
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    # method setter
    def setName(self,value):
        if isinstance(value,str):
            self.__name = value
        else:
            raise ValueError("Name must a string!")
    
    def setAge(self,value):
        self.__age = value

    def birth(self):
        return (2024 - self.__age)
    
print(Human.__dict__)
ratu = Human("Ratu",19)
print(ratu.__dict__)

# mengambil value
# print(ratu.__name) --> error
print(ratu.getName())
print(ratu.getAge())

# mengubah value
# ratu.__name = "Ratu" --> membuat variabel/property baru
print(ratu.__dict__)
ratu.setName("Ratuayu Nurfajar")
print(ratu.__dict__)
# ratu.setName(17)
ratu.setAge(18)
print(ratu.__dict__)
print(ratu.birth())
print(ratu.__dict__)
