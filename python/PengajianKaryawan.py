#PenggajianKaryawan
#I.S. : pengguna memasukkan bulan, tahun, tiga buah NIK, tiga buah nama
#       karyawan dan tiga buah gaji pokok
#F.S. : menampilkan pajak, tunjangan dan gaji bersih per karyawan beserta
#       total gaji


#memasukkan bulan dan tahun penggajian
Bulan = str (input('Bulan : '))
Tahun = str (input('Tahun : '))

#memasukkan NIK, nama karyawan dan gaji pokok sebanyak 3 karyawan
print (' Nama Karyawan ke>>')
print ('--------------------' )
print ('<< Data Karyawan ke-1>>')
NIK1         = str(input('NIK : '))
Nama1        = str(input('Nama Karyawan  :'))
GajiPokok1   = int(input('Gaji Pokok     : Rp.'))


print('<< Data Karyawan ke-2>>')
NIK2        = str(input('NIK : '))
Nama2       = str(input('Nama Karyawan  :'))
GajiPokok2  = int(input('Gaji Pokok     : Rp.'))


#menghitung pajak 3 karyawan
Tunjangan1 = 0.1 * GajiPokok1
Tunjangan2 = 0.1 * GajiPokok2
Tunjangan3 = 0.1 * GajiPokok3

#menghitung tunjangan 3 karyawan
Tunjangan1 = 0.2 * GajiPokok1
Tunjangan2 = 0.2 * GajiPokok2
Tunjangan3 = 0.2 * GajiPokok3

#menghitung tunjangan 3 karyawan
GajiBersih1 = GajiPokok1 + Tunjangan1 - Pajak1
GajiBersih2 = Gajipokok2 + Tunjangan2 - Pajak2
GajiBersih3 = GajiPokok3 + Tunjangan3 - Pajak3

#menghitung total gaji
TotalGaji = GajiBersih1 + GajiBersih2 + GajiBersih3

#menampilkan laporan penggajian
os.system ('cls')
print ('Laporan Penggajian')
print ('------------------')
print (f'Bulan/Tahun  {Bulan}/{Tahun}')
print ('--------------------------------------------------------------------------------------------------')
print ('|    NIK    |   Nama Karyawan  |     Gaji Pokok    |    Tunjangan   |   Pajak   |  Gajih Bersih  |')
print ('--------------------------------------------------------------------------------------------------')
print (f'| {NIK1:9} | {Nama1:13} | Rp. {GajiPokok1:8} | Rp. {Tunjangan1:8.1f} |{Pajak1:8.1f} | {GajiBersih1:9.1f}')
print (f'| {NIK2:9} | {Nama1:13} | Rp. {GajiPokok1:8} | Rp. {Tunjangan1:8.1f} |{Pajak1:8.1f} | {GajiBersih1:9.1f}')
print (f'| {NIK3:9} | {Nama1:13} | Rp. {GajiPokok1:8} | Rp. {Tunjangan1:8.1f} |{Pajak1:8.1f} | {GajiBersih1:9.1f}')
print ('--------------------------------------------------------------------------------------------------------=')
print('Total Gaji : Rp. {TotalGji:10.1f}')

