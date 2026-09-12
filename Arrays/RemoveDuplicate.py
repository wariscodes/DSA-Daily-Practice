# Q. Remove duplicate in give Array Elements?

# APPROCH 1
arr = [4, 2, 7, 2, 4, 9, 7, 1, 2]
result = []

for i in arr:
    if i not in result:
        result.append(i)
        
print(result)

# Time Complexity = O(n ** 2)
# Space Complexity = O(n)

# APPROCH 2 (Preserve in order way)
arr = [4, 2, 7, 2, 4, 9, 7, 1, 2]
seen = set()
result = []

for i in arr:
    if i not in seen:
        seen.add(i)
        result.append(i)
        
print(result)

# Time Complexity = O(n)
# Space Complexity = O(n)
# OPTMIZED SOLUTION !!

# (Preserve in unorderd way)
arr = [4, 2, 7, 2, 4, 9, 7, 1, 2]
result = list(set(arr))
print(result)