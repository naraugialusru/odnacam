from unittest import TestCase, main
from leet1431 import Solution


class TestSolution(TestCase):
    def test_kids_with_candies(self):
        self.solution = Solution()
        self.assertEqual(self.solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3),
                         [True, True, True, False, True])
        self.assertEqual(self.solution.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1),
                         [True, False, False, False, False])


if __name__ == '__main__':
    main()
