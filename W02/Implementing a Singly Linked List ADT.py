class SNode:
    def __init__(self, e, next=None):
        self.elem = e
        self.next = next
        newNode = SNode(e)


class SList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, e):
        newNode = SNode(e)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def removeFirstNode(self):
        result = None
        if self.isEmpty():
            print("List is emtpy!!!")
        else:
            result = self.head.elem
            self.head = self.head.next
            self.size -= 1
        return result

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def addLast(self, e):
        if self.isEmpty():
            self.addFirst(e)
        else:
            newNode = SNode(e)
            node = self.head  # Toma la cabeza de la lista
            while node.next is not None:
                node = node.next
            node.next = newNode
            self.size += 1

    def removeLast(self):
        node = self.head  # Toma la cabeza de la lista
        for i in range(self.size):
            if node.next.next is None:
                break
        result = node.next.elem
        node.next = None
        return result
