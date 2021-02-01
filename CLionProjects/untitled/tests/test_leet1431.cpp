//
// test_leet1431.cpp
//

//#define CONFIG_CATCH_MAIN
//#include "catch.hpp"

//TEST_CASE("Leet test", "[1431]") {
//    std::vector<int> candies{2, 3, 5, 1, 3};
//    std::vector<bool> out{ true, true, true, false, true };
//
//    REQUIRE(Solution::kidsWithCandies(candies, 3) == out);
//}


#include "../leet1431.cpp"
#include <vector>
#include <iostream>


int main() {
    std::vector<int> test_candies{2, 3, 5, 1, 3};
    std::vector<bool> out{true, true, true, false, true};

    auto kwc = Solution::kidsWithCandies(test_candies, 3);

    auto result = kwc == out;

    result ? std::cout << "Success!" << std::endl
           : std::cout << "Failure!" << std::endl;

    return 0;
}
