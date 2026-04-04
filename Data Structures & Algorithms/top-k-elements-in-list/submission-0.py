class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = collections.defaultdict(int)

        for num in nums:
            num_frequencies[num] += 1
        

        sorted_freq = sorted(num_frequencies.items(), key=lambda x: x[1], reverse=True)

        return list(map(lambda x: x[0], sorted_freq[:k]))