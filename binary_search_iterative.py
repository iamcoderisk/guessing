#author: Prince Darlington

def binary_search_iterative(arr,x):
    low = 0
    high = len(arr)-1
    mid =0
    while low <=high:
        mid = (high+low)//2

        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            low = mid-1

        else:
            return -1

arr = [10,15,25,30,45,67,89,95,105]
key = 15

result = binary_search_iterative(arr,key)

if result !=-1:
    print("element is present at index: ", str(result))
else:
    print("element is not present")