class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # generate a two index map where key is the total and value is list of index pairs
        two_idx_map = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_idx_map[nums[i]+nums[j]].append([i,j])

        # Iterate through nums and check if there are indexes using the map where sum is 0
        for i in range(len(nums)):
            if -nums[i] in two_idx_map:
                potential_idxs = two_idx_map[-nums[i]]
                for idxs in potential_idxs:
                    if i not in idxs:
                        tmp_res = [nums[idxs[0]], nums[i], nums[idxs[1]]]
                        tmp_res.sort()
                        res.append((tmp_res[0], tmp_res[1], tmp_res[2]))
        return list(set(res))

        
