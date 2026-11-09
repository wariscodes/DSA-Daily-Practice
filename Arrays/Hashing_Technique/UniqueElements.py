# Q. Find the Unique elements in Given arrays??

# Using HASING TECHNIQUE(HASH MAP)
arr = [10, 20, 10, 30, 20, 40]
frequency = {}

for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
        
for key in frequency:
    if frequency[key] == 1:
        print("Unique Element :",key)
        
# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n)