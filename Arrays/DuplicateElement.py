# Q. Find the Duplicate elements in given array by DSA Concepts?
# Approch 1
arr = [10, 20, 10, 30, 20, 40]
seen = []

for i in arr:
    if i in seen:
        print("Duplicate :" , i)
    else:
        seen.append(i)

# Time Complexity = O(n**2)
# Space Complexity = O(n)

# Approch 2
arr = [10, 20, 10, 30, 20, 40]

frequency = {}
for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
        
for key in frequency:
    if frequency[key] > 1:
        print("Duplicate Elements :",key)
        
# Time Complexity = O(n)
# Space Complexity = O(n)
# OPTIMIZATION SOLUTION