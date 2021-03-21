/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL || head->next == NULL){
            return false;
        }
        
        ListNode *fastptr = head->next, *slowptr = head;
        while(fastptr != slowptr){
            if(fastptr == NULL || fastptr->next== NULL){
                return false;
            }
            fastptr = fastptr->next->next;
            slowptr = slowptr->next;
        }
        return true;
    }
};