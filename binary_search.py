def binary_search(arr,low,high,x):
    if low<=high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1


def bin_search(arr, x):
    if len(arr) > 1:
        left = 0
        right = len(arr) - 1
        while not left == right:
            mid = (left + right)//2
            print(left, right, mid)
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        if arr[left] == x:
            return left
    elif arr[0] == x:
        return 0
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 40
    result = binary_search(arr,0,len(arr)-1,x)
    result = bin_search(arr, x)
    if result == -1:
        print("Element not found")
    else:
        print("Element found at %d"%(result))
