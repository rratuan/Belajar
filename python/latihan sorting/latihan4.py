listFilm =  ["An American Crime", "The Shawshank Redeption", "A Beautiful Mind","Swallow", "The Crown", "American Beauty", "Pacific Rim"]
print(listFilm)

def sortingFilm(listFilm):
    n = len(listFilm)
    for i in range(n):
        idx_min = i
        for j in range(i+1,n):
            filmSatu = ' '
            filmDua = ' '
            if listFilm[j].split()[0].lower() in ['the','a','an']:
                filmSatu = ' '.join(listFilm[j].split()[1:])
            else:
                filmSatu = listFilm[j]
            if listFilm[idx_min].split()[0].lower() in ['the','a','an']:
                filmDua = ' '.join(listFilm[idx_min].split()[1:])
            else:
                filmDua = listFilm[idx_min]
            if filmSatu.lower() < filmDua.lower():
                idx_min = j
        listFilm[i],listFilm[idx_min] = listFilm[idx_min],listFilm[i]

sortingFilm(listFilm)
print(listFilm)