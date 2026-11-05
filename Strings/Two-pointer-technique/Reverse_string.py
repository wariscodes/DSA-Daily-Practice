# Q. Reverse the string Problem?

# Approch 1
name = "Programming"
rev = ""

for ch in name:
    rev = ch + rev
    
print(rev)

# Time Complexity = O(n**2) # Every iteration they make a new copy so n**2 time..
# Space Complexity = O(n)


# Approch 2(Obtimized by Two Pointer Technique)
name = "Programming"  # Two pointer + list
s = list(name)

left = 0
right = len(s) - 1

while left < right:
    s[left] , s[right] = s[right] , s[left]
    
    left += 1
    right -= 1
    
result = "".join(s)
print(result)

# Time Complexity = O(n)
# Space Complexity = O(n)