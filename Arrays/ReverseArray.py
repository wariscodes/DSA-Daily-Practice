# Q. Reverse the given array ?
# Approch 1

arr = [2 , 4 , 9 , 10 , 12]
rev = []

for i in arr:
    rev = [i] + rev

print(rev)
# Time Complexity = O(n**2)
# Space Complexity = O(1)

# Approch 2

arr = [2 , 4 , 6 , 8 , 10]
left = 0
right = len(arr) - 1

while left < right:
    arr[left] , arr[right] = arr[right] , arr[left]
    
    left += 1
    right -= 1
    
print(arr)

# Time Complexity = O(n)
# Space Complexity = O(1)
# Optimization Solution