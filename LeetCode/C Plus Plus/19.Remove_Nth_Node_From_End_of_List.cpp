/*
Problem Statement:
-----------------
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
*/

// Link --> https://leetcode.com/problems/remove-nth-node-from-end-of-list/

// Code:
/**
 * Definition for singly-linked list.
 * struct ListNode 
 * {
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
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        if(head->next == NULL)
            return NULL;
        
        int size = 0;
        ListNode* currentNode = head;
        while(currentNode != NULL)
        {
            currentNode = currentNode->next;
            size++;
        }
        
        if(n == size)
            return head->next;
        
        int indextoDelete = size - n;
        int i = 1;
        ListNode* temporaryNode = head;
        while(i < indextoDelete)
        {
            temporaryNode = temporaryNode->next;
            i++;
        }
        
        temporaryNode->next = temporaryNode->next->next;
        
        return head;
        
    }
};
