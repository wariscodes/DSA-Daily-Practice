# Q. Left rotate array by k ?
# K = 1

# Approch
arr = [2 , 3, 4 ,5 ,6 ,7]
temp = arr[0]

for i in range(0 , len(arr) - 1):
    arr[i] = arr[i + 1]
    
arr[-1] = temp

print(arr)

# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(1)

# k = 2

arr = [2 , 3 ,4 ,5 ,6 ,7]
k = 2

arr = arr[k:] + arr[:k]
print(arr)

# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n) for making ney list