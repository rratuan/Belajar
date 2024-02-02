M = int(input('banyak pegawai : '))
N = int(input('banyaknya kriteria : '))

data = [0] * M

for i in range(len(data)):
    data[i] = [0] * (N+2)
print(data)

for i in range(len(data)):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] = str(input('NIP : '))
        elif j == len(data[i])-1:
            for k in range(len(data[i])):
                if k != 0 and k !=len(data[i])-1:
                    data[i][j] += data[i][k]
            data[i][j] /= N
        else:
            data[i][j] = float(input(f'kriteria ke-{j} : '))
print(data)