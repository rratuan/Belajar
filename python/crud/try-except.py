# membuat program agar tidak tejadi error pada saat di run

while True:
    pembagi = int(input('masukan angka pembagi : '))
    # jika pembagi tidak sama dengan 0 maka dia akan menampilkan hasil
    # jika pembagi sama dengan 0 maka dia akan error karena undefind
    # tapi dengan adanya try dan expect,ketika 0 masuk ke try dan terjadi error,,,
    # dia akan masuk ke except untuk memberi tahu inputkan selain 0 
    try:
        hasil = 10/pembagi
        print(f'hasil = {hasil}')
        next = input('lanjut [y/n] ? ')
        if next == 'n':
            break
    except:
        print('pembagi tidak boleh sama dengan 0')

print('akhir program 1')
print('-'*30)
# ------------------------------------------------------------------#
try:
    # program ini akan error karena file try.txt belum di buat
    with open('try.txt','r') as file:
        print(file.read())
except:
    # program error otomatis masuk ke except dan akan di buatkan file nya
    print('file tidak ditemukan.membuat file....')
    with open('try.txt','w',encoding="utf-8") as file:
        file.write('file baru')
    # run pertama akan membuat file,dan run yang kedua akan mebaca isi file

print('akhir program 2')
