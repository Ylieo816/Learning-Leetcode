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
    vector<int> postorderTraversal(TreeNode* root) {
        int white =0, gray = 1;
        vector<int> answer;
        stack<TreeNode *> s;
        s.push(root);
        stack<int> flag;
        flag.push(white);
        
        while(s.empty() != 1){
            TreeNode *node = s.top();
            s.pop();
            int f = flag.top();
            flag.pop();
            if(node == NULL)
                continue;
            if(f == white){
                s.push(node), flag.push(gray);
                s.push(node->right), flag.push(white);
                s.push(node->left), flag.push(white);
            }else{
                answer.push_back(node->val);
            }
        }
        
        
        // vector<int> answer;
        // postorder(root,answer);
        return answer;
    }
// private: 
//     void postorder(TreeNode *root, vector<int> &node){
//     if(!root){
//         return;
//     }
//     postorder(root->left,node);
//     postorder(root->right,node);
//     node.push_back(root->val);
// }
};