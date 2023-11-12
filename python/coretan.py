# title = 'Hari Kemerdekaan Indonesia'
# cekJudul = str(title.istitle())
# print(title,'is title = ',cekJudul)
# print(title.capitalize())

# print('title'.center(30,"-"))

# import datetime as dt
# hari_ini = dt.date.today()
# print(hari_ini)

# listAngka = [0,1,2,3,4,5]

# for angka in listAngka:
#     print(f'ini angka ke-{angka}')

# print('akhir program 1\n')

# for i in range(5):
#     print(f'ini i ke-{i}')

# print('akhir program 2\n')

# data_str = 'ini ibu budi'

# for huruf in data_str:
#     print(huruf)

# print('akhir program 3')

# angka = 0
# print(f'angka awal adalah {angka}\n')

# while angka < 5:
#     angka += 1
#     print('pasti bisa')
#     print(f'angka sekarang adalah {angka}')

# angka = 0

# print(f"angka sekarang -> {angka}")

# while angka < 5:
# 	angka += 1
# 	print(f"angka sekarang -> {angka}") # aksi 1

# 	if angka == 3:
# 		print("nice!")
# 		continue # akan membuat loop meloncat ke step selanjutnya

# 	print("whassup!") # aksi 2

# print("Pinish!")

# data_int = int(input("hitung sampai = "))

# angka = 0

# while True:
# 	angka += 1
# 	print(f"count = {angka}")

# 	if angka == data_int:
# 		print("nice!")
# 		break

# 	print("wassup!")

# print("cukuuup finish!")

data = range(0,10,3) # range(start,stop,step)
dataList = list(data)
print(dataList)

data_for = [i for i in range(0,10)]
print(data_for)

data_for_if = [i for i in range(0,10) if i%2 == 0]
print(data_for_if)

data_pangkat = [i**2 for i in range(0,10)]
print(data_pangkat)

data_pangkat_if = [i**2 for i in range(0,10) if i%2 == 0]
print(data_pangkat_if)

data_hapus = [i for i in range(0,10) if i != 5]
print(data_hapus)

## Operasi

# index   0(-3)  1(-2)  2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi =\n{data}")

# menambah list dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data rubah = \n{data}")

# meremove data

data.remove("Ujang")
print(f"data remove = \n{data}")
# data.remove("usep") akan error karena huruf harus sesuai yaitu "Usep"

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)

list = [1,3,5,7,9]

# for i in range(len(list)):
#     print(i)
#     print(list[i])

