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
    vector<int> inorderTraversal(TreeNode* root) {
        // answer1: use flag and stack to do
        int white = 0, gray = 1;
        vector<int> answer;
        stack<TreeNode *> s;
        s.push(root);
        stack<int> doornot;
        doornot.push(white);

        while(s.empty() != 1){
            int color = doornot.top();
            doornot.pop();
            TreeNode *node = s.top();
            s.pop();
            if(node==NULL)
                continue;
            if(color == white){
                s.push(node->right), doornot.push(white);
                s.push(node), doornot.push(gray);
                s.push(node->left), doornot.push(white);
            }else{
                answer.push_back(node->val);
            }
        }
        return answer;
        
        
        
        
        // answer2: recursion
        // vector<int> answer;
        // inorder(root,answer);
        // return answer;
    }
// private:
//     void inorder(TreeNode *root, vector<int> &node){
//         if(!root){
//             return;
//         }
//         inorder(root->left,node);
//         node.push_back(root->val);
//         inorder(root->right,node);
//     }
};