# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        v=[]
        for i in lists:
            x=i
            while x:
                v+=[x.val]
                x=x.next
        v=sorted(v,reverse=True)
        ans=None
        for i in v:
            ans=ListNode(i,ans)
        return ans        