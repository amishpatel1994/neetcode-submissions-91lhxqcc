class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # Use dicitonary to store the nums iterated
         # If the incoming num is in the dictionary, return false
         # Otherwise, add the num to the dictionary
         # Runtime - O(n)
         # Memory - O(n)
        cache = {}
        for num in nums:
            if num in cache:
                return True
            else:
                cache[num] = True
        return False