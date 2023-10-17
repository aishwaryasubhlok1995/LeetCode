def merge_two_lists(l1, l2)
    previoushead = ListNode.new(-1)

    previous = previoushead

    while l1 && l2
        if l1.val<=l2.val
            previous.next = l1
            l1 = l1.next
        else
            previous.next = l2
            l2 = l2.next
        end
        previous = previous.next
    end
    previous.next = l1.nil?? l2:l1;
    previoushead.next
end