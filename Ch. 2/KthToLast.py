# Find kth to last element of singly linked list

import LinkedList as ll

def findKthToLast(linked_list, k):
    pointer_1 = linked_list.head
    pointer_2 = linked_list.head
    temp = pointer_1

    while k > 1:
        pointer_2 = temp.next
        temp = temp.next
        k -= 1

    while pointer_2.next is not None:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    return pointer_1.value

values = input('Enter values: ')
k = input('Enter k: ')
linked_list = ll.LinkedList(values.split())
linked_list.printList()
print('kth to last element is:', findKthToLast(linked_list, int(k)))

