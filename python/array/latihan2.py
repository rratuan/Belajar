baris = int(input('baris : '))
kolom = int(input('kolom : '))

data = [0] * baris
print(data)

for i in range(len(data)):
    data[i] = [0] * kolom
print(data)

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(input('data : '))
print(data)