#include <algorithm>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

int diameterOfBinaryTree(TreeNode* root) {
    int diameter = 0;

    auto dfs = [&](auto&& self, TreeNode* node) -> int {
        if (!node) return 0;
        int left = self(self, node->left);
        int right = self(self, node->right);

        diameter = max(diameter, left + right);

        return 1 + max(left, right);
    };

    dfs(dfs, root);
    return diameter;
}

int main() {
    // [1, 2, 3, 4, 5]
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    cout << diameterOfBinaryTree(root) << endl;  // 3

    return 0;
}
