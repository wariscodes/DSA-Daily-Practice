# Q. Remove duplicate string in given string ??

# APPROCH 1(BRUTE FORCE)
name = "Programming"
seen = ""     # WORST CASE SERCHING(TIME - O(n))
for ch in name:
    if ch not in seen:
        seen = seen + ch
print(seen)

# TIME COMPLEXITY - O(n ** 2)
# SPACE COMPLEXITY - O(n)

# APPROCH 2(HASING(HASH SET))
# OPTIMIZE SOLUTION-

name = "Programming"
seen = set()
result = []

for ch in name:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)
        
result = "".join(result)
print(result)

# TIME COMPLEXITY - O(n)
# SPACE COMPLEXITY - O(n)
