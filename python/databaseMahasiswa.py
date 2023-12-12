import datetime

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim':'10123215',
    'sks_lulus':132,
    'beasiswa':True,
    'lahir':datetime.datetime(2005,6,13)
}

mahasiswa2 = {
    'nama':'Asep Surasep',
    'nim':'10123216',
    'sks_lulus':140,
    'beasiswa':False,
    'lahir':datetime.datetime(2005,2,23)
}

mahasiswa3 = {
    'nama':'Otong Surotong',
    'nim':'10123217',
    'sks_lulus':148,
    'beasiswa':True,
    'lahir':datetime.datetime(2005,1,1)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"| {'KEY':^6} | {'NAMA':^15} | {'NIM':^15} | {'SKS LULUS':^12} | {'BEASISWA':^15} | {'LAHIR':^15} |")
print('-'*97)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"| {KEY:^6} | {NAMA:^15} | {NIM:^15} | {SKS:^12} | {BEASISWA:^15} | {LAHIR:^15} |")
