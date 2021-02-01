# leet 1672. Richest Customer Wealth

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the customer has in the bank.
# Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer
# that has the maximum wealth.

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(customer) for customer in accounts])
