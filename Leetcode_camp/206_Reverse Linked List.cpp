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
    ListNode* reverseList(ListNode* head) {
        // if (head ==NULL or head->next ==NULL){
        //     return;
        // }
        
        ListNode *newHead = NULL;
        
        while(head != NULL){
            ListNode *newNext = head->next;
            head->next = newHead;
            newHead = head;
            head = newNext;
        }
        return newHead;
    }
};