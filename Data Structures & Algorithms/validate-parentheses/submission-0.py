class Solution:
    def isValid(self, s: str) -> bool:
        paran_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        # keep a stack
        stack = []
        # If you encounter open paran, push to stack
        # If you encounter closing paran
        #   - if stack is empty, return False
        #   - if popped item is not matching paran, return False
        # At the end, return True IFF stack is empty
        for char in s:
            if char in paran_map.keys():
                stack.append(paran_map[char])
            elif char in paran_map.values():
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != char:
                        return False
        
        return len(stack) == 0