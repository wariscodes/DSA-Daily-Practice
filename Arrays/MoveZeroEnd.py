# Q. Move the Zero to the end of the array....

# APPROCH 1
arr = [1 , 2 , 0 , 4 , 0 , 5 , 0 , 6]
n = len(arr)
temp = []

for i in range(0 , n):
    if arr[i] != 0:
        temp.append(arr[i])
        
n1 = len(temp)
for i in range(0 , n1):
    arr[i] = temp[i]
    
for i in range(n1 , n):
    arr[i] = 0
    
print(arr)

# Time Complexity = O(n)
# Space Complexity = O(n) but not a optimal 

# APPROCH 2 FOR OPTIMAL SOLUTION
arr = [1 , 2 , 0 , 4 , 0 , 5 , 0 , 6]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        
        j += 1
    
print(arr)

# Time Complexity = O(n)
# Space Complexity = O(1)