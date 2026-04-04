class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = collections.defaultdict(int)

        for num in nums:
            num_frequencies[num] += 1
        

        max_count = 0
        for freq in num_frequencies.values():
            if freq > max_count:
                max_count = freq
        
        bucket = [[] for i in range(max_count)]

        for num, freq in num_frequencies.items():
            bucket[freq-1].append(num)

        tmp = 0
        res = []
        while tmp < k:
            res.append(bucket[-1].pop())
            while bucket and bucket[-1] == []:
                bucket.pop()
            tmp += 1
        
        return res