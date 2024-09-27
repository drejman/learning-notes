"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        input: array of prices on each day
        output: maximum profit possible to achieve
        Brute force: O(n^2) -> check all combinations
        Solution:
            for buying days to consider are the ones with lower price
            that current minimum
            for selling just calculate profit on each day (from current lowest price)
            - start from the first day
            - calculate profit of each day (0 if not possible)
            - if profit is bigger than current max update
            - if price is lower than current lowest update lowest
            time: O(n)
            space: O(1)
        Examples:
            input: [7,1,5,3,6,4]
            iterations:
                initialize: lowest=7, profit=0
                1: price=1, lowest=1, profit=0
                2: price=5, lowest=1, profit=4
                3: price=3, lowest=1, profit=4
                4: price=6, lowest=1, profit=5,
                5: price=4, lowest=1, profit=5
        """
        lowest_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price

            diff = price - lowest_price
            if diff > profit:
                profit = diff
        return profit
