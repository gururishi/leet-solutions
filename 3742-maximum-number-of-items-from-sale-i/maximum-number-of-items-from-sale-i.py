class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0] * (budget + 1)
        min_price = min(price for factor, price in items)
        for i in range(n):
            factor, price = items[i]
            count = sum(
                1 for j in range(n)
                if i != j and items[j][0] % factor == 0
            )
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count + 1)
        return max(
            dp[j] + (budget - j) // min_price
            for j in range(budget + 1)
        )