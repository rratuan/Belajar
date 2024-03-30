buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500    
}

mahal = 8500
for key in buah:
    if buah[key] >= mahal:
        print(key)
