# Definition for singly-linked list.
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
"""
"""
解题思路:
快慢指针法，由于单链表只能从头到尾依次访问链表的各个结点，因此，如果要找到链表的倒数第N个元素，也只能从头到尾进行遍历查找，在查找的过程中，设置两个指针，让其中一个指针比另一个指针先前移N步，然后两个指针同时在向前移动。循环直到先行的指针值为None时，另一个指针所指的位置就是所要找的位置。

"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        p1=head
        p2=head
        while n:
            p2=p2.next
            n-=1
        if  not p2:
            return head.next
        while p2.next:
            p2=p2.next
            p1=p1.next
        p1.next=p1.next.next
        return head

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
            n = int(line);
            
            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()