# #Latihan 1
data = [24,56,23,22,90,45]
n = len(data)
print(data)

# Sorting Selection Sort satuan Minimum Accending
def selectionSatuanAccending(data):
    for i in range(n):
        index_min = i
        for j in range(i+1,n):
            if (data[j]%10) < (data[index_min]%10):
                index_min = j
        data[i],data[index_min] = data[index_min],data[i]

selectionSatuanAccending(data)
print('data selection sort minimum accending : ',data)

# Sorting Bubble Sort satuan
def bubbleSatuanAccending(data):
    beres = True
    while beres:
        for i in range(n-1):
            if (data[i]%10) > (data[i+1]%10):
                data[i],data[i+1] = data[i+1],data[i]
        for i in range(n-1):
            if (data[i]%10) > (data[i+1]%10):
                beres = True
                break
            else:
                beres = False

bubbleSatuanAccending(data)
print('data bubble sort accending :',data)


# #Latihan 2
# Selection Sort Maximum Decending satuan
def selectionSatuan(data):
    for i in range(n):
        index_max = i
        for j in range(i+1,n):
            if (data[j]%10) > (data[index_max]%10):
                index_max = j
        data[i],data[index_max] = data[index_max],data[i]

selectionSatuan(data)
print('data selection sort maximum deccending :',data)

# bb sort decending satuan
def bubbleSatuanDeccending(data):
    beres = True
    while beres:
        for i in range(n-1):
            if (data[i]%10) < (data[i+1]%10):
                data[i],data[i+1] = data[i+1],data[i]
        for i in range(n-1):
            if (data[i]%10) < (data[i+1]%10):
                beres = True
                break
            else:
                beres = False

bubbleSatuanDeccending(data)
print('data bubble sort deccending :',data)


