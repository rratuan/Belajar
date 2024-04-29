# tabel data mahasiswa
data_mahasiswa = [
    ['Ardi',86,78,80,91],
    ['Fajar',75,78,81,68],
    ['Ratu',96,97,90,91],
    ['Jarot',64,71,80,88],
    ['Ucup',91,80,83,78],
    ['Komeng',55,70,68,78],
    ['Kardun',80,88,67,82],
    ['Neneng',70,78,89,92]
]

length = len(data_mahasiswa)

# menampilkan tabel data asli
print('-'*91)
print(f'| {"Nama":^15} | {"Matematika":^15} | {"Fisika":^15} | {"Biologi":^15} | {"Informatika":^15} |')
print('-'*91)
for i in range(length):
    print(f'| {data_mahasiswa[i][0]:^15} | {data_mahasiswa[i][1]:^15} | {data_mahasiswa[i][2]:^15} | {data_mahasiswa[i][3]:^15} | {data_mahasiswa[i][4]:^15} |')
print('-'*91)

# function sorting
def sortingData(data,x):
    for i in range(length):
        idx = i
        for j in range(i+1,length):
            if data[j][x] > data[idx][x]:
                idx = j
        data[i],data[idx] = data[idx],data[i]

# function total jumlah
def sumData(data,x):
    total = 0
    for i in range(length):
        total = total + data[i][x]
    return total

# function rata rata 
def average(data,x):
    average = sumData(data,x)/length
    return average

# function median
def median(data,x):
    sortingData(data,x)
    if length % 2 == 1:
        median = data[int(length/2 + 0.5)][x]
    else:
        median = (data[int(length/2 - 1)][x] + data[int(length/2)][x]) / 2
    return median

# function maximum
def maximum(data,x):
    mx = data[0][x]
    for i in range(length):
        if data[i][x] > mx:
            mx = data[i][x]
    return mx

# function minimum
def minimum(data,x):
    mn = data[0][x]
    for i in range(length):
        if data[i][x] < mn:
            mn = data[i][x]
    return mn

# function modus
def modus(data,x):
    maxCount = 0
    maxValue = 0
    for i in range(length):
        count = 0
        for j in range(length):
            if data[i][x] == data[j][x]:
                count += 1
        if count > maxCount:
            maxCount = count
            maxValue = data[i][x]
    if maxCount == 1:
        return 0
    else:
        return maxValue

# table data mahasiswa berdasarkan statistik
data_statistik = [
    ["Banyak Data",length,length,length,length],
    ["Rata Rata",average(data_mahasiswa,1),average(data_mahasiswa,2),average(data_mahasiswa,3),average(data_mahasiswa,4)],
    ["Median",median(data_mahasiswa,1),median(data_mahasiswa,2),median(data_mahasiswa,3),median(data_mahasiswa,4)],
    ["Nilai Max",maximum(data_mahasiswa,1),maximum(data_mahasiswa,2),maximum(data_mahasiswa,3),maximum(data_mahasiswa,4)],
    ["Nilai Min",minimum(data_mahasiswa,1),minimum(data_mahasiswa,2),minimum(data_mahasiswa,3),minimum(data_mahasiswa,4)],
    ["Modus",modus(data_mahasiswa,1),modus(data_mahasiswa,2),modus(data_mahasiswa,3),modus(data_mahasiswa,4)]
]

length2 = len(data_statistik)
print('-'*91)
print(f'| {"Keterangan":^15} | {"Matematika":^15} | {"Fisika":^15} | {"Biologi":^15} | {"Informatika":^15} |')
print('-'*91)
for i in range(length2):
    print(f'| {data_statistik[i][0]:^15} | {data_statistik[i][1]:^15} | {data_statistik[i][2]:^15} | {data_statistik[i][3]:^15} | {data_statistik[i][4]:^15} |')
print('-'*91)
