#Average of Array
def average_of_array(arr):
    arr = list(map(int , arr.split()))  
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    average = sum / len(arr)
    return f"{average:.2f}"
print(average_of_array(input("Enter the array elements separated by space: ")))