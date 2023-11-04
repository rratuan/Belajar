print('\n'+' MENU RESTORAN PYTHON '.center(40,'='))
print(f"""Tersedia 3 Pilihan Menu : 
1.Breakfast
2.Lunch
3.Dinner""")

# pelanggan memilih
while True:
    pelanggan = input('Pilih menu yang ingin anda lihat : ')
    if pelanggan == 'breakfast':
        print('ini adalah menu breakfast')
    elif pelanggan == 'lunch':
        print('ini adalah menu lunch')
    elif pelanggan == 'dinner':
        print('ini adalah menu dinner')
    elif pelanggan == 'exit':
        break
    else:
        print('menu tidak tersedia')
        

