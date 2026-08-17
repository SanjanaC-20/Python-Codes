#DecimaltoBinary Conversion
def sparse_or_not(n):
    arr = []
    while n > 0:
        arr.append(n%2)
        n = n//2
    arr.reverse()
    for i in range(len(arr)):
        print(arr[i])
    for i in range(len(arr)):
        if arr[i] == 1 and arr[i+1] == 1:
            return False
        return True 

n = int(input("Enter the number:"))
print(sparse_or_not(n))