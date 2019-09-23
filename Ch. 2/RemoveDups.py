# Remove duplicates from a (singly) linked list

import LinkedList as ll

# Loop through each node O(n)
def removeDups(linked_list):
    d = {}

    curr = linked_list.head
    prev = None
    while curr is not None:
        if curr.value in d:
            prev.next = curr.next
            curr = curr.next
        else:
            d[curr.value] = 1
            prev = curr
            curr = curr.next

    return linked_list

values = input('Enter values: ')
linked_list = ll.LinkedList(values.split())
linked_list.printList()
print('After removing duplicates')
linked_list = removeDups(linked_list)
linked_list.printList()

