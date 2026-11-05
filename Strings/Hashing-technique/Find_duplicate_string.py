# Q. Remove duplicate String ingiven string ??

# Approch 1
name = "Programming"
seen = ""

for ch in name:
    if ch in seen:
        print("Duplicate :" , ch)
        
    else:
        seen = seen + ch

# Time Complixity = O(n **2)
# Space Complexity = O(n)

# Approch 2 
# (Optimized Soloutiom)(Hasing_Technique(Hash-Set))

name = "Programming"
seen = set() #Unique elements store only

for ch in name :
    if ch in seen:
        print("Duplicate :" , ch)
        
    else:
        seen.add(ch)

# Time Complixity = O(n)
# Space Complexity = O(n)
