// leet 1672. Richest Customer Wealth
//
// You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the customer has in the
// bank. Return the wealth that the richest customer has.
//
// A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the
// customer that has the maximum wealth.

#include <vector>

class Solution {
public:
    static int maximumWealth(std::vector<std::vector<int>> &accounts) {
        int maxc{0};
        for (auto &c : accounts) {
            int csum{0};
            for (auto a : c) {
                csum += a;
            }
            if (csum > maxc) {
                maxc = csum;
            }
        }
        return maxc;
    }
};