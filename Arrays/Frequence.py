# Q. Find the Frequence of Single element?

arr = [10, 20, 30, 20, 40, 20, 50]
x = int(input("Enter number :"))
count = 0

for i in arr:
    if i == x:
        count += 1
print(count)

# Time Complexity = O(n) //Optimal for single elements
# Space Complexity = O(1)

# Q. Find the Frequence of Each elements ?

arr = [10, 20, 10, 30, 20, 10]
seen = []
for i in arr:
    if i in seen:
        continue
    
    count = 0
    for j in arr:
        if i == j:
            count += 1
    print(i , ":" , count)
    seen.append(i)
# Time Complexity = O(n**2)
# Space Complexity = O(n)

# Not Optimal Try another Way
    
arr = [10, 20, 10, 30, 20, 10]
frequency = {}

for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
        
for key in frequency:
    print(key , ":" , frequency[key])  
    
# Time Complexity = O(n)
# Space Complexity = O(n)
# Optimal Solution  