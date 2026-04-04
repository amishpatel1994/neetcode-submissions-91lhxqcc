class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4 -> 0, 5 -> 1, 0 -> 2, 1 -> 3, 2 -> 4, 3 -> 5
        # formula to get the actual index:
        #   idx - 4 when negative, add len(nums), else return idx - 4
        def _get_idx(offet, idx):
            return (idx + offset) % len(nums)
            # if idx - offset < 0:
            #     return idx - offset + len(nums)
            # else:
            #     return idx - offset
        
        offset = self.min_index(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            idx = _get_idx(offset, m)
            print(m, idx, nums[idx])
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