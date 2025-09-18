#ifndef TREE_HPP
#define TREE_HPP

#include <iostream>
#include <queue>
#include <vector>

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

class TreeUtils {
   public:
    static TreeNode* buildTree(const vector<int>& values) {
        if (values.empty() || values[0] == -1) return nullptr;

        TreeNode* root = new TreeNode(values[0]);
        queue<TreeNode*> q;
        q.push(root);

        for (size_t i = 1; i < values.size(); i += 2) {
            TreeNode* node = q.front();
            q.pop();

            if (i < values.size() && values[i] != -1) {
                node->left = new TreeNode(values[i]);
                q.push(node->left);
            }

            if (i + 1 < values.size() && values[i + 1] != -1) {
                node->right = new TreeNode(values[i + 1]);
                q.push(node->right);
            }
        }

        return root;
    }

    static vector<int> levelOrder(TreeNode* root) {
        vector<int> result;
        if (!root) return result;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            result.push_back(node->val);

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }

        return result;
    }

    static vector<int> inorder(TreeNode* root) {
        vector<int> result;
        inorderHelper(root, result);
        return result;
    }

    static vector<int> preorder(TreeNode* root) {
        vector<int> result;
        preorderHelper(root, result);
        return result;
    }

    static vector<int> postorder(TreeNode* root) {
        vector<int> result;
        postorderHelper(root, result);
        return result;
    }

    static void printTree(TreeNode* root) {
        auto values = levelOrder(root);
        for (int val : values) {
            cout << val << " ";
        }
        cout << endl;
    }

   private:
    static void inorderHelper(TreeNode* root, vector<int>& result) {
        if (!root) return;
        inorderHelper(root->left, result);
        result.push_back(root->val);
        inorderHelper(root->right, result);
    }

    static void preorderHelper(TreeNode* root, vector<int>& result) {
        if (!root) return;
        result.push_back(root->val);
        preorderHelper(root->left, result);
        preorderHelper(root->right, result);
    }

    static void postorderHelper(TreeNode* root, vector<int>& result) {
        if (!root) return;
        postorderHelper(root->left, result);
        postorderHelper(root->right, result);
        result.push_back(root->val);
    }
};

#endif  // TREE_UTILS_HPP
