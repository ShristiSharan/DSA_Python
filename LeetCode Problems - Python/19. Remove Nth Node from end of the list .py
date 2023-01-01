# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        """
        pre = head
        slow = head
        fast = head
        # Make sure fast pointer is n nodes ahead of slow pointer.
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            pre = pre.next if slow != head else pre
            slow = slow.next
        if slow == head and fast == head:
            pre = None
        elif slow == head:
            head = pre.next
        else:
            pre.next = slow.next
        return head

# *********************************************************************************************************
#  the first approach misses one edge case, won't getting it .............................................
# *********************************************************************************************************

#          if (head.next==None):   # ~~~~ here edge case is a single node linked list ~~~~
#             return None
        
#         size=0                  # finding out the size
#         currNode=head
#         while(currNode is not None):
#             currNode = currNode.next
#             size+=1
#         size=size-n
#         if size==0:
#             currNode=head.next
#             head.next=None
#             del head
#             return currNode

#         if(n==size):
#             return head.next
        
#         if head.next.next == None:
#             del head.next
#             return head

#         curr=head
#         prev=None
#         while(size>0):
#             prev=curr
#             curr=curr.next
#             size-=1

#         prev.next=curr.next
#         curr.next=None
#         del curr
#         return head
       

 



























