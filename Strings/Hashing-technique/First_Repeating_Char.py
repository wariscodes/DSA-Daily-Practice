# Q. Find the First repeating character in given strig????

# APPROCH 1(BRUTE FORCE)
name = "aabccde"

for ch1 in name:
    count = 0
    
    for ch2 in name:
        if ch1 == ch2:
            count += 1
            
    if count > 1:
        print("First repeating character is :",ch1)
        break 

# TIME COMPLEXITY = O(n ** 2)
# SPACE COMPLEXITY = O(n)

# APPROCH 2 (USING HASING TECHNIQUE(HASH SET)) BECAUSE WE CAN'T FIND FREQUENCY ONLY FIRST REAPTING CHARACTER..
# OPTIMIZED SOLUTION !!
name = "aacbbde"
seen = set()
for ch in name:
    if ch in seen:
        print(ch)
        break
    seen.add("First repeating character is :",ch)

# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n)

# LEETCODE SOLUTION - (2351. First Letter to Appear Twice)
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)