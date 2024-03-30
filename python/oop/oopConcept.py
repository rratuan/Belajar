class Mobil:  # nama class (disarankan menggunakan huruf kapital pada awal nama class)
    jumlah_mobil = 0 # varibel kelas
    # membuat atribut
    def __init__(self, merk, warna): # __init__ = konstruktor untuk si objek 
        self.merk = merk  # atribut class --> merk # varibel instansi
        self.warna = warna  # atribut class --> warna # variabel instansi
        Mobil.jumlah_mobil += 1 # akan bertambah sesuai penambahann objek
        
    # membuat method
    def jalankan(self):  # membuat method berjalan --> supaya mobil bisa berjalan
        print(f'mobil {self.merk} berwarna {self.warna} sedang berjalan')
        
    def berhenti(self):  # membuat method berhenti --> supaya mobil bisa berhenti
        print(f'mobil {self.merk} berwarna {self.warna} sedang berhenti')

# membuat objek = turunan/instansi dari class --> classnya = Mobil (gunakan huruf kapital sesuai dengan konvensi)
mobil1 = Mobil('Toyota', 'Hitam')
print(Mobil.jumlah_mobil) # jumlah = 1
mobil2 = Mobil('BMW', 'Putih')
print(Mobil.jumlah_mobil) # jumlah = 2

mobil1.jalankan()
mobil2.berhenti()

print(mobil1.__dict__)
print(mobil2.__dict__)
