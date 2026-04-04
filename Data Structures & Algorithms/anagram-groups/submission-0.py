class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort and add to dictionary where sorted string is the key
        # and the value is the actual string
        anagram_to_words = collections.defaultdict(list)
        for word in strs:
            anagram = ''.join(sorted(word))
            anagram_to_words[anagram].append(word)
        
        return list(anagram_to_words.values())