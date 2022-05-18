import random
import sys

from slist import SList


class SList2(SList):

    def sumLastN(self, n):
        """Sums the last n elements of the list"""
        if self._size <= 0 or n == 0:  # If the list is empty or the number of elements is 0, return 0
            return 0
        if n < 0:
            return None
        addition = 0
        nodeIT = self._head

        if n <= self._size:  # If the n is smaller than the number of elements in the list, advance the pointer until
            # there are only n elements until the end of the list from the pointer
            for _ in range(self._size - n):
                nodeIT = nodeIT.next
        # Until the end of the list, add the elements of the list, from the pointer, forwards
        while nodeIT:
            addition += nodeIT.elem
            nodeIT = nodeIT.next
        return addition

    def insertMiddle(self, elem):
        """Method to insert a new node in the middle of a list"""
        if self._size == 0:
            return self.addLast(elem)
        # Calculate where the middle of the list is
        middle = 0
        if self._size % 2 == 0:
            middle = self._size // 2
        else:
            middle = (self._size + 1) // 2
        self.addFirst(None)
        nodeIT = self._head
        # Move the elements one by one until the elements is in the middle of the list
        for i in range(middle):
            nodeIT.elem = nodeIT.next.elem
            nodeIT = nodeIT.next
        nodeIT.elem = elem
        """This is not as effective as creating a node in the middle, but as we did not have the Snode class imported 
        in the file and we can't edit the imported classes, this is the way we propose it is done"""

    def insertList(self, inputList, start, end):
        # Initial checks
        if self.isEmpty():
            self._head = inputList._head
        if inputList.isEmpty():
            return
        nodeIT = self._head

        # Is the replacement is going to be of the entire list
        if end - start == self._size - 1:
            self._head = inputList._head
            return

        # Navigate to the last element of the list you want to add
        nodeADD = inputList._head
        while nodeADD.next is not None:
            nodeADD = nodeADD.next
        # Navigate to the last element you want to replace
        for i in range(start - 1):
            nodeIT = nodeIT.next
        link = nodeIT
        # Add the list and lik the en to the end of the replacement part of the original list
        if end == start:
            nodeIT.next, nodeADD.next = inputList._head, nodeIT.next
        else:
            addition = 0
            if start != 0:
                addition = 1
            for i in range(end - start + addition):
                link = link.next
            nodeIT.next = inputList._head
            nodeADD.next = link.next
        if start == 0:
            self.removeFirst()


    def maximumPair(self):
        "Returns the maximum pair of the first with the last element of the list"
        if self.isEmpty():
            return None
        if self._size == 1:
            return self._head.elem
        if self._size == 2:
            return self._head.elem + self._head.next.elem

        # Creating a reversed list, so we can have a similar structure of Double liked lists, being able to go forwards
        # and backwards
        rev_list = SList2()
        nodeIT = self._head
        max_acceptable_pair = 0
        for i in range(self._size):
            rev_list.addFirst(nodeIT.elem)
            nodeIT = nodeIT.next
        # Selecting the start and "end" of the original list and traversing them one by one and adding them up
        nodeIT = self._head
        nodeIT_rev = rev_list._head
        for i in range(self._size//2 + 1):
            intent = nodeIT_rev.elem + nodeIT.elem
            if i == self._size//2:
                intent = intent / 2
            if intent > max_acceptable_pair:
                max_acceptable_pair = intent
            nodeIT = nodeIT.next
            nodeIT_rev = nodeIT_rev.next

        return max_acceptable_pair

    def reverseK(self, k):
        if k == 0:
            return None
        if self.isEmpty():
            return 0
        if k > len(self):
            k = len(self)

        # def_pointer = None
        tail_pointer = None
        # aux_pointer = None
        added_pointer = None
        defi = SList2()

        nodeIT = self._head  # Pointer to the original list

        # The addition of the list is based on the  principle that we have to make groups of k elements,
        # reversing them and adding them to the list. It is not very memory efficient, as it needs to create multiple
        # lists. We change the pointer where if starts to insert fist, so we have linked elements but not accessible by
        # self._head but by another pointer.
        for i in range(len(self) // k):
            aux_list = SList2()
            for j in range(k):
                aux_list.addFirst(nodeIT.elem)
                if j == 0:
                    tail_pointer = aux_list._head
                nodeIT = nodeIT.next
            if i == 0:
                defi._head = aux_list._head
            else:
                added_pointer.next = aux_list._head
            added_pointer = tail_pointer

        # This last part is for the elements that can't fit inside the group of k elements, so we need a special case
        aux_list = SList2()
        remainder = len(self) % k
        for j in range(remainder):
            aux_list.addFirst(nodeIT.elem)
            if j == 0:
                tail_pointer = aux_list._head
            nodeIT = nodeIT.next
        added_pointer.next = aux_list._head
        added_pointer = tail_pointer

        self._head = defi._head
