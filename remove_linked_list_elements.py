# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # to remove linked list nodes, we usually need both a previous and current node pointers
        prev, curr = None, head
        # while we still nodes to go check through
        while curr:
            # if the current node equals the val we need to delete
            if curr.val == val:
                # if the current node is the head of the linked list
                if curr == head:
                    # move the current pointer one forward
                    curr = curr.next
                    # move the head to where the current pointer is
                    head = curr
                # if the current node is not the head node
                else:
                    # we set its previous node pointer to point to current's next element
                    prev.next = curr.next
                    # we shift current only
                    curr = curr.next
            # else no removal required
            else:
                # move on to the next pair of elements
                prev = curr
                curr = curr.next
        # return the head of the updated list
        return head