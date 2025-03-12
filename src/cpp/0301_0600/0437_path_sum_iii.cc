#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Solution {
   public:
    int pathSum(TreeNode *root, int targetSum) {
        int res = 0;
        unordered_map<long long, int> cnt{{0, 1}};

        auto dfs = [&](auto &&self, TreeNode *node, long long cur) {
            if (!node) return;
            cur += node->val;

            if (cnt.find(cur - targetSum) != cnt.end())
                res += cnt[cur - targetSum];

            cnt[cur]++;
            self(self, node->left, cur);
            self(self, node->right, cur);
            cnt[cur]--;
        };

        dfs(dfs, root, 0);
        return res;
    }
};

int main() {
    Solution s;
    {
        TreeNode *root = new TreeNode(10);
        root->left = new TreeNode(5);
        root->right = new TreeNode(-3);
        root->left->left = new TreeNode(3);
        root->left->right = new TreeNode(2);
        root->right->right = new TreeNode(11);
        root->left->left->left = new TreeNode(3);
        root->left->left->right = new TreeNode(-2);
        root->left->right->right = new TreeNode(1);
        cout << s.pathSum(root, 8) << endl;  // 3
    }
    {
        TreeNode *root = new TreeNode(5);
        root->left = new TreeNode(4);
        root->right = new TreeNode(8);
        root->left->left = new TreeNode(11);
        root->right->left = new TreeNode(13);
        root->right->right = new TreeNode(4);
        root->left->left->left = new TreeNode(7);
        root->left->left->right = new TreeNode(2);
        root->right->right->left = new TreeNode(5);
        root->right->right->right = new TreeNode(1);
        cout << s.pathSum(root, 22) << endl;  // 3
    }
    return 0;
}
