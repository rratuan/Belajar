print(' Database Buku '.center(40,'='))

list_buku = []
while True:
    judul = input('Judul Buku \t: ')
    penulis = input('Penulis \t: ')

    buku = [judul,penulis]
    list_buku.append(buku)
    # print(list_buku)

    print('-'*60)
    print('|    No     |        Judul        |         Penulis       |')
    print('-'*60)
    for index,data in enumerate(list_buku):
        print(f'|    {index+1}      |          {data[0]}          |            {data[1]}          |')

    lanjut = input('Mau Lanjut Lagi ? [Y/N] : ').upper()
    if lanjut == 'N':
        break