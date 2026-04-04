class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        # maintain min price seen
        # if there is a lower price encounter, update min price
        # when higher price is encountered, get max profit
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if min_price < price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price
        return max_profit