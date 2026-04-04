from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = defaultdict(int)

        for char in s:
            cache[char] += 1

        for char in t:
            cache[char] -= 1

        for count in cache.values():
            if count != 0:
                return False

        return True 