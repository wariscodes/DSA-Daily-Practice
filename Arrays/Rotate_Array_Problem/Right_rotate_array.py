# Q. Right Rotate By k ?

# Approch 1
arr = [2 , 3 , 4, 5, 7 , 8 , 12]
k = 3 # k is anyvalue like 1 , 2, 3

for _ in range(0 , k):
    e = arr.pop()  # blank means op the last value
    arr.insert(0 , e)
    
print(arr)

# Time Complexity = O(k * n)
# Space Complexity = O(1)

# Approch 2
arr = [2 , 3 , 4, 5, 7 , 8 , 12]
k = 3

n = len(arr)
k = k % n  # means Doesn't change tha value

arr.reverse()
arr[:k] = reversed(arr[:k])
arr[k:] = reversed(arr[k:])

print(arr)

# Time Complexity = O(n) Because 3 reverse exist O(n) + O(n) + O(n) = O(3n) and 3 is constant..\
# Space Complexity = O(n)
# Optimized Solution....

# Leetcode Solution (Question - 189)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k % n

#         nums.reverse()
#         nums[:k] = reversed(nums[:k])
#         nums[k:] = reversed(nums[k:])