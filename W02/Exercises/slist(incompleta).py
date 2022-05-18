# -*- coding: utf-8 -*-
"""SList(incompleta).ipynb
Original file is located at
    https://colab.research.google.com/drive/1u5NRZOHwQrDVv8Td9-BNWQMxaxHBkca-
"""


class SNode:
    def __init__(self, e, next=None):
        self.elem = e
        self.next = next
        self.previous = None


class SList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def getAt(self, index):
        if index < 0 or index >= (self.size - 1):
            print("out of range")
            return None

        i = 0
        nodeIT = self.head
        while i < index:
            nodeIT = nodeIT.next
            i += 1
        return nodeIT.elem

    def addFirst(self, e):
        newNode = SNode(e)
        newNode.next = self.head
        self.head = newNode
        if self.isEmpty():
            self.tail = newNode
        self.size += 1

    def addLast(self, e):
        if self.isEmpty():
            self.addFirst(e)
        else:
            newNode = SNode(e)
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def removeFirst(self):
        result = None
        if self.isEmpty():
            print("List is emtpy!!!")
        else:
            result = self.head.elem
            self.head = self.head.next
            self.size -= 1
            if self.isEmpty():
                self.head = self.tail = None
        return result

    def insertOn(self, e, index):
        if index < 0 or index >= self.size:
            print("out of range")
            return None
        i = 0
        nodeIT = self.head
        while i < index-1:
            nodeIT = nodeIT.next
            i += 1
        nodeRest = nodeIT.next
        nodeIT.next = SNode(e)
        nodeIT.next.next = nodeRest

    def removeLast(self):
        result = None
        if self.isEmpty():
            print("List is emtpy!!!")
        else:
            penult = None  # will point to the penultimate node
            last = self.head  # will point to the last node
            while last.next != None:
                penult = last
                last = last.next

            if penult is None:
                # the list only has an element
                result = self.removeFirst()
            else:
                result = last.elem
                penult.next = None
                self.size -= 1
            self.tail = penult

        return result

    def contains(self, e):
        nodeIT = self.head
        counter = 0
        while nodeIT.elem != e:
            nodeIT = nodeIT.next
            counter += 1
            if counter == self.size:
                return -1
        return 1

    """
        nodeIT = self.head
        counter = 0
        found = True
        while nodeIT is not None and found=False:
            if nodeIT.elem == e:
                found = True
            counter += 1
            nodeIT = nodeIT.next
        if found:
            return 1
        else:
            return -1
    """

    #  def addLast(self,e):
    #    if self.isEmpty():
    #      self.addFirst(e)
    #    else:
    #      newNode=SNode(e)
    #      nodeIt=self.head
    #      for i in range(1,self.size):
    #        nodeIt=nodeIt.next
    # nodeIt is the last node
    #      nodeIt.next=newNode
    #      self.size +=1

    def __str__(self):
        result = ''
        nodeIt = self.head
        while nodeIt is not None:
            result += str(nodeIt.elem) + ','
            nodeIt = nodeIt.next
        if len(result) > 0:
            result = result[:-1]
        return result


#  def removeLast(self):
#    result=None
#    if self.isEmpty():
#      print("List is emtpy!!!")
#    elif self.size==1:
#      result=self.removeFirst()
#    else:
#      nodeIt=self.head
#      while nodeIt.next.next!=None:
#        nodeIt=nodeIt.next
# nodeIt is the penultimate node of the list
#      last=nodeIt.next
#      result=last.elem
#      nodeIt.next=None
#      self.size -=1
#    return result

import random

l = SList()
for i in range(1, 10):
    # l.addLast(random.randint(0,10))
    l.addLast(i)
print('List:', str(l))
print('len:', len(l))

print(l.contains("de"))

# o = SNode("e")
# print(o)


"""
l = SList()
for i in range(1, 10):
    # l.addLast(random.randint(0,10))
    l.addLast(i)
print('List:', str(l))
print('len:', len(l))

l.addFirst(0)
print('List:', str(l))
print('len:', len(l))

print(l.removeLast())
print('List:', str(l))
print('len:', len(l))

print(str(l))
print(l.removeLast())
print(str(l))

while len(l) > 0:
    print(l.removeLast())

print(l.removeLast())
"""
