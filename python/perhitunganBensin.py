import os

os.system("cls")

n = int(input('N : '))
diskon = 0
harga_akhir = 0

print('-'*63)
print(f'| {"Liter":^10} | {"Harga Normal":^15} | {"Diskon":^10} | {"Harga":^15} |')
print('-'*63)

for i in range(1,n+1):
    harga_normal = i * 5000
    
    if i < 5:
        diskon = 0
    elif i%5 == 0:
        diskon = diskon + 4000
    
    harga_akhir = harga_normal - diskon
    
    print(f'| {i:^10} | {harga_normal:^15} | {diskon:^10} | {harga_akhir:^15} |')




