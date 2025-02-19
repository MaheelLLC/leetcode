# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we'll use a stack to store the nodes
        # since a stack is first in, last out, we can easily reverse the order by popping out and changing next
        stack = []
        # while we still have nodes to add to the stack
        while head:
            # add the node to the stack
            stack.append(head.val)
            # go to the next node
            head = head.next
        # let's pop the first node of the stack
        if stack:
            first = ListNode(stack.pop())
            # store the first node to return it later
            head = first
        # now we just pop nodes and set their next equal to the node afterwards
        # while the stack still has nodes to pop
        while stack:
            # grab the next node to pop
            second = ListNode(stack.pop())
            # set the next of the first node to the second node
            first.next = second
            # now make the first node move forward
            first = first.next
        return head
  
"""
the iterative solution requires two pointers. The curr pointer will start at 
the head of the linked list. The prev pointer will start as Null. Store the next
pointer of curr. Then, point curr's next to prev. Shift prev by setting it to curr
shift curr by setting it to stored next. Repeat this process until curr is Null.
prev will equal the new head of the list.
"""  
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # intialize our two pointers
        prev, curr = None, head
        # while the curr pointer is not null
        while curr:
            # store the next pointer of the current node pointer
            nxt = curr.next
            # reverse the current node by flipping its next to previous
            curr.next = prev
            # shift the previous pointer
            prev = curr
            # shift the current pointer
            curr = nxt
            
        return prev
    
    
# NEXT: WORK ON REVERSE LINKED LIST RECURSIVE ON NEETCODE