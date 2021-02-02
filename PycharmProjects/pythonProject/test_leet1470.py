from unittest import TestCase, main
from leet1470 import Solution


class TestSolution(TestCase):
    def test_kids_with_candies(self):
        self.solution = Solution()
        self.assertEqual(self.solution.shuffle(nums=[2,5,1,3,4,7], n=3),
                         [2,3,5,4,1,7])
        self.assertEqual(self.solution.shuffle(nums=[1,2,3,4,4,3,2,1], n=4),
                         [1,4,2,3,3,2,4,1])
        self.assertEqual(self.solution.shuffle(nums=[1,1,2,2], n=2),
                         [1,2,1,2])

if __name__ == '__main__':
    main()