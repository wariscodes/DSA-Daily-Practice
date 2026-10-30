# Q. Find tha Maximum Subarray Sum in Array?

# Approch 1(Brute Force)
arr = [2, -4, 3, 5, -1]
max_arr = arr[0]

for i in range(len(arr)):
    total = 0
    
    for j in range(i , len(arr)):
        total += arr[j]
        
        if total > max_arr:
            max_arr = total

print("Maximum subaaray sum is :",max_arr)
# Time Complexiity = O(n)
# Space Complexity = O(1)


# Approch 2(kadane's Algorithum)
arr = [2, -4, 3, 5, -1]
max_arr = arr[0]
total = 0

for i in range(0 , len(arr)):
    total += arr[i]
    
    max_arr = max(max_arr , total)
    
    if total < 0:
        total = 0
        
print("Maximum subaaray sum is :",max_arr)

# Time Complexiity = O(n)
# Space Complexity = O(1)