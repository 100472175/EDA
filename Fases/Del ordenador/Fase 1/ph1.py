import random

from slist import SList
import sys
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

        while nodeIT.next is not None:
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
        nodeIT.elem = elem

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

    def reverseK(self, k):
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
            self.reverseKNodes(nodeIT, remainder)

    def reverseKNodes(self, pointer, k: int):
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

    def maximumPair(self):
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


list1 = []
inputList = SList2()
for i in range(1000000):
    list1.append(random.randint(0, 100))
for x in list1:
    inputList.addLast(x)

a = time.time()
inputList.reverseK_alfonso(len(inputList) + 1)
b = time.time()
print(b - a)
