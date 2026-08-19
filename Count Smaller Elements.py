#Given an array of N integers, for every element determine how many elements in the array are smaller than it. Print the count corresponding to each element.
def count_smaller_elements(arr):
    arr = list(map(int, arr.split()))
    result_count = []
    
    for i in range(len(arr)):
        count = 0
        for j in range(0,len(arr)):
            if arr[i] > arr[j]:
                count += 1
        result_count.append(count)
    return result_count
print(count_smaller_elements(input("Enter the array: ")))