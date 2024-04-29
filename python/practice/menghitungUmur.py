import datetime as dt

print(' MENGHITUNG UMUR '.center(30,'='))
# input user
tanggal_lahir = int(input('Masukkan tanggal lahir anda\t: '))
bulan_lahir = int(input('Masukkan bulan lahir anda\t: '))
tahun_lahir = int(input('Masukkan tahun lahir anda\t: '))

# pengecekan
lahir = dt.date(tahun_lahir,bulan_lahir,tanggal_lahir)
print(f'Kamu lahir pada {lahir:%A},{lahir}')

# perhitungan
today = dt.date.today()
thisYear = today.year
selisihHari = today - lahir
umurBulan = (selisihHari.days % 365) // 30
umurTahun = thisYear - tahun_lahir
print(f'Maka sekarang kamu berumur {umurTahun} tahun,{umurBulan} bulan')