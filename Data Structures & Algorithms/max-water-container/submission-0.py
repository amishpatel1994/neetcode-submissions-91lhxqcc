class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start with left=0 and right=end
        # keep the greater and update the other one for next iteration
        # keep track of max area
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            curr_area = (right - left) * min(left_height, right_height)
            max_area = max(curr_area, max_area)
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        
        return max_area

