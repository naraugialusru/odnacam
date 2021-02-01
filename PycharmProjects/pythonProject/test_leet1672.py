from unittest import TestCase, main

from leet1672 import Solution


class TestSolution(TestCase):
    def test_maximumWealth(self):
        self.solution = Solution()
        self.assertEqual(self.solution.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]), 6)
        self.assertEqual(self.solution.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]), 10)


if __name__ == '__main__':
    main()
