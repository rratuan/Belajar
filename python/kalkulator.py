print('\n' + ' KALKULATOR SEDERHANA '.center(30,'=') + '\n')
# input angka user
angka1 = float(input('masukkan angka pertama : '))
operator = input('masukkan operator (+,-,x,/) : ')
angka2 = float(input('masukkan angka kedua : '))

#percabangan
if operator == '+':
    print('hasil =',angka1 + angka2)
elif operator == '-':
    print('hasil =',angka1 - angka2)
elif operator == 'x':
    print('hasil =',angka1 * angka2)
elif operator == '/':
    print('hasil =',angka1 / angka2)
else:
    print('inputkan operator yang sesuai!')

# akhir
print('\n' + ' PROGRAM SELESAI '.center(30,'=') + '\n')