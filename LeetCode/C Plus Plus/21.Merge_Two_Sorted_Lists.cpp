/*
Problem Statemnt:
-----------------
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
---------
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
---------
Input: list1 = [], list2 = []
Output: []
Example 3:
---------
Input: list1 = [], list2 = [0]
Output: [0]
*/

// Link --> https://leetcode.com/problems/merge-two-sorted-lists/

// Code:
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
class Solution 
{
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) 
    {
        ListNode* l1 = list1;
        ListNode* l2 = list2;
        ListNode* list = new ListNode(-1);
        
        ListNode* answerList = list;
        
        while(l1 != NULL && l2 != NULL) 
        {
            if(l1->val < l2->val)
            {
                list->next = l1;
                l1 = l1->next;
            }
            else
            {
                list->next = l2;
                l2 = l2->next;
            }
            list = list->next;
        }
        
        while (l1 != NULL) 
        {
            list->next = l1;
            l1 = l1->next;
            list = list->next;
        }
        
        while (l2 != NULL) 
        {
            list->next = l2;
            l2 = l2->next;
            list = list->next;
        }
        
        return answerList->next;
    }
};
