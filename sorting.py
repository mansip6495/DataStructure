def bubble_sort(arr):

    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

    return arr


def selection_sort(arr):
    for i in range(len(arr) -1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if arr[i] > arr[min_index]:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    return arr


def insertion_sort_for(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j=i-1
        flag = 0
        for j in range(i-1,-1,-1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
            else:
                flag = 1
                break
        print(j)
        if flag:
            arr[j+1] = temp
        else:
            arr[j] = temp
        print(arr)
        print("-" * 20)
    return arr


def insertion_sort_while(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j=i-1
        while arr[j] > temp and j>=0:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = temp
    return arr

def merge(left,right,arr):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1


def merge_sort(arr):
    if len(arr)<2:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,arr)

def combine(left, right):
    i = 0
    j = 0
    arr = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j+=1
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr

def merge_sort2(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    if len(left) == 1 and len(right) == 1:
        return [min(left[0],right[0]), max(left[0], right[0])]
    else:
        left = merge_sort2(left[:len(left)//2], left[len(left)//2:])
        right = merge_sort2(right[:len(right)//2], right[len(right)//2:])
    return combine(left, right)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = list()
        right = list()
        for i in range(1,len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        left = quicksort(left)
        right = quicksort(right)
    result = []
    result.extend(left)
    result.append(pivot)
    result.extend(right)
    return result

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90,50]
    # print(quicksort(arr))
    print(merge_sort2(arr[:len(arr)//2], arr[len(arr)//2:]))
    # print(bubble_sort(arr))
    # print(selection_sort(arr))
    # print(insertion_sort_for(arr))
    # print(insertion_sort_while(arr))
    # arr1 = [2,4,1,6]
    # arr2 = [8,5,3,7]
    # merge_sort(arr1)
    # merge_sort(arr2)
    # arr = [0] * (len(arr1)+len(arr2))
    # merge(arr1,arr2,arr)
    #
    # print(arr)