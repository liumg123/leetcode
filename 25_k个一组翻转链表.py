"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
"""
解题思路：
先找到K个一组的最后一个，把这一组链表翻转，把这一组的第一个节点指向这一组之后的节点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self,head):
        count=0
        cur=head
        while cur!=None:
            cur=cur.next
            count+=1
        return count
    #头插法反转链表
    def reverseList(self,head):
        cur=head
        ans=None
        while cur!=None:
            tmp=cur.next
            cur.next=ans
            ans=cur
            cur=tmp
        return ans
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dealEnd=None #dealEnd是需要处理的k个的最后一个， toDeal是待处理的第一个
        toDeal=head
        i=0
        while toDeal !=None and i<k:
            dealEnd=toDeal
            toDeal=toDeal.next
            i+=1
        if i!=k:
            return head
        # 将在处理的K个节点断链，反转这K个节点
        dealEnd.next=None
        ans=self.reverseList(head)
        #此时head是反转后的最后一个节点
        head.next=self.reverseKGroup(toDeal,k)
        return ans

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()