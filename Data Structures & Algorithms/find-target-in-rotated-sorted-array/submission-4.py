class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _get_idx(offet, idx):
            return (idx + offset) % len(nums)
        
        offset = self.min_index(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            idx = _get_idx(offset, m)
            if target == nums[idx]:
                return idx
            
            if target < nums[idx]:
                r = m - 1
            else:
                l = m + 1
        
        return -1

    def min_index(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return l