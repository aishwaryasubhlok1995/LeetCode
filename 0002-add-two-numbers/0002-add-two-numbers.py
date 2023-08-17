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
        carry = 0        
        node = None
        while l1!= None or l2 != None or carry==1:
            digit1 = 0
            digit2 = 0
            if l1 != None:
                digit1 = l1.val
                l1 = l1.next
            if l2 != None:
                digit2 = l2.val
                l2 = l2.next
            val = digit1 + digit2 + carry
            if val > 9:
                val = val - 10  
                carry = 1
            else:  
                carry = 0
            if node == None:
                node = ListNode(val)
                head = node
            else:
                node.next = ListNode(val)
                node = node.next 
        return head
        
            
       
        