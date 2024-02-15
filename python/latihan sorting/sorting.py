data = [1,5,4,2,8]
n = len(data)

# bb sort accending versi atu ngecek kiri ke kanan
def bubbleSortAccending(data):
    for i in range(n):
        for j in range(i+1,n-1):
            if data[j+1] < data[j]:
                data[j],data[j+1] = data[j+1],data[j]
        print(i,data)
    
# bb sort accending versi pak andri ngecek kanan ke kiri
def bubbleSorttAccending(data):
    N = len(data)
    ulang = 0
    for i in range(N): # 0 s.d N-1
        for j in range(N-1,i,-1): # N-1 s.d i+1
            if data[j]<data[j-1]: # jika data[j]<data[j-1]
                data[j],data[j-1]=data[j-1],data[j] # tukar isi
        ulang += 1
    return ulang

bubbleSorttAccending(data)
print(data)

# print('data asli :',data)
# bubbleSort(data)
# print('data terurut :',data)

# selection sort minimum accending
def selectionSortAccending(data):
    for i in range(n):
        idx_min = i
        for j in range(i+1,n):
            if data[j] < data[idx_min]:
                idx_min = j
        data[i],data[idx_min] = data[idx_min],data[i]

# selectionSortAccending(data)
# print(data)
                
# bb sort accending versi ardi
def bubbleSortAccending(data):
    beres = True
    while beres:
        for i in range(n-1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
        for i in range(n-1):
            if data[i] > data[i+1]:
                beres = True
                break
            else:
                beres = False

# print(bubbleSort(data))
# print('bubble sort :',data)
                
# selection sort maximum deccending 
def selectionSortDeccending(data):
    for i in range(n):
        index_max = i
        for j in range(i+1,n):
            if data[j] > data[index_max]:
                index_max = j
        data[i],data[index_max] = data[index_max],data[i]

selectionSortDeccending(data)
print('Selection sort maximum deccending :',data)
