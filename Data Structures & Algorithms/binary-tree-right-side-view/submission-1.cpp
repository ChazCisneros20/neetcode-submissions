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
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> res; 
        std::queue<TreeNode*> myQueue; 
        if (root==NULL)
        {
            return res;
        }
        else
        {
            myQueue.push(root);
        }
        
        while (myQueue.size() > 0)
        {
            int temp_size = myQueue.size();
            for (int i=0; i < temp_size; i++)
            {
                TreeNode* root = myQueue.front(); // C++ doesn't return with a pop(). so do front() THEN pop()
                myQueue.pop(); 
                if (i==temp_size-1)
                {
                    res.push_back(root->val);
                }
                if (root->left)
                {
                    myQueue.push(root->left);
                }
                if (root->right)
                {
                    myQueue.push(root->right);
                }
            }
        }
        return res;
    }
};
