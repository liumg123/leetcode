"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
"""
解题思路：归并排序的思想
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(None)
        Node=res
        while l1 and l2:
            if l1.val<l2.val:
                Node.next,l1=l1,l1.next
            else:
                Node.next,l2=l2,l2.next
            Node=Node.next
        if l1:
            Node.next=l1
        if l2:
            Node.next=l2
        return res.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length=len(lists)
        if length==0:
            return None
        if length==1:
            return lists[0]
        if length==2:
            return self.mergeTwoLists(lists[0],lists[1])
        mid=length//2
        leftLists=self.mergeKLists(lists[:mid])
        rightLists=self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(leftLists,rightLists)
        
        
        