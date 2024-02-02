listNama = ["Asep Supriatna","Budi Dharma","Cecep Permana","Dede Adi Agung","Ardi Fajar arifin","Ratuayu Nurfajar"]
print(listNama)

def sortingNamaBelakang(listNama):
    n = len(listNama)
    for i in range(n):
        idx_min = i
        for j in range(i+1,n):
            if listNama[j].split()[-1].upper() < listNama[idx_min].split()[-1].upper():
                idx_min = j
        listNama[i],listNama[idx_min] = listNama[idx_min],listNama[i]

sortingNamaBelakang(listNama)
print(listNama)