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
    TreeNode* invertTree(TreeNode* root) {
        //answer 1: recursion
//         if(root == NULL or (root->left == NULL && root->right == NULL)){
//             return root;
//         }
        
//         TreeNode *tmp = root->right;
//         root->right = root->left;
//         root->left = tmp;
        
//         invertTree(root->right);
//         invertTree(root->left);
        
//         return root;
        
        //answer 2: while and stack
        if(root == NULL or root->left == NULL && root->right == NULL){
            return root;
        }
        stack<TreeNode*> s;
        s.push(root);
        while(s.empty() != true){
            TreeNode *node = s.top();
            s.pop();
            TreeNode *tmp = node->left;
            node->left = node->right;
            node->right = tmp;
            
            if(node->left != NULL){
                s.push(node->left);
            }
            
            if(node->right != NULL){
                s.push(node->right);
            }
        }
        return root;
    }
};