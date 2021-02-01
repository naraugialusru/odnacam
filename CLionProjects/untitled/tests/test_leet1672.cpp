//
// test_leet1672.cpp
//



#include "../leet1672.cpp"
#include <vector>
#include <iostream>


int main() {
    // test 1
    std::vector<std::vector<int>> accounts1{std::vector<int>{1, 2, 3}, std::vector<int>{3, 2, 1}};
    int out1{6};

    auto mW1 = Solution::maximumWealth(accounts1);

    auto result1 = mW1 == out1;

    result1 ? std::cout << "Success!" << std::endl
            : std::cout << "Failure!" << std::endl;

    // test2
    std::vector<std::vector<int>> accounts2{std::vector<int>{1, 5}, std::vector<int>{7, 3}, std::vector<int>{3, 5}};
    int out2{10};

    auto mW2 = Solution::maximumWealth(accounts2);

    auto result2 = mW2 == out2;

    result2 ? std::cout << "Success!" << std::endl
            : std::cout << "Failure!" << std::endl;


    return 0;
}
