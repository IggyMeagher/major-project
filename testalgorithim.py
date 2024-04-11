
arr = [1,3,5,5,5,6,1,1]

arr.sort()

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print('found')
    else:
        i = i+1
        print(i)



