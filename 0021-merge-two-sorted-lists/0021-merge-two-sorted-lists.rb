def merge_two_lists(list1, list2)
  node = pre_res = ListNode.new(0)
  while list1 && list2
    if list1.val <= list2.val
      node.next = list1
      list1 = list1.next
    else
      node.next = list2
      list2 = list2.next
    end
    node = node.next
  end

  # Link the remaining elements of the non-empty list
  if list1.nil?
    node.next = list2
  else
    node.next = list1
  end

  pre_res.next
end