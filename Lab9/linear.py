def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

mylist = [8, 6, 7, 5, 3, 0, 9]
x = 5
print(linear_search(mylist, x))  
