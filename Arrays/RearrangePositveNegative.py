# Q. Rearrange the Positive and Negatve Elements in array?
#APPROCH 1

arr = [2, -4, 5, -1, 3, -6]
temp1 = []
temp2 = []

for i in arr:
    if i >= 0:
        temp1.append(i)
    else:
        temp2.append(i)

result= temp1 + temp2
print(result)
# Time Complexity = O(n)
# Space Complexity = O(n) 

# APPROCH 2
arr = [2, -4, 5, -1, 3, -6]
j = 0

for i in range(0 , len(arr)):
    if arr[i] >= 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        j += 1
        
print(arr)

# Time Complexity = O(n)
# Space Complexity = O(1)
# Optimization Solution

# If we want Positive element at the front, or negative elements at the back So.
# change arr[i] >=0 to arr[i] <= 0