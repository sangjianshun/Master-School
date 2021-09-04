# 25题，难度：难
# 给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
# k是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 给输入listNode加入一个辅助节点，另外反转函数最好传入两个参数，tail和head。

class Solution:
    def reverseKGroupMainProcess(self, head:ListNode):
        tail = head

        head_head = ListNode(0)
        head_head.next = head
        p = head_head.next
        head_head.next = None
        while p.next:
            q = p.next
            p.next = head_head
            head_head = p
            p = q
        p.next = head_head
        tail.next = None
        return tail, p

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        last_batch_tail = None
        while head:
            tail = head
            flag = 0
            for i in range(k-1):
                if tail.next:
                    tail = tail.next  # 该batch中的最后一个节点
                else:
                    flag = 1
            if not last_batch_tail:
                res_head = tail
            if flag == 1:
                last_batch_tail.next = head
                return res_head
            new_head = tail.next
            tail.next = None
            beg_list_node, end_list_node = self.reverseKGroupMainProcess(head)
            if last_batch_tail:
                last_batch_tail.next = end_list_node
            head = new_head
            last_batch_tail = beg_list_node
        return res_head

solution = Solution()
head = ListNode(0)
p = head
for i in range(1, 3):
    p.next =ListNode(i)
    p = p.next


res_head = solution.reverseKGroup(head, 2)
print(1)


