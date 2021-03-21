/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // answer 1: use recursion
        if(l1==NULL){
            return l2;
        }else if(l2==NULL){
            return l1;
        }else if(l1->val <= l2->val){
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }else{
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
        
        //answer 2: while
        // ListNode *newNode = new ListNode(0);
        // ListNode *ptr = newNode;
        // while(l1 && l2){
        //     if(l1->val <= l2->val){
        //         ptr->next = l1;
        //         l1 = l1->next;
        //     }else{
        //         ptr->next = l2;
        //         l2 = l2->next;
        //     }
        //     ptr = ptr->next;
        // }
        // if(l1 == NULL){
        //     ptr->next = l2;            
        // }else{
        //     ptr->next = l1;
        // }
        // return newNode->next;
    }
};