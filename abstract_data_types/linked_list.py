import operator
from abstract_data_types.node import Node


class LinkedList:
    def __init__(self):
        """
        This constructor initialises the head and size of the LinkedList
        :complexity: O(1)
        """
        self.head = None
        self.size = 0

    def __str__(self):
        """
        This function overrides the built-in __str__ function so it returns the LinkedList in a line break delimited
        string for printing
        :return: line break delimited string representation of LinkedList
        :complexity: O(N)
        """
        node = self.head
        string_rep = ""
        while node is not None:
            string_rep += str(node.data)
            node = node.next
            if node is not None:
                string_rep += ", "
        return string_rep

    def __len__(self):
        """Overrides the built-in __len__ function to return the size of the ArrayList"""
        return self.size

    def __contains__(self, item):
        """
        This function overrides the built-in __contains__ function, returning if a target item is in the LinkedList
        :param item: target item to be found in the LinkedList
        :return: True if the target item is in the LinkedList, False otherwise
        :complexity: O(N)
        """
        node = self.head
        while node is not None:
            if node.data == item:
                return True
            node = node.next
        return False

    def __getitem__(self, index):
        """
        This function overrides the built-in __get__ item function, getting an item from the user-specified index
        :param index: index location of the target item
        :return: the item in the LinkedList at location index
        :complexity: O(N)
        """
        index = self._index_checking(index)
        return self._get_node(index).data

    def __setitem__(self, index, item):
        """
        This function overrides the built-in __setitem__ function, setting an item at the user-specified index
        :param index: index of the target location
        :param item: the item to be set at the location
        :complexity: O(N)
        """
        index = self._index_checking(index)
        if index == 0:
            self.head = Node(item, self.head.next)
        else:
            node = self._get_node(index-1)
            node.next = Node(item, node.next)

    # recall that "is" checks for object equality, but == checks for value equality
    def __eq__(self, other):
        """
        Overrides the built-in __eq__ function, returning if the contents of the ArrayList have the same values as a
        user-defined object
        :param other: the object to be compared with
        :return: True if the ArrayList is the same as the object compared, False otherwise
        :complexity: O(N)
        """
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
        return True

    def prepend(self, item):
        """
        Prepends an item to the front of the LinkedList
        :param item: the item to prepend
        :complexity: O(1)
        """
        if self.size == 0:
            self.head = Node(item, None)
        else:
            self.head = Node(item, self.head)
        self.size += 1

    def append(self, item):
        """
        Appends an item to the end of the LinkedList
        :param item: the item to append
        :complexity: O(N)
        """
        if self.size == 0:
            self.head = Node(item, None)
        else:
            node = self._get_node(self.size-1)
            node.next = Node(item, None)
        self.size += 1

    def insert(self, index, item):
        """
        Inserts an item to the user-specified index
        :param index: index to insert at
        :param item: the item to insert
        :precondition: index is an integer within the bounds of the LinkedList
        :complexity: O(N)
        """
        if index == 0:
            self.head = Node(item, self.head.next)
        else:
            index = self._index_checking(index)
            node = self._get_node(index-1)
            node.next = Node(item, node.next)
        self.size += 1

    def remove(self, item):
        """
        Removes the first instance of a user-specified item from the list
        :param item: the item to remove
        :raises ValueError: if the item is not found in the list
        :complexity: O(N)
        """
        found = False
        for i, elem in enumerate(self):
            if elem == item:
                found = True
                break
        if not found:
            raise ValueError
        else:
            self.delete(i)

    def delete(self, index):
        """
        Deletes the item at the user-specified index
        :param index: the index to delete the item from
        :complexity: O(N)
        """
        if index == 0:
            self.head = self.head.next
        else:
            index = self._index_checking(index)
            if index == 0:
                self.head = None
            else:
                node = self._get_node(index-1)
                node.next = node.next.next
        self.size -= 1

    def sort(self, reverse=False):
        """
        Sorts the list in either ascending or descending order with merge sort
        :param reverse: set to True if the list should be sorted in descending order, False otherwise
        :complexity: O(N log N)
        """
        if not reverse:
            op_func = operator.le
        else:
            op_func = operator.ge
        self.head = self._merge_sort(op_func).head

    def _merge_sort(self, op_func):
        """
        Auxiliary merge sort function to split list into left and right until the list is length 1 or more
        :param op_func: operator function for determining forward or reverse sort
        :return: the sorted list
        :complexity: O(N log N)
        """
        if len(self) <= 1:
            return self
        left_list = LinkedList()
        right_list = LinkedList()
        for i in range(len(self)):
            if i < len(self)/2:
                left_list.append(self[i])
            else:
                right_list.append(self[i])
        left = left_list._merge_sort(op_func)
        right = right_list._merge_sort(op_func)
        return self._merge(left, right, op_func)

    @staticmethod
    def _merge(left_side, right_side, op_func):
        """
        Merges two lists in sorted order
        :param left_side: left list
        :param right_side: right list
        :param op_func: operator function for determining forward or reverse sort
        :return: merged list
        :complexity: O(N)
        """
        merged_list = LinkedList()
        while left_side and right_side:
            if op_func(left_side[0], right_side[0]):
                merged_list.append(left_side[0])
                left_side.delete(0)
            else:
                merged_list.append(right_side[0])
                right_side.delete(0)
        while left_side:
            merged_list.append(left_side[0])
            left_side.delete(0)
        while right_side:
            merged_list.append(right_side[0])
            right_side.delete(0)
        return merged_list

    def __iter__(self):
        """Returns the list iterator object"""
        return ListIterator(self.head)

    def _index_checking(self, index):
        """
        Checks if the index is within the range of the list
        :param index: index to check
        :raises IndexError: if the index is outside the range of the list
        :complexity: O(1)
        """
        if self.size == 0:
            if index == 0 or index == -1:
                return index
        if not -self.size <= index <= self.size - 1:
            raise IndexError("list index out of range")
        if index < 0:
            index += self.size
        return index

    def _get_node(self, index):
        """
        Gets the node required by the calling function by index
        :param index: the index of the node in the LinkedList required
        :return: the node at the index specified
        :complexity: O(N)
        """
        node = self.head
        for _ in range(index):
            node = node.next
        return node


class ListIterator:
    def __init__(self, head):
        """
        Constructor for initialising the head of the iterator
        :param head: head node of the LinkedList
        :complexity: O(1)
        """
        self.current = head

    def __iter__(self):
        """Returns itself as the iterator for itself"""
        return self

    def __next__(self):
        """
        Provides the next element in the iterator
        :raises StopIteration: if there are no more elements to iterate through
        :complexity: O(1)
        """
        if self.current is None:
            raise StopIteration
        item = self.current.data
        self.current = self.current.next
        return item
