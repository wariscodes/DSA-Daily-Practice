# Q. Check the Valid Anagram in two given String??

# Approch 1(brute force)
s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)    # If elements are not same so they are not anagram return False and they stop..
else:
    sort_s = sorted(s)   # For sort s time is O(n logn)
    sort_t = sorted(t)   # For sort t time is O(n logn)
    if sort_s == sort_t:
        print(True)
    else:
        print(False)
        
# Total Time Complexity = O(n logn) + O(n logn) = O(2n logn)
# Original Time Complexity = O(n logn) because 2 is contant..
# Space Complexity = O(n) 

# Approch 2 (Frequency check by Hash Map)
s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print(False)    # If elements are not same so they are not anagram return False and they stop..
else:
    frequency = {}
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    
    for ch in t:
        if ch in frequency:
            frequency[ch] -= 1
        else:
            print(False)
            break
    else:
        is_anagram = True
        for values in frequency.values():
            if values != 0:
                is_anagram = False
                break
        print(is_anagram)