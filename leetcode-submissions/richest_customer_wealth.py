class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            total = 0
            for money in customer:
                total += money
            if total > max_wealth:
                max_wealth = total
        return max_wealth