class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map for storing num_to_freq
        num_to_freq = collections.defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        # create an array with number of keys - default it to empty array
        
        max_count = 0
        for freq in num_to_freq.values():
            if freq > max_count:
                max_count = freq
        buckets = [[] for i in range(max_count)]

        
        # go through num_to_freq and push the num to freq position
        for num, freq in num_to_freq.items():
            buckets[freq-1].append(num) 
        # iterate through the array and append to result if present

        res = []
        for idx in range(len(buckets)-1, -1, -1):
            bucket_nums = buckets[idx]
            if len(bucket_nums) + len(res) >= k:
                elems_to_extract = k - len(res)
                return res + bucket_nums[:elems_to_extract]
            else:
                res += bucket_nums
