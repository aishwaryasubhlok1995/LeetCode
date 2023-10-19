def merge_two_lists(l1, l2)
    dummy = ListNode.new
    cur = dummy
    
    while l1 && l2
        if l1.val < l2.val
            cur.next = l1
            l1 = l1.next
        else
            cur.next = l2
            l2 = l2.next
        end
        cur = cur.next
    end
    
    cur.next = l1 || l2
    
    dummy.next
end

