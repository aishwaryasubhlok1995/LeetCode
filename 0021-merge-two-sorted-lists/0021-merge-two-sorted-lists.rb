=begin
Question 2

Solve the following leetcode problem using Ruby language

21. Merge Two Sorted Lists

(submit screen shot of submission and source code file)

=end

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
    return if !list1 && !list2
    return list1 unless list2
    return list2 unless list1
    if list1.val > list2.val
        list1, list2 = list2, list1
    end
    list1.next = merge_two_lists(list1.next, list2)
    list1
end