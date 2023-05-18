from slistH import SList
from slistH import SNode

import sys


class SList2(SList):

    def delLargestSeq(self: SList):
        """
        This function travels throught the list once, using a two counters to find the largest sequences and
        some pointers to save the cut and paste nodes that will be use at the end. Pre_start saves the node previous
        to the start of the actual sequence so, in case it results being the new largest, the cut can be set again.
        The main pointer is actual_node, that follows the position in the list we are looking at.
        """
        highest_count = 1
        actual_count = 1
        cut = None
        paste = None
        pre_start = None
        actual_node = self._head

        # Travelling the list and finding the largest sequence
        for i in range(len(self)):
            if actual_node.next:
                if actual_node.elem == actual_node.next.elem:
                    actual_count += 1
                else:
                    if actual_count >= highest_count:
                        highest_count = actual_count
                        paste = actual_node.next
                        cut = pre_start
                    actual_count = 1
                    pre_start = actual_node
                actual_node = actual_node.next
            else:
                if actual_count >= highest_count:
                    highest_count = actual_count
                    paste = actual_node.next
                    cut = pre_start

        # Cutting the list at its largest sequence
        if cut:
            cut.next = paste
            self._size -= highest_count
        else:
            self._head = paste
            self._size -= highest_count


    def fix_loop(self):
        """
        This function fixes a loop in a list caused by the last node pointing towards one of the previous ones.
        In order to achieve this, the id of each element will be compared with the next one. Therefore, if the id of
        a node is lower than the id of the one that it is pointing at, the loop is detected and broken.
        """

        # We check if the list is empty before entering the loop
        if self._head is None:
            return False

        # The function will only end when a value is returned. Therefore, we can create an infinite loop and only
        # break it with the return of the function.
        node = self._head
        while True:
            # If we reach a None value, there is no loop. We return False and end the loop.
            if not node.next:
                return False
            # If a node's id is lower that the next one's id, it has been created before.
            # Therefore, we break the loop by changing the value to None and returning True.
            if id(node) < id(node.next):
                node.next = None
                return True
            node = node.next


    def leftrightShift(self, left:bool, n:int):
        """
        This function shift n elements of the list, counting from the left or from the right.

        Four variables are needed: one to control the node that will have to point to None, another to control
        the node that will control the first node that we shift, another to control the last node shifted and
        one last variable to control the node that follows the last shifted node.

        Since shifting from left or right are different processes, the variables will also have different names
        in order to reach a better understanding.
        """

        # We will use a conditional to control that the n is a natural number and is not greater than the length.
        if len(self) > n >= 1:

            # Shifting from the left side
            if left:
                newheadnode = self._head
                lastnode = self._head
                shiftednode = self._head
                lastshiftednode = self._head
                for i in range(len(self)-1):
                    if i < n:
                        newheadnode = newheadnode.next
                    if i < (n-1):
                        lastshiftednode = lastshiftednode.next
                    lastnode = lastnode.next
                # Reassemble the list
                self._head = newheadnode
                lastnode.next = shiftednode
                lastshiftednode.next = None

            # Shifting from the right side
            else:
                tobelinked = self._head
                shiftednode = self._head
                lastshiftednode = self._head
                tobecut = self._head
                for i in range(len(self)-1):
                    if i+1 <= len(self)-n:
                        shiftednode = shiftednode.next
                    if i+1 <= len(self):
                        lastshiftednode = lastshiftednode.next
                    if i+1 > n:
                        tobecut = tobecut.next
                # Reassemble the list
                self._head = shiftednode
                lastshiftednode.next = tobelinked
                tobecut.next = None






list1 = SList2()

print(list1)
print(len(list1))

list1.addLast(1)
list1.addLast(2)
list1.addLast(3)
list1.addLast(4)
list1.addLast(5)

