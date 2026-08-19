#alternate array
#Given an array of N integers, write a program to print the elements present at alternate positions, starting from the first element.
def alternate_array(arr):
    arr = list(map(int, arr.split()))
    result = []
    for i in range(0, len(arr)):
        if i%2 == 0:
            result.append(arr[i])
    return result
print(alternate_array(input("Enter the array elements separated by space: ")))
