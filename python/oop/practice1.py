class Hero:
    
    def __init__(self,name,health,attactPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attactPower
        self.armorNumber = armorNumber

    def serang(self,lawan):
        print(f'{self.name} menyerang {lawan.name}')
        lawan.diserang(self,self.attackPower) # self = lawan di parameter diserang

    def diserang(self,lawan,attackPowerLawan):
        print(f'{self.name} diserang {lawan.name}')
        attackDiterima = attackPowerLawan/self.armorNumber
        print(f'Serangan terasa : {attackDiterima}')
        self.health -= attackDiterima
        print(f'Health {self.name} tersisa {str(self.health)}')

sniper = Hero('sniper',100,10,5)
ak4 = Hero('ak4',100,20,10)

sniper.serang(ak4)
ak4.serang(sniper)
