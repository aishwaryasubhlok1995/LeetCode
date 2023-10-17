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

def merge_two_lists(l1, l2)
    dummy = ListNode.new
    current = dummy
    
    while l1 && l2
      if l1.val < l2.val
        current.next = l1
        l1 = l1.next
      else
        current.next = l2
        l2 = l2.next
      end
      current = current.next
    end
    
    current.next = l1 || l2
    dummy.next
  end