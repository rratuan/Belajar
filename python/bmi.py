# input berat badan
bodyWeight = float(input('masukkan berat badan anda : '))
# input tinggi badan
bodyHeight = float(input('masukkan tinggi badan anda : '))

#konvert cm to meter
bodyHeight = bodyWeight / 100

# perhitungan body mass index
bmi = bodyWeight / bodyHeight**2
print(bmi)

# pengkategorian
if bmi < 18.5:
    print('anda masuk ke dalam kategori berat badan kurang(underweight)')
elif bmi >= 18.5 or bmi <= 24.9:
    print('anda masuk ke dalam kategori berat badan normal')
elif bmi > 24.9 or bmi <= 29.9:
    print('anda masuk ke dalam kategori berat badan berlebih (overweight) ')
elif bmi > 29.9:
    print('anda masuk ke dalam kategori obesitas')
else:
    print('inputkan data yang benar!')

print('terima kasih')