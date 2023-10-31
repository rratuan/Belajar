print('Soal Nomor 1')
#garis bilangan 1
# -----0+++++5------8+++++11----- (positif = true)

#input user
# bilangan yang diantara 0 dan 5
userInput = int(input('masukkan angka diantara 0 dan 5 : '))

#pengecekan
lebihDari = userInput > 0
kurangDari = userInput < 5

#hasil bilangan yang diantara 0 dan 5
hasil1 = lebihDari and kurangDari

# bilangan yang diantara 8 dan 11
userInput = int(input('masukkan angka diantara 8 dan 11 : '))

# pengecekan 
lebihDari = userInput > 8
kurangDari = userInput < 11

# hasil bilangan yang diantara 8 dan 11
hasil2 = lebihDari and kurangDari

# hasil akhir
hasilAkhir = hasil1 or hasil2
print('jawaban anda adalah',hasilAkhir)

print("=" * 30)

print('Soal Nomor 2')
# garis bilangan 2
# ++++++0------5++++++8------11++++++ (positif = true)

# input user
# bilangan yang kurang dari 0
inputUser = int(input('masukkan angka yang kurang dari 0 : '))

# pengecekan
kurangDari = inputUser < 0

# hasil
hasil1 = kurangDari

# bilangan yang diantara 5 dan 8
inputUser = int(input('masukkan angka yang diantara 5 dan 8 : '))

# pengecekan
lebihDari = inputUser > 5
kurangDari = inputUser < 8

# hasil 
hasil2 = lebihDari and kurangDari

# bilangan yang lebih dari 11
inputUser = int(input('masukkan angka yang lebih besar dari 11 : '))

# pengecekan
lebihDari = inputUser > 11

# hasil
hasil3 = lebihDari

# hasil akhir
hasilAkhir = (hasil1 or hasil2) or hasil3 
print('jawaban anda adalah',hasilAkhir)

