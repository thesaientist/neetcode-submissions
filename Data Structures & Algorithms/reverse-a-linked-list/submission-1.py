# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        _prev = head
        _curr = head.next
        _prev.next = None
        while _curr:
            _next = _curr.next
            _curr.next = _prev
            _prev = _curr
            _curr = _next
        return _prev
    
        