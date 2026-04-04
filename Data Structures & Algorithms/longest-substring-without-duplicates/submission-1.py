class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        longest_length = 1
        # keep track of start and end of a unique string
        start = 0
        end = 0
        unique_chars = collections.defaultdict(bool)
        # maintain a map of seen characters
        # keep incrementing end until there is a duplicate char
        while end < len(s):
            if unique_chars[s[end]] == False:
                unique_chars[s[end]] = True
                end = end + 1
            else:
                while unique_chars[s[end]]:
                    unique_chars[s[start]] = False
                    start += 1
                
            longest_length = max(end-start, longest_length)
        return longest_length


        # when duplicate, keep updating map and start until duplicate is removed
        # when duplicate is encountered, update longestLength