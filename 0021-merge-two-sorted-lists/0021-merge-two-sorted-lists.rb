# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(list1, list2)
    dummy = ListNode.new
    p = dummy
    while list1 != nil && list2 != nil
        if list1.val < list2.val
            p.next = list1
            p = list1
            list1 = list1.next
        else
            p.next = list2
            p = list2
            list2 = list2.next
        end
    end
        if list1 != nil
            p.next = list1
        end
        if list2 != nil
            p.next = list2
        end
        return dummy.next
end
