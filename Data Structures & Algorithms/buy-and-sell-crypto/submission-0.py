class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_buy = prices[0]

        for price in prices:
            # Update the lowest price found so far
            if price < min_buy:
                min_buy = price
            
            # Calculate profit if we sold today and update max_p
            res = price - min_buy
            if res > max_p:
                max_p = res
                
        return max_p
        