# Q. FInd the Second Lagrest element in the given array ?

arr = [10 , 20 , 40 , 50 , 90 , 70 , 100]
largest = arr[0]
second_largest = arr[1]

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i

    if i < largest and i > second_largest:
        second_largest = i

print("Second Largest Element is :" , second_largest)

# Time Complexity = O(n)
# Space Complexity = O(1)
# Optimization Solution