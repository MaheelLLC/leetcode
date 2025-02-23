# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Neetcode two pointer solution
        fast = head
        slow = head
        # While fast is not null (the next value of the last node) or
        # while fast isn't pointing to the last node
        # We need both cases since fast moves two nodes at a time

        # Goal of this: find middle of linked list (will be pointed by slow)
        while fast and fast.next:
            # Same as saying fast = fast.next, fast = fast.next
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Check palindrome
        # prev is fortunately pointing at the last node since slow is
        # pointing to the null value after it
        left, right = head, prev
        # The end of the reverse second half is actually null now
        # So we can iterate until the right pointer reaches the end
        # of the second half
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        # Neetcode Array Solution
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        l, r = 0, len(nums) - 1
        # Same as a_list == a_list[::-1] but with two pointers instead
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
        # My attempt
        # Make a copy of linked list that is reversed
        # If reversed linked list equals original list, set true
        # OR we can make two pointers, one at head, one at tail
        # ORRRR we can just add all of the node vals into a single list
        # then, we just reverse the list and test equality to original list
        a_list = []
        while head:
            a_list.append(head.val)
            head = head.next
        # [::-1] returns the list reversed, list.reverse() updates the list while list[::-1]
        # creates a reversed copy
        return a_list == a_list[::-1]

