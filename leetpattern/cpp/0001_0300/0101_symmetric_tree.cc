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
