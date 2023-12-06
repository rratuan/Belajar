print(' Membuat,Menulis,Menambah(modify) File '.center(70,'-'))

with open("data1.txt",'w',encoding="utf-8") as file:
    file.write('baris 1\n')
    file.write('baris 2')
    print(f'Status write : {file.writable()}')
    print(f'Status read : {file.readable()}')

# tambahan data dibawah akan overwrite/menimpa data sebelumnya 
with open("data1.txt",'w',encoding="utf-8") as file:
    file.write('baris 3\n')
    file.write('baris 4')

# agar tidak menimba maka menggunakan 'append'
with open("data2.txt",'w',encoding="utf-8") as file:
    file.write('baris 1\n')
    file.write('baris 2\n')
    print(f'Status write : {file.writable()}')
    print(f'Status read : {file.readable()}')

with open("data2.txt",'a',encoding="utf-8") as file:
    file.write('baris 3\n')
    file.write('baris 4')

# ingin melakukan write dan read secara bersamaan menggunakan 'w+'
with open("data3.txt",'w+',encoding="utf-8") as file:
    file.write('baris 1\n')
    file.write('baris 2\n')
    print(f'Status write : {file.writable()}') #true
    print(f'Status read : {file.readable()}') #true
    file.seek(0)
    print(file.read())
    
# ingin write,append,read secara bersamaan menggunakan 'a+'
with open("data3.txt",'a+',encoding="utf-8") as file:
    file.write('baris 3\n')
    file.write('baris 4')
    print(f'Status write : {file.writable()}') #true
    print(f'Status read : {file.readable()}') #true
    file.seek(0)
    print(file.read())

