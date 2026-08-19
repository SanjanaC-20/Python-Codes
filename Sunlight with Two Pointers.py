#A building is said to receive sunlight if there is no building taller than it between the beginning of the array and its current position.
def building_with_sunlight(arr):

    arr = list(map(int, arr.split()))

    count = 0
    left = 0

    while left < len(arr):

        right = 0
        sunlight = True

        while right < left:

            if arr[right] > arr[left]:
                sunlight = False
                break

            right += 1

        if sunlight:
            count += 1

        left += 1

    return count


print(building_with_sunlight(input("Enter the array elements separated by space: ")))
