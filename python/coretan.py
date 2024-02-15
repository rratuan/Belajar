# # # # kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
# # # kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
# # # print("'" + kanan + "'")

# # # kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
# # # print("'" + kiri + "'")

# # # tengah ="tengah".center(20) # rata tengah dengan 20 karakter
# # # print("'" + tengah + "'")

# # # tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
# # # print("'" + tengah + "'")

# # # tes = range(1,12)
# # # print(tes)

# # # i = 6
# # # while i <= 15:
# # #     i = i + 4
# # # print(i)

# # # t = 0
# # # for i in range(1,11):
# # #     if (i % 3) == 3:
# # #         t = t + 1
# # # print(t)

# # # import random

# # # for i in range(1,3):
# # #     print(random.randint(1,5), end=',')

# # # a= input('masukkan a')
# # # b = input('masukkan b')

# # # while b < 28:
# # #     b + b - 2
# # #     a + a + 3
# # # print(b)

# # harga = int(input('harga = '))
# # qty = int(input('qty = '))
# # status = input('status pelanggan = ')

# # diskon = 0
# # if status == 'Y':
# #     diskon = 0.15 * harga
# # else:
# #     diskon = 0.10 * harga
# # subtotal = harga * qty
# # total = subtotal - diskon
# # print(total)


# # print(1%5)
# # print(10/5)

# # t = 0
# # for i in range(1,11):
# #     if t%3 == 3:
# #         t = t + 1
# #     print(t)
# # print(t)

# # import random

# # for i in range(1,3):
# #     print(random.randint(1,5), end=' ')

# # a = input('a = ')
# # b = input('b = ')
# # c = a + b * 2
# # print(c)
# # print(type(c))

# # n = 5
# # for j in range(n-1,0,-1):
# #     print(j)

# # n = 6
# # for i in range(n-1):
# #     print(i)

# # nama_lengkap = "John Michael Doe"

# # # Memisahkan nama lengkap menjadi bagian-bagian dengan spasi sebagai pemisah
# # bagian_nama = nama_lengkap.split()

# # # Mengambil kata terakhir (nama belakang)
# # nama_belakang = bagian_nama[-1]

# # print("Nama Belakang:", nama_belakang)

# # listNama = ["Asep supriatna","Budi Dharma","Cecep Permana","Dede Adi Agung"]
# # n = len(listNama)
# # listNama = [nama.upper() for nama in listNama]
# # print(listNama)

# listFilm = ['An American Crime','The Shawshark Redeption','A Beautifull Mind']
# n = len(listFilm)


# # for i in range(n):
# #     listFilm[i].lower()
# #     print(film)

# # if listFilm[0].split()[0].lower() in ['the','a','an']:
# #     listFilm[0] = listFilm[0].split()[1:]

# # print(listFilm[0])

# # print(''.join(listFilm[0].split()[1:]))
# # print("Swallow".split())
# listFilm = ["An American Crime", "The Shawshank Redemption", "A Beautiful Mind", "Swallow", "The Crown", "American Beauty", "Pacific Rim"]
# print("List Film sebelum diurutkan:")
# print(listFilm)

# def sortingFilm(listFilm):
#     n = len(listFilm)
#     for i in range(n):
#         idx_min = i
#         for j in range(i+1, n):
#             filmSatu = ' '.join(listFilm[j].split()[1:]) if listFilm[j].split()[0].lower() in ['the', 'a', 'an'] else listFilm[j]
#             filmDua = ' '.join(listFilm[idx_min].split()[1:]) if listFilm[idx_min].split()[0].lower() in ['the', 'a', 'an'] else listFilm[idx_min]

#             if filmSatu.lower() < filmDua.lower():
#                 idx_min = j
#         listFilm[i], listFilm[idx_min] = listFilm[idx_min], listFilm[i]

# # Memanggil fungsi untuk mengurutkan listFilm
# sortingFilm(listFilm)

# print("\nList Film setelah diurutkan:")
# print(listFilm)

# tabel data mahasiswa
# data_mahasiswa = [
#     ['Ardi',86,78,80,91],
#     ['Fajar',75,78,81,68],
#     ['Ratu',96,97,90,91],
#     ['Jarot',64,71,80,88],
#     ['Ucup',91,80,83,78],
#     ['Komeng',55,70,68,78],
#     ['Kardun',80,88,67,82],
#     ['Neneng',70,80,89,92]
# ]

# length = len(data_mahasiswa)

# # function sorting
# def sortingData(data,x):
#     for i in range(length):
#         idx = i
#         for j in range(i+1,length):
#             if data[j][x] > data[idx][x]:
#                 idx = j
#         data[i],data[idx] = data[idx],data[i]

# # function total jumlah
# def sumData(data,x):
#     total = 0
#     for i in range(length):
#         total = total + data[i][x]
#     return total

# # function rata rata 
# def average(data,x):
#     average = sumData(data,x)/length
#     return average

# # function median
# def median(data,x):
#     sortingData(data,x)
#     if length % 2 == 1:
#         median = data[int(length/2 + 0.5)][x]
#     else:
#         median = (data[int(length/2 - 1)][x] + data[int(length/2)][x]) / 2
#     return median

# print(median(data_mahasiswa,4))