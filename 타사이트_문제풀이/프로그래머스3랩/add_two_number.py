# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.set_list_node(l1, l2, 0)

    def set_list_node(self, l1, l2, val):
        
        add = 0
        l1_n = None
        l2_n = None
        if l1 and l2:
            add = l1.val + l2.val + val
            l1_n = l1.next
            l2_n = l2.next
        elif l1:
            add = l1.val + val
            l1_n = l1.next
        elif l2:
            add = l2.val + val
            l2_n = l2.next
        elif val == 1:
            add = 1
            val = 0
        else:
            return None
            
        if add >= 10:
            add -= 10
            val = 1
        else:
            val = 0
        
        new_list = ListNode(add, self.set_list_node(l1_n, l2_n, val))
        return new_list
        
            