data_list = [5,9,3,4,8,2]

# menghitung rata rata

rata_rata = 0
for i in data_list:
    rata_rata += i
rata_rata /= 2
print(rata_rata)

#mencari angka terkecil

data_terkecil = data_list[0]
for i in data_list:
    if i < data_terkecil:
        data_terkecil = i
        print(i)

# mencari angka terbesar

data_terbesar = data_list[0]
for i in data_list:
    if i > data_terbesar:
        data_terbesar = i
        print(i)

# mencari nilai tengah
data_tengah = sorted(data_list)
print(data_tengah)
lenght = 0
for i in data_list:
    lenght += 1
if lenght % 2 == 1:
    print(data_tengah[int(lenght/2 + 0.5 - 1)])
else:
    data_tengah = (data_tengah[int(lenght/2 - 1)] + data_tengah[int(lenght/2)])/2
    print(data_tengah)