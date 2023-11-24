print(' Database Buku '.center(40,'='))

list_buku = [] #di assign di luar loop supaya data list yang sudah ada tidak teriset
while True:
    # menginputkan data buku
    judul = input('Judul Buku \t: ')
    penulis = input('Penulis \t: ')

    # menampung data buku ke dalam list
    buku = [judul,penulis]
    # menambahkan list data buku ke dalam list buku buku 
    list_buku.append(buku)
    # print(list_buku)

    # menunjukan data list buku buku berupa tabel
    print('-'*60)
    print('|    No     |        Judul        |         Penulis       |')
    print('-'*60)
    for index,data in enumerate(list_buku):
        print(f'|    {index+1}      |          {data[0]}          |            {data[1]}          |')

    lanjut = input('Mau Lanjut Lagi ? [Y/N] : ').upper()
    if lanjut == 'N':
        break