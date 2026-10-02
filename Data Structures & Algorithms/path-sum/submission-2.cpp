/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool pathSum(TreeNode* root, int& path, int targetSum)
    {
        if (!root)
        {
            return false;
        }
        path+=root->val;
        if (path==targetSum && (!root->left && !root->right))
        {
            return true; 
        }
        if (pathSum(root->left, path, targetSum))
        {
            return true; 
        }
        if (pathSum(root->right, path, targetSum))
        {
            return true; 
        }
        path-=root->val; 
        return false; 
    }
    bool hasPathSum(TreeNode* root, int targetSum) 
    {
        int path = 0; 
        if (!root) 
        {
            return false;
        }
        if (pathSum(root, path, targetSum))
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
};