# Q. Find the first Non Reapeting/Unique Character in Given string ????

# APPROCH 1(BRUTE FORCE)
name = "leetcode"
for ch1 in name:
    count = 0
    for ch2 in name:
        if ch1 == ch2:
            count += 1
            
    if count == 1:
        print(name.index(ch1))
        break

# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n)


# APPROCH 2(USING HASING TECHNIQUE(HASH MAP))   
name = "leetcode"
frequency = {}

for ch in name:       # n times
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
        
for key in frequency:  # n times
    if frequency[key] == 1:
        print(name.index(key))
        break
    
# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n)


# LEETCODE SOLUTION - (387. First Unique Character in a String)
# Given a string s, 
#find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        for key in frequency:
            if frequency[key] == 1:
                return s.index(key)
        
        return -1