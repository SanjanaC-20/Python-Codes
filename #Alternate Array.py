#Alternate Array
#Rearrange positive and negative number in an array
def rearrange_array(arr):
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    for i in range(len(arr)-1):
        if i % 2 == 0 and arr[i] < 0:
            j = i + 1
            while j < len(arr) and arr[j] < 0:
                j += 1

            if j < len(arr):
                arr[i],arr[j] = arr[j], arr[i]

        elif i % 2 == 1 and arr[i] >= 0:
            j = i + 1
            while j < len(arr) and arr[j] >= 0:
                j += 1

            if j < len(arr):
                arr[i],arr[j] = arr[j], arr[i]
    return arr
print(rearrange_array([]))
            