/*
Problem Statement:
-----------------
Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is 
some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
---------
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
---------
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
---------
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
*/

// Link --> https://leetcode.com/problems/linked-list-cycle/

// Code:
class Solution 
{
public:
    bool hasCycle(ListNode *head) 
    {
        bool answer = false;
        
        if(head == NULL || head->next == NULL)
            return answer;
        
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        while(fast != NULL && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
                
            if(slow == fast)
            {
                answer = true;
                break;
            }
        }
        return answer;
    }
};
