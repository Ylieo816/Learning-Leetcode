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
    vector<int> preorderTraversal(TreeNode* root) {
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
                s.push(node->left), doornot.push(white);
                s.push(node), doornot.push(gray);
            }else{
                answer.push_back(node->val);
            }
        }
        // vector<int> answer;
        // preorder(root,answer);
        return answer;
    }
// private:
//     void preorder(TreeNode *root,vector<int> &node){
//         if(!root){
//             return;
//         }
//         node.push_back(root->val);
//         preorder(root->left,node);
//         preorder(root->right,node);
//     }
};