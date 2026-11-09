# Q. Insertion between of two Arrays?
# Approch 1(Brute Force)

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
result = []

for i in arr1:
    for j in arr2:
        if i == j:
            result.append(i)
print(result)

# Time Complexity = O(n * m) If we use both array has n elements the Time = O(n Square)
# Space Complexity = O(n * m)

# Approch 2(Using Hashing technique(Hash set))
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
set2 = set(arr2)
result = []

for i in arr1:    # First they start a loop in arr1
    if i in set2: # Check index i element present in set2 array
        result.append(i) # Then append same element in result
print(result)

# Time Complexity = O(n + m) If we use both array has n elements the Time = O(n)
# Space Complexity = O(n + m)

# For leetcode solution insertion two array but only unique value store....
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set2 = nums2
        seen = set()
        for i in nums1:
            if i in set2:
                seen.add(i)
        result = list(seen)
        return result
        
