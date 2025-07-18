#Selection Sort
num_arr =[1,3,5,2,4,6]

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        cur_min_indx = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[cur_min_indx]:
                cur_min_indx = j
                arr[i], arr[cur_min_indx] = arr[cur_min_indx], arr[i]
        
selection_sort(num_arr)
print(num_arr)
