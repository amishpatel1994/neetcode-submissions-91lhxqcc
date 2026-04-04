class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                return [cache[diff], idx]
            elif num not in cache:
                cache[num] = idx

        return [-1, -1]