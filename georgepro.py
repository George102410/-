import math


def bubble_sort(arr):
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr)-1):
            if arr[j][3] > arr[j+1][3]:
                a[j],a[j+1] = a[j+1],a[j]

arr = []
with open ('source.txt',encoding='UtF-8') as f:
    for _ in range(102):
        data = f.readline().strip().split('*')
        arr.append(data)

for i in range(1,len(arr)-1):
    a,b = arr[i][2],arr[i][3]
    a = list(map(int,a.split()))
    b = list(map(int,b.split()))
    arr[i].insert(-1,math.sqrt(abs(b[0]-a[0]) + abs(b[1]-a[1])))

print(arr)
print(bubble_sort(arr))