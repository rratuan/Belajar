# input barang
kodeBarang = input('Kode Barang : ')
jumlahBeli = int(input('Jumlah Beli : '))

# kode barang
if kodeBarang == 'PK01':
    namaBarang = 'Pakaian'
    hargaSatuan = 75000
    hargaTotal = jumlahBeli*hargaSatuan
    totalBayaran = hargaTotal
elif kodeBarang == 'TS02':
    namaBarang = 'Tas'
    hargaSatuan = 65000
    hargaTotal = jumlahBeli*hargaSatuan
    totalBayaran = hargaTotal
elif kodeBarang == 'SP03':
    namaBarang = 'Sepatu'
    hargaSatuan = 157000
    hargaTotal = jumlahBeli*hargaSatuan
    totalBayaran = hargaTotal
elif kodeBarang == 'AK04':
    namaBarang = 'Aksesoris'
    hargaSatuan = 45000
    hargaTotal = jumlahBeli*hargaSatuan
    totalBayaran = hargaTotal
else:
    print('Kode barang yang anda masukkan tidak ditemukan.')

# output tanpa diskon
print(f'Kode Barang : {kodeBarang}')
print(f'Nama Barang : {namaBarang}')
print(f'Jumlah Beli : {jumlahBeli}')
print(f'Harga Satuan : {hargaSatuan}')
print(f'Harga Total : {hargaTotal}')
print(f'Total Bayar : {totalBayaran}')

# output dengan diskon
if jumlahBeli >= 10:
    diskon = input('Ada Diskon [Ya/Tidak] : ')
    if diskon == 'Ya':
        besarDiskon = int(input('Besar Diskon (%) : '))
        potonganDiskon = hargaTotal * (besarDiskon/100)
        print(f'Diskon {besarDiskon} : {potonganDiskon}')
        totalBayaran = hargaTotal - potonganDiskon
        print(f'Total Bayar : {totalBayaran}')
    elif diskon == 'Tidak':
        potonganDiskon = hargaTotal * (0/100)
        print(f'Diskon 0% : {potonganDiskon}')
        totalBayaran = hargaTotal - potonganDiskon
        print(f'Total Bayar : {totalBayaran}')
    else:
        print('tidak ditemukan.')

# input uang bayar
uangBayar = int(input('Bayar : '))

# kembalian
uangKembalian = uangBayar - totalBayaran
print(f'Uang Kembalian : {uangKembalian}')
