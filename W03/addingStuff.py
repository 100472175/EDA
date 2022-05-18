from dlist import DList
from dlist import DNode


class DList1(DList):
    def getAtRev(self, index):
        if index < 0 or index >= self.size:
            print(index, 'error: index out of range')
            return None

        i = self.size - 1
        current = self.tail
        while i > index:
            current = current.prev
            i += 1
        return current

    def getAtEff(self, index):
        if index < 0 or index >= self.size:
            print(index, 'error: index out of range')
            return None
        if index < self.size // 2:
            return self.getAt(index)
        else:
            return self.getAtRev(index)

    def reverse(self):
        """By swapping the data"""
        top, bottom = self.head, self.tail

        for _ in range(len(self)//2):
            """aux = top.elem
            top.elem = bottom.elem
            bottom.elem = aux
            top = top.next
            bottom = bottom.prev"""

            top.elem, bottom.elem = bottom.elem, top.elem
            top = top.next
            bottom = bottom.prev

    def reverse2(self):
        """By swapping the references"""
        aux = self.head
        for _ in range(self.size):
            aux.next, aux.prev = aux.prev, aux.next
            aux = aux.prev
        self.head, self.tail = self.tail, self.head

    def isSorted(self):
        if self.isEmpty():
            print("List if empty")
            return True
        aux = self.head
        for _ in range(self.size-1):
            if aux.elem > aux.next.elem:
                return False
            else:
                aux = aux.next
        return True


class User:
    def __init__(self, u, p):
        self.username = u
        self.password = p

    def __gt__(self, other):
        return self.username > other.usename


dl = DList1()
for i in range(10):
    dl.addLast(i)
dl.addLast("a")
dl.addFirst("b")

