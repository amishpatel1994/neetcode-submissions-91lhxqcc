class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumeric character and store lower case
        filtered_str = ''
        for char in s:
            if char.isalnum():
                filtered_str += char.lower()


        # one ptr checks from left to right
        # another ptr checks from right to left
        # need to go till midpoint (floor) and check if the values are equal
        for i in range(len(filtered_str)//2):
            if filtered_str[i] != filtered_str[-i-1]:
                return False
        return True