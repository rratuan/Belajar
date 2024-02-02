panjangBaris = int(input('baris : '))
panjangKolom = int(input('kolom : '))

array = [[0] * panjangKolom for i in range(panjangBaris)] 

# print(array)

for i in range(panjangBaris):
    for j in range(panjangKolom):
        data = int(input('data = '))
        array[i][j] = data
print(array)