//
// test_leet1470.cpp
//



#include "../leet1470.cpp"
#include <vector>
#include <iostream>


int main() {
    // test 1
    std::vector<int> nums1{2, 5, 1, 3, 4, 7};
    int n1 = 3;
    std::vector<int> out1{2, 3, 5, 4, 1, 7};

    auto s1 = Solution::shuffle(nums1, n1);

    auto result1 = s1 == out1;

    result1 ? std::cout << "Success!" << std::endl
            : std::cout << "Failure!" << std::endl;

    // test2
    std::vector<int> nums2{1, 2, 3, 4, 4, 3, 2, 1};
    int n2 = 4;
    std::vector<int> out2{1, 4, 2, 3, 3, 2, 4, 1};

    auto s2 = Solution::shuffle(nums2, n2);

    auto result2 = s2 == out2;

    result2 ? std::cout << "Success!" << std::endl
            : std::cout << "Failure!" << std::endl;


    return 0;
}
