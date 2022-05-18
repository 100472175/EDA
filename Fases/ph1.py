import random
import sys

from slist import SList
import time


class SList2(SList):

    def sumLastN(self, n):
        if self._size <= 0 or n == 0:
            return 0
        if n < 0:
            return None
        addition = 0
        nodeIT = self._head

        if n <= self._size:
            for _ in range(self._size - n):
                nodeIT = nodeIT.next

        while nodeIT is not None:
            addition += nodeIT.elem
            nodeIT = nodeIT.next
        addition += nodeIT.elem
        return addition

    # method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if self._size == 0:
            return self.addLast(elem)
        middle = 0
        if self._size % 2 == 0:
            middle = self._size // 2
        else:
            middle = (self._size + 1) // 2
        self.addFirst(None)
        nodeIT = self._head
        for i in range(middle):
            nodeIT.elem = nodeIT.next.elem
            nodeIT = nodeIT.next
        nodeIT.elem = elem  #

    def insertList(self, inputList, start, end):
        if not (start < 0 or end < 0) and not inputList.isEmpty():
            nodeADD = inputList._head
            if start == end:
                self.removeAt(start)
                for i in range(len(inputList)):
                    self.insertAt(start, nodeADD.elem)
                    if nodeADD.next is not None:
                        nodeADD = nodeADD.next
            else:
                for i in range(start, end + 1):
                    self.removeAt(start)
                for i in range(len(inputList)):
                    self.insertAt(start, nodeADD.elem)
                    if nodeADD.next is not None:
                        nodeADD = nodeADD.next

    """def reverseK_old(self, k):
        if k == 0:
            return None
        if self.isEmpty():
            return 0
        if k > len(self):
            k = len(self)

        nodeIT = self._head
        for i in range(len(self) // k):
            self.reverseKNodes(nodeIT, k)
            for j in range(k):
                nodeIT = nodeIT.next
        remainder = len(self) % k
        if remainder != 0:
            self.reverseKNodes(nodeIT, remainder)"""

    def reverseKNodesO33(self, pointer, k: int):
        start = pointer
        endpoint = round(k // 2) + k % 2
        for m in range(1, endpoint + 1):
            end = pointer
            for n in range(k - m):
                end = end.next
            start.elem, end.elem = end.elem, start.elem
            start = start.next

    def reverseK_alfonso(self, k):
        # Special Cases
        if self._size == 0:
            return None
        if k <= 1:
            return None
        if k > self._size:
            k = self._size

        # All auxiliar values
        aux = k
        ls_aux = SList2()
        selected_node_1 = self._head
        selected_node_2 = None
        selected_node_3 = None

        # Iterate the main SList (self)
        while selected_node_1 is not None:
            # Create first reverse group and select
            while aux > 0 and selected_node_1 is not None:
                ls_aux.addFirst(selected_node_1.elem)
                selected_node_1 = selected_node_1.next
                aux -= 1

                # Add first value and store it in a variable to store last element of aux list
                if aux == k - 1:
                    selected_node_2 = ls_aux._head

            if selected_node_2.elem == self._head.elem:
                self._head = ls_aux._head
                selected_node_2.next = selected_node_1
            else:
                selected_node_3.next = ls_aux._head
                selected_node_2.next = selected_node_1
            selected_node_3 = selected_node_2

            aux = k
            ls_aux = SList2()

    def maximumPairO4(self):
        if self.isEmpty():
            return None
        iterations = 0
        grandTotal = 0
        halfLength = round(self._size // 2 + self._size % 2)

        for i in range(halfLength):
            sumNode = 0
            nodeBottom = self._head
            nodeTop = self._head
            for j in range(iterations):
                nodeTop = nodeTop.next
            for k in range(self._size - iterations - 1):
                nodeBottom = nodeBottom.next
            if nodeTop.elem != nodeBottom.elem:
                sumNode = nodeTop.elem + nodeBottom.elem
            else:
                sumNode = nodeTop.elem
            if sumNode > grandTotal:
                grandTotal = sumNode
            iterations += 1

        return grandTotal

    def maximumPair(self):
        if self.isEmpty():
            return None
        if self._size == 1:
            return self._head.elem
        if self._size == 2:
            return self._head.elem + self._head.next.elem

        rev_list = SList2()
        nodeIT = self._head
        max_acceptable_pair = 0
        for i in range(self._size):
            rev_list.addFirst(nodeIT.elem)
            nodeIT = nodeIT.next
        nodeIT = self._head
        nodeIT_rev = rev_list._head
        for i in range(self._size // 2 + 1):
            intent = nodeIT_rev.elem + nodeIT.elem
            if i == self._size // 2:
                intent = intent / 2
            if intent > max_acceptable_pair:
                max_acceptable_pair = intent
            nodeIT = nodeIT.next
            nodeIT_rev = nodeIT_rev.next

        return max_acceptable_pair

    def reverseKNodes(self, k):
        if k == 0:
            return None
        if self.isEmpty():
            return 0
        if k > len(self):
            k = len(self)

        reversed_list = SList2()
        reversed_list.addFirst(0)
        reversed_pointer = reversed_list._head
        aux_pointer = None
        node_conversion_list = SList2()

        remainder = len(self) % k
        nodeIT = self._head

        for i in range(len(self) // k):
            aux_list = SList2()
            for j in range(k):
                aux_list.addFirst(nodeIT.elem)
                nodeIT = nodeIT.next

            aux_pointer = aux_list._head
            for k in range(aux_list._size):
                node_conversion_list = SList2()
                node_conversion_list.addFirst(aux_pointer.elem)
                reversed_pointer.next = node_conversion_list._head
                reversed_list._size += 1
                reversed_pointer = reversed_pointer.next
                aux_pointer = aux_pointer.next
                if i == 0 and k == 0:
                    reversed_list.removeFirst()

        reversed_list.removeFirst()
        for j in range(remainder):  # We don't need to check if the ramainder is 0 as if this was the case, the range
            # would never be executed
            reversed_list.addLast(nodeIT.elem)
            nodeIT = nodeIT.next

        self._head = reversed_list._head

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

        nodeIT = self._head  # Puntero a la lista original

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


"""
list1 = []
inputList = SList2()
for i in range(17):
    list1.append(i+1)
for x in list1:
    inputList.addLast(x)

print(inputList)
a = time.time()
inputList.papa(3)
b = time.time()
print(b - a)
print(inputList)"""

s = SList2()
quantity = 100_000_000
for i in range(quantity):
    s.addFirst(i)

a = time.time()
s.reverseK(3)
b = time.time()
print(b - a, "Time taken to reverse the list with %i elements" % quantity)


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

    """def insertList(self, inputList, start, end):  # Mirar que ha hecho Lucía
        """  # Replaces part of a list inside another list
    """
        if inputList.isEmpty() or self.isEmpty():
            return


        if not (start < 0 or end < 0):  # If the list is not empty and the start and end values are acceptable
            nodeADD = inputList._head
            true_head = self._head
            if start == end == 0:
                self.removeFirst()
                while nodeADD:
                    self.addFirst(nodeADD.elem)
                    nodeADD = nodeADD.next
                return
            if start == end:
                self.removeAt(start)
            for i in range(start - end):
                self.removeFirst()
            while nodeADD:
                self.addFirst(nodeADD.elem)
                nodeADD = nodeADD.next


            self._head = true_head

            return

        if inputList.isEmpty():
            return
        if self._size == 0 or end - start == self._size - 1:
            self._head = inputList._head
            return
        if start < 0 and end < start or end > len(self):
            return
        if start == end == 0:
            self._head = self._head.next
            node = inputList._head
            while node is not None:
                self.addFirst(node.elem)
                node = node.next
            return
        else:
            nodeADD = inputList._head
            nodeIT = self._head
            prev = self._head
            for i in range(start - 1):
                prev = prev.next
            nodeIT = prev
            for j in range(end - start):
                nodeIT = nodeIT.next
            prev.next = nodeADD
            while nodeADD is not None:
                nodeADD = nodeADD.next
            nodeADD.next = nodeIT"""

    def insertList(self, inputList, start, end):
        if self.isEmpty():
            self._head = inputList._head
        if inputList.isEmpty():
            return
        nodeIT = self._head

        if end - start == self._size - 1:
            self._head = inputList._head
            return

        nodeADD = inputList._head
        while nodeADD.next is not None:
            nodeADD = nodeADD.next

        for i in range(start - 1):
            nodeIT = nodeIT.next
        link = nodeIT
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
        """if end == self._size - 1:
            self.removeLast()"""

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
        for i in range(self._size // 2 + 1):
            intent = nodeIT_rev.elem + nodeIT.elem
            if i == self._size // 2:
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


######################################################################################################################

# Final:

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
        for i in range(self._size // 2 + 1):
            intent = nodeIT_rev.elem + nodeIT.elem
            if i == self._size // 2:
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
