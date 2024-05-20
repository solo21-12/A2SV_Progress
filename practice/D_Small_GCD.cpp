#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

int solve(std::vector<int>& nums, int n) {
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int gcd = std::__gcd(nums[i], nums[j]);
            cnt += gcd * (n - j - 1);
        }
    }
    return cnt;
}

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;

        std::vector<int> nums(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> nums[i];
        }

        std::sort(nums.begin(), nums.end());

        int ans = solve(nums, n);
        std::cout << ans << std::endl;
    }

    return 0;
}
