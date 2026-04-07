def bubble_sort(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(0, n - i -1):
            if list_a[j] > list_a[j+1]:
                list_a[j] , list_a[j+1] = list_a[j+1] , list_a[j]
    
    return list_a
data = [4,6,2,3,5,9,8,7,1]
print("Bubble Sort:", bubble_sort(data))















































