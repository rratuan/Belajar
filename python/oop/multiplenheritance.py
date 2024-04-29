# superclass
class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.setTeam)

# superclass
class Tipe_Hero:
    def setTipe(self,tipe):
        self.setTipe = tipe

    def showTipe(self):
        print(self.setTipe)

# childclass
class Hero(Team,Tipe_Hero):
    def __init__(self,name,healt):
        self.name = name
        self.healt = healt

Tiko = Hero('Tiko',100)
Tiko.setTeam = "Merah Putih"
Tiko.setTipe = "Gelandang"

Tiko.showTeam()
Tiko.showTipe()
print(Tiko.__dict__)