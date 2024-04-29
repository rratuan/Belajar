# variabel protected dan variabel private

class Hero:
    # varibel class
    jumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variabel protected (pake satu underscored) --> bisa di akses dan di ubah
        self._protected = "protected"

        # variabel private (pake dua underscored) --> ga bisa di akses dan ubah
        self.__private = "private"

# variabel protected
lina = Hero("lina",100)
print(lina.__dict__)
print(lina._protected)
lina._protected = "hallo"
print(lina.__dict__)

# variabel private 
# print(lina.__private)
lina.__private = "ubah"  # malah buat atribut baru
print(lina.__dict__)

