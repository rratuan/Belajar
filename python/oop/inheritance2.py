class Hero:
    def __init__(self,name,healt):
        self.name = name
        self.healt = healt

    def showinfo(self):
        print(f'''Hero Name : {self.name}
Health : {self.healt}''')

class Intellegent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        super().showinfo()

class Magic(Hero):
    def __init__(self, name):
        Hero.__init__(self,name, 200)
        Hero.showinfo(self)

axe = Intellegent('axe')
megumi = Magic('megumi')
