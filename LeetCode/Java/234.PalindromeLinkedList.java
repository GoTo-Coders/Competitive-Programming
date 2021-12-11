/*
Problem Statement:
-----------------
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
---------
Input: head = [1,2,2,1]
Output: true

Example 2:
---------
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
*/

// Link --> https://leetcode.com/problems/palindrome-linked-list/

// Code:
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head)
    {
        if(head == null)
            return null;
        
        ListNode previous = null;
        ListNode current = head;
        
        while(current != null) {
            ListNode next = current.next;
            
            current.next = previous;
            previous = current;
            current = next;
        }
        
        return previous;
    }
    
    public ListNode findHalf(ListNode head){
        ListNode currentHead = head;
        ListNode fastPointer = head;
        
        while(fastPointer.next != null && fastPointer.next.next != null) {
            fastPointer = fastPointer.next.next;
            currentHead = currentHead.next;
        }
        
        return currentHead;
    }
    
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null)
            return true;
        
        ListNode middle = findHalf(head);
        ListNode reverseHead = reverseList(middle.next);
        
        ListNode firstHalfHead = head;
        while(reverseHead != null)
        {
            if(reverseHead.val != firstHalfHead.val)
                return false;
            
            firstHalfHead = firstHalfHead.next;
            reverseHead = reverseHead.next;
        }
        return true;
    }
}
