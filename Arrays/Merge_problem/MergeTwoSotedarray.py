# Q Merge the Two sorted array in single array?

# SIMPLE APPROCH
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
result = arr1 + arr2
result.sort() # sort() is a built-in function or method in list that arrange in ascending order !!
print(result)

# Time = O(n)
# Space = O(1)

# Optimized Approch(Using TWO POINTER TECHNIQUE)
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
i = 0
j = 0
result = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1
        
while i < len(arr1):
    result.append(arr1[i])
    i += 1
    
while j < len(arr2):
    result.append(arr2[j])
    j += 1
    
print(result)

# Time Complexity = O(n + m) because arr1 length is n and arr2 length is m.
# Space Complexity = O(n + m)