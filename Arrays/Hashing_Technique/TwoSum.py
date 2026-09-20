# Q. Two Sum problem Find two value there addition will be equal to target value?
# APPROCH 1

arr = [2 , 7 , 9 , 8 , 20 , 10 , 6]
target = 16

for i in range(len(arr) - 1):
    for j in range(0 , len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i] , arr[j]) # If we find only index so write print(i , j)
            
# TIME COMPLEXITY = O(n ** 2)
# SPACE COMPLEXITY = O(1)

# APPROCH 2
# Using Hasing(Hash map) technique for optimization !!
arr = [2 , 7 , 9 , 8 , 20 , 10 , 6]
target = 16
seen = {}

for i in range(0 , len(arr)):
    needed = target - arr[i]
    if needed in seen:
        print(needed , arr[i])
    else:
        seen[arr[i]] = i

# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n)
# OPTIMIZATION.....

        
# If we want only one pair and stop so write...
for i in range(0 , len(arr)):
    needed = target - arr[i]
    if needed in seen:
        print(needed , arr[i])
        break
    seen[arr[i]] = i