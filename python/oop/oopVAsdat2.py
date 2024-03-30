class Segiempat: # nama kelas
    def __init__(self,panjang,lebar): # konstruktor
        self.panjang = panjang # property
        self.lebar = lebar  # property

    # membuat method
    def keliling(self):
        return (2*self.panjang) + (2*self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def view_info(self):
        print(f'Ukuran   : {self.panjang} x {self.lebar}')
        print(f'Keliling : {self.keliling()}')
        print(f'Luas     : {self.luas()} \n')

# instanisasi --> proses pembuatan objek
s1 = Segiempat(10,5) # objek dengan class segiempat
s2 = Segiempat(15,3) # objek dengan class segiempat

s1.view_info()
s2.view_info()
