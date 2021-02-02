# leet 1470. Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        for i in range(n):
            out.append(nums[i])
            out.append(nums[i+n])
        return out