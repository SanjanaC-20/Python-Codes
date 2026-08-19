#Building Sunlight
def sunlight(arr):
    arr = list(map(int, arr.split()))
    result = []
    result.append(arr[0])
    count = 1
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            count += 1
            result.append(arr[i])
    return count, result
print(sunlight(input("Enter array: ")))

        