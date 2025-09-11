#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

long long maximumBeauty(vector<int>& flowers, long long newFlowers, int target,
                        int full, int partial) {
    int n = flowers.size();

    long long left = newFlowers - 1LL * target * n;
    for (int& flower : flowers) {
        flower = min(flower, target);
        left += flower;
    }

    if (left == newFlowers) return 1LL * full * n;

    if (left >= 0) {
        return max(1LL * (target - 1) * partial + 1LL * (n - 1) * full,
                   1LL * n * full);
    }

    sort(flowers.begin(), flowers.end());
    long long res = 0, pre_sum = 0;

    int j = 0;
    for (int i = 1; i <= n; i++) {
        left += target - flowers[i - 1];
        if (left < 0) {
            continue;
        }

        while (j < i && 1LL * flowers[j] * j <= pre_sum + left) {
            pre_sum += flowers[j];
            j++;
        }

        long long avg = (left + pre_sum) / j;
        long long total_beauty = avg * partial + 1LL * (n - i) * full;
        res = max(res, total_beauty);
    }

    return res;
}

int main() {
    vector<int> flowers = {1, 3, 1, 1};
    long long newFlowers = 7;
    int target = 6;
    int full = 12;
    int partial = 1;
    long long res = maximumBeauty(flowers, newFlowers, target, full, partial);
    cout << res << endl;  // 14
    return 0;
}
