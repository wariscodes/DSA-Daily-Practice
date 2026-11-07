# Q. Count the Frequecny of given string??

# Approch 1(Brute Force)
name = "Programming"
seen = ""

for ch1 in name:
    if ch1 in seen:
        continue
    count = 0
    for ch2 in name:
        if ch1 == ch2 :
            count += 1
    print(ch1 , ":" , count)
    seen = seen + ch1
    
# Time Complexity = O(n**2)
# Space Complexity = O(n)

# Approch 2 (Using Hasing(Hash Map))
name = "Programming"
frequency = {}

for ch in name:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
        
for key in frequency:
    print(key ,":", frequency[key])
    
# Time Complexity = O(n)
# Space Complexity = O(n)