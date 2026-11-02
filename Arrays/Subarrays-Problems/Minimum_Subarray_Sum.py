# Q. Find the minimum Subarray sum in given array?

# Approch 1
arr = [2, -4, 3, 5, -1]
min_arr = arr[0]

for i in range(len(arr)):
    total = 0
    
    for j in range(i , len(arr)):
        total += arr[j]
        
        if total < min_arr:
            min_arr = total
print("Minimum Subarray Sum is :",min_arr)

# Time Complexity: O(n**2)
# Space Complexity: O(1)

# Approch 2
# OPTIMIZED APPROCH(KEDANS ALGORITHUM)
arr = [2, -4, 3, 5, -1]
min_arr = arr[0]
total = 0

for i in range(0 , len(arr)):
    total += arr[i]
    
    min_arr = min(min_arr , total)
    if total > 0:
        total = 0

print("Minimum Subarray Sum is :",min_arr)

# Time Complexity: O(n)
# Space Complexity: O(1)