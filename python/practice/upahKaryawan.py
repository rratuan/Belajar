# inputan jam kerja
jamKerja = int(input(f'masukkan jam kerja anda : '))

# rules
jamNormal = 40
jamLembur = jamKerja - jamNormal
gajiNormal = 2500000
gajiPerJam = gajiNormal / jamNormal

# gaji lembur
gajiLembur = jamLembur * (2 * gajiPerJam)
totalGaji = (gajiPerJam * jamNormal) + gajiLembur

#penggajian
if jamKerja == jamNormal:
    print(f'gaji anda {gajiNormal}')
elif jamKerja > jamNormal:
    print(f'gaji anda {totalGaji} ')
else:
    print(f'gaji anda 0')

print('terima kasih')