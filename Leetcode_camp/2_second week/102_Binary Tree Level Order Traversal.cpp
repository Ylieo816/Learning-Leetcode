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
    void traver(vector<vector<int>> &table, TreeNode* node, int level){
        if(node==NULL){
            return;
        }
        if(table.size()<(level+1)){
            table.push_back(vector<int>());
        }
        table[level].push_back(node->val);
        
        traver(table, node->left, level+1);
        traver(table, node->right, level+1);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> answer;
        traver(answer, root,0);
        return answer;
    }
};