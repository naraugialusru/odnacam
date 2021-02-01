// 1431. Kids With the Greatest Number of Candies
//
// Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the
// ith kid has.
//
//For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
//greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
//

#include <vector>

class Solution {
public:
    static std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        int current_greatest = *std::max_element(candies.begin(), candies.end());
        std::vector<bool> out;
        for (auto k: candies) {
            (k + extraCandies >= current_greatest) ?
            out.push_back(true) : out.push_back(false);
        }
        return out;
    }
};