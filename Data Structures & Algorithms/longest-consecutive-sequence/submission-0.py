class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force approach - convert to sorted set and check for longest sequence O(nlogn)

        # Convert the array into a map (num_presence) - O(n)
        num_presence = {}

        # keep a running longest_consecutive tally
        longest_consecutive = 0

        for num in nums:
            num_presence[num] = True
        
        # Identify the start of a sequence (if n-1 does not exist) - O(n)
        seq_starters = []
        for num in nums:
            if num - 1 not in num_presence:
                seq_starters.append(num)
        
        # When start of sequence is identified, check for sequence length
        for starter in seq_starters:
            tmp_counter = 1
            tmp_num = starter + 1
            while tmp_num in num_presence:
                tmp_num += 1
                tmp_counter += 1
            longest_consecutive = max(tmp_counter, longest_consecutive)

        return longest_consecutive
