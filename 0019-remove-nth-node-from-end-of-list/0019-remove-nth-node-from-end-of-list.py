class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        counter = 0
        current = head
        while current != None:
            current = current.next 
            counter = counter + 1
        current=head
        if counter == 1:
            head = None
            return head 
        if counter == n: 
            head = head.next 
            return head
        for i in range(counter-1-n):
            current=current.next
        current.next = current.next.next
        return head