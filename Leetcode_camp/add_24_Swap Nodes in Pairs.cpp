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
    ListNode* swapPairs(ListNode* head) {
    	// answer1: recursion
        // if (head == NULL || head->next == NULL){
        //     return head;
        // }
        // ListNode *newNext = head->next;
        // head->next = swapPairs(head->next->next);
        // newNext->next = head;
        // return newNext;

    	//answer2: loop
        ListNode *newNext = new ListNode(0);
        newNext->next = head;
        ListNode *ptr = newNext, *swap1, *swap2;
        while(ptr->next!= NULL && ptr->next->next != NULL){
            swap1 = ptr->next, 
            swap2 = ptr->next->next;
            printf("\n%d %d %d",swap1->val, swap2->val, ptr->val);
            swap1->next = swap2->next;
            swap2->next = swap1;
            
            ptr->next = swap2;
            ptr = swap1;
            printf("\n%d %d %d",swap1->val, swap2->val, ptr->val);
        }
        return newNext->next;
        
    }
};