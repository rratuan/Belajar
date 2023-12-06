print(' Membaca file txt '.center(30,'-'))

# membuka file
file = open("crud.txt",mode="r") # 'r' mode read

# memeriksa status file bisa dibaca atau tidak
print(f'Status Read : {file.readable()}')
# memeriksa status file bisa dimodif/ditulis atau tidak
print(f'Status Write : {file.writable()}')

# membaca seluruh file
# print(file.read())

# membaca file perbaris
# print(file.readline(),end="") #membaca baris pertama
# print(file.readline(),end="") #membaca baris kedua
#... dan seterusnya

# membaca file perbaris tapi dalam bentuk list
# print(file.readlines())

# mengecek apakah file udah di tutup
print(f'Status close : {file.closed}')
# setiap membuka file open() harus ditutup kembali close()
file.close()
# mengecek apakah file udah di tutup
print(f'Status close : {file.closed}')

# ------------------------------------------------------------#
print(' Membaca file txt dengan "with" '.center(50,'-'))

# tujuan penggunaan 'with' adalah ketika kita buka file kita tidak perlu menutupnya karena otomatis akan ditutup
with open("crud.txt",mode="r") as file:
    content = file.read()
    print(content)
    print(f'Status close : {file.closed}') #false
print(f'Status close : {file.closed}') #true karena sudah keluar dari wilayah 'with'


