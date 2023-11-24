# # kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
# kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
# print("'" + kanan + "'")

# kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
# print("'" + kiri + "'")

# tengah ="tengah".center(20) # rata tengah dengan 20 karakter
# print("'" + tengah + "'")

# tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
# print("'" + tengah + "'")

# tes = range(1,12)
# print(tes)

# i = 6
# while i <= 15:
#     i = i + 4
# print(i)

# t = 0
# for i in range(1,11):
#     if (i % 3) == 3:
#         t = t + 1
# print(t)

# import random

# for i in range(1,3):
#     print(random.randint(1,5), end=',')

# a= input('masukkan a')
# b = input('masukkan b')

# while b < 28:
#     b + b - 2
#     a + a + 3
# print(b)

harga = int(input('harga = '))
qty = int(input('qty = '))
status = input('status pelanggan = ')

diskon = 0
if status == 'Y':
    diskon = 0.15 * harga
else:
    diskon = 0.10 * harga
subtotal = harga * qty
total = subtotal - diskon
print(total)


