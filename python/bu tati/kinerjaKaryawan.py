# Input jumlah karyawan dan kriteria
M = int(input("Masukkan jumlah karyawan: "))
N = int(input("Masukkan jumlah kriteria: "))

# Input NIP karyawan
NIP = []
for i in range(M):
    nip = input("Masukkan NIP karyawan ke-{}: ".format(i+1))
    NIP.append(nip)

# Input kriteria dan bobot kriteria
kriteria = []
bobot = []
for i in range(N):
    k = input("Masukkan kriteria ke-{}: ".format(i+1))
    b = float(input("Masukkan bobot kriteria {}: ".format(k)))
    kriteria.append(k)
    bobot.append(b)

# Input skor penilaian kinerja karyawan
skor = []
for i in range(M):
    nilai = []
    print("Masukkan skor kinerja karyawan dengan NIP", NIP[i])
    for j in range(N):
        n = float(input("Masukkan skor untuk kriteria {}: ".format(kriteria[j])))
        nilai.append(n)
    skor.append(nilai)

# Hitung nilai akhir
nilai_akhir = []
for i in range(M):
    total = 0
    for j in range(N):
        total += skor[i][j] * (bobot[j] / 100)
    nilai_akhir.append(total)

# Ubah skor menjadi indeks
indeks = []
for i in range(M):
    idx = []
    for j in range(N):
        if skor[i][j] >= 9:
            idx.append('A')
        elif skor[i][j] >= 8:
            idx.append('B')
        elif skor[i][j] >= 7:
            idx.append('C')
        else:
            idx.append('D')
    indeks.append(idx)

# Hitung predikat
predikat = []
for i in range(M):
    if nilai_akhir[i] >= 8.5:
        predikat.append('Baik')
    elif nilai_akhir[i] >= 7:
        predikat.append('Cukup')
    else:
        predikat.append('Kurang')

# Tampilkan nilai akhir dan predikat
print("NIP",end='\t')
for i in range(N):
    print(kriteria[i],end='\t')
print('Nilai Akhir\tPredikat')
for i in range(M):
    print(NIP[i], end='\t')
    for j in range(N):
        print(nilai[j], end='\t')
    print('{:.3f}'.format(nilai_akhir[i]), end='\t\t')
    print(predikat[i])