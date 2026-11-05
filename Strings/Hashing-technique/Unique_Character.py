# Q. Find the Unique Character in give String ??

# Approch 1
name = "Programming"

for ch in name:
    count = 0
    
    for i in name:
        if ch == i:
            count += 1
            
    if count == 1:
        print("Unique character are :",ch)

# Time Complexity = O(n ** 2)
# Space Compleixty = O(1)
# This is not Optimized because we gone every character again and again So we use Hashing Technique...

# Approch 2(Using Hash Map)
name = "Programming"
frequency = {}

for ch in name:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
        
for key in frequency:
    if frequency[key] == 1:
        print("Unique Character are :", key)
        
# Time Complexity = O(n)
# Space Compleixty = O(n)
# OPTIMIZATION SOLUTION........