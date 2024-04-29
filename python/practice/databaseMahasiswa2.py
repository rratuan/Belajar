import datetime
import os

mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,11,1)
}

os.system("cls")

print(f"{'SELAMAT DATANG':^30}")
print(f"{'DATA MAHASISWA':^30}")
print('-'*30)

mahasiswa = dict.fromkeys(mahasiswa_template)
mahasiswa['nama']=input('Nama Mahasiswa: ')
mahasiswa['nim']=input('NIM : ')
mahasiswa['sks_lulus']=int(input('SKS Lulus : '))
TAHUN_LAHIR = int(input('Tahun Lahir (yyyy): '))
BULAN_LAHIR = int(input('Bulan Lahir : '))
TANGGAL_LAHIR = int(input('Tanggal Lahir : '))
mahasiswa['lahir']=datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)

