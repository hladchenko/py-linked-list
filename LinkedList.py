from Node import Node


class LinkedList:
    __size = 0

    def __init__(self, element):
        self.__first = Node(element)
        self.__last = self.__first
        self.__size = 1

    @staticmethod
    def of(arr):
        new_list = LinkedList(arr[0])
        for i in range(1, len(arr)):
            new_list.add(arr[i])
        return new_list

    def add(self, element):
        if self.__first is None:
            self.__first = Node(element)
            self.__last = self.__first
        else:
            self.__last.next = Node(element)
            self.__last = self.__last.next
        self.__size += 1

    def add_by_index(self, index, element):
        new_node = Node(element)
        if index == 0:
            self.__first, new_node.next = new_node, self.__first
        elif index > self.__size:
            return
        else:
            current, i = self.__first, 1
            while current is not None:
                if index == i:
                    current.next, new_node.next = new_node, current.next
                current, i = current.next, i + 1
        self.__size += 1

    def set(self, index, element):
        if index > self.__size - 1:
            return
        current, i = self.__first, 0
        while current is not None:
            if i == index:
                current.element = element
            current, i = current.next, i + 1

    def remove(self, element):
        if self.__first.element == element:
            self.__first = self.__first.next
            self.__size -= 1
        else:
            prev = self.__first
            current = self.__first.next
            while current is not None:
                if current.element == element:
                    if current.next is not None:
                        prev.next = current.next
                    else:
                        self.__last = prev
                        prev.next = None
                    self.__size -= 1
                prev = current
                current = current.next

    def print_list(self):
        self.__print(self.__first)

    def __print(self, root):
        if root is not None:
            print(root.element)
            self.__print(root.next)

    def get_size(self):
        return self.__size

    def get_first(self):
        return self.__first.element

    def get_last(self):
        return self.__last.element

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def contains(self, element):
        current = self.__first
        while current is not None:
            if current.element == element:
                return True
            current = current.next
        return False
