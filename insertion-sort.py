#Insertion Sort
arr=[4,2,1,3,6,5]
 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1] > arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j=j-1
 
insertion_sort(arr)
print(arr)
