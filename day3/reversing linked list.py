# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.next = None

# def reverse_second_half(head):
    
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

   
#     prev = None
#     current = slow
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node

    
#     second_half_head = prev
#     first_half_tail = slow
#     while first_half_tail.next:
#         first_half_tail = first_half_tail.next
#     first_half_tail.next = second_half_head

#     return head
# print(head)
