#include <cassert>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
   public:
    void flatten(TreeNode* root) {
        if (!root) return;

        flatten(root->left);
        flatten(root->right);

        TreeNode* left = root->left;
        TreeNode* right = root->right;

        root->left = nullptr;
        root->right = left;

        TreeNode* curr = root;
        while (curr->right) curr = curr->right;
        curr->right = right;
    }
};

int main() {
    Solution sol;
    TreeNode* root =
        new TreeNode(1, new TreeNode(2, new TreeNode(3), new TreeNode(4)),
                     new TreeNode(5, nullptr, new TreeNode(6)));
    sol.flatten(root);

    TreeNode* cur = root;
    std::vector<int> expected = {1, 2, 3, 4, 5, 6};
    for (int val : expected) {
        assert(cur != nullptr && cur->val == val);
        cur = cur->right;
    }
    assert(cur == nullptr);  // End of list

    return 0;
}
