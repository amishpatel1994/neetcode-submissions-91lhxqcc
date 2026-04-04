class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # left
        # [1,2,8,48]
        # right
        # [48,48,24,6]
        # res
        # [48, 24, 12, 8]
        # compute left products
        left_products = []
        for i in range(len(nums)):
            if i == 0:
                left_products.append(nums[i])
            else:
                left_products.append(nums[i]*left_products[-1])

        right_products = []
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right_products.append(nums[i])
            else:
                right_products.append(nums[i] * right_products[-1])
        right_products = right_products[::-1]

        # compute right products
        # on the edges, just look at the other array
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right_products[1])
            elif i == len(nums) - 1:
                res.append(left_products[-2])
            else:
                res.append(left_products[i-1] * right_products[i+1])
        # for the rest, get product of pos-1 for left and pos+1 of right

        return res