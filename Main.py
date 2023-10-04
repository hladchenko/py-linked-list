from LinkedList import LinkedList

linked_list = LinkedList(1)

linked_list.add(2)
linked_list.add(3)
linked_list.add(4)

linked_list.remove(4)

linked_list.print_list()

print("\nLinked list size is: ", linked_list.get_size())
print("First: ", linked_list.get_first())
print("Last: ", linked_list.get_last())
print("Is empty: ", linked_list.is_empty())
linked_list.clear()
print("Is empty: ", linked_list.is_empty())

linked_list.add(6)
linked_list.print_list()
print("Size: ", linked_list.get_size())
