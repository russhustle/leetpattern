#include <iostream>

#include "include/trees.hpp"

class Solution {
   private:
    bool dfs(TreeNode *Left, TreeNode *Right) {
        if (Left == nullptr && Right == nullptr) return true;
        if (Left == nullptr || Right == nullptr || Left->val != Right->val)
            return false;
        return dfs(Left->left, Right->right) && dfs(Left->right, Right->left);
    }

   public:
    bool isSymmetric(TreeNode *root) {
        return root == nullptr || dfs(root->left, root->right);
    }
};

int main() {
    Solution solution;
    // Test with a symmetric tree
    std::vector<int> values = {1, 2, 2, 3, 4, 4, 3};
    TreeNode *root = TreeUtils::buildTree(values);
    bool result = solution.isSymmetric(root);
    std::cout << "Is symmetric: " << (result ? "true" : "false") << std::endl;
    return 0;
}
