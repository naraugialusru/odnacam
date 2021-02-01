# leet 1431. Kids With the Greatest Number of Candies

# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the
# ith kid has.

# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
# greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_greatest = max(candies)
        out = list(map(lambda c: c + extraCandies >= current_greatest, candies))
        print(out)
        return out
