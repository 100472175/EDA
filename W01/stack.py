#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# THINK; SIMPLE; PROTECT

class Stack1:
    """LIFO Stack implementation using a Python list as storage.
  The top of the stack stored at the end of the list."""

    def __init__(self):
        """Create an empty stack"""
        self.items = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self.items)

    def isEmpty(self):
        """Return True if the stack is empty"""
        return len(self) == 0

    def __str__(self):
        # print the elements of the list
        return str(self.items)

    def push(self, e):
        """Add the element e to the top of the stack"""
        self.items.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack"""
        if self.isEmpty():
            print('Error: Stack is empty')
            return None

        return self.items.pop()  # remove last item from the list

    def top(self):
        """Return the element from the top of the stack"""
        if self.isEmpty():
            print('Error: Stack is empty')
            return None

        # returns last element in the list
        return self.items[-1]


"""## Second option: top at the first position of the list```

#We could have chosen to implement the stack using a list where
#the top is at the beginning instead of at the end. In this case, the previous pop and append methods would no longer work and we would have to index position 0 (the first item in the
#list) explicitly using pop and insert. The implementation is shown below.
#"""


class Stack2:
    """LIFO Stack implementation using a Python list as storage.
  The top of the stack is stored at the beginning of the list."""

    def __init__(self):
        self.items = []

    # tests if the stack is empty
    def isEmpty(self):
        """This method tests if the stack is empty. You
    can implement it in different ways"""
        # return len(self.items)==0
        # return len(self)==0
        return self.items == []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    # adds at the beginning of the list
    def push(self, item):
        self.items.insert(0, item)

    # removes and returns the top element
    def pop(self):
        if self.isEmpty():
            print('Error: Stack is empty')
            return None

        # return the first element
        return self.items.pop(0)

    # returns the top element
    def top(self):
        if self.isEmpty():
            print('Error: Stack is empty')
            return None

        return self.items[0]


"""**What implementation is better? **
Althought the above implementations are logically equivalent, the first one is better 
than the second one because they operations append and pop() operations are both O(1), 
while insert(0) and pop(0) have linear complexity (O(n) for a stack of size n). 
In other words, the second implementation (top element is stored at 
the fist position of the list) requires more time complexity 
than the first one (where the top element is stored at the end of the list). 
"""

test1 = False  # set  to True to test Stack1
if test1:
    print('testing Stack1')
    s = Stack1()
    print('isEmpty()', s.isEmpty())
    s.push('W')
    s.push('O')
    print('top element', s.top())
    print('isEmpty()', s.isEmpty())
    s.push('R')
    s.push('D')
    print('Content of stack', str(s))
    print('pop:', s.pop())
    print('Content of stack', str(s))
    print('top element:', s.top())
    print()

m = Stack1()
reword = ""
for w in input():
    m.push(w)

if len(m) != 0:
    for q in range(len(m)):
        reword += m.pop()
print(reword)


test2 = False  # set  to True to test Stack2
if test2:
    print('testing Stack2')
    s = Stack2()
    print('isEmpty()', s.isEmpty())
    s.push('W')
    s.push('O')
    print('top element', s.top())
    print('isEmpty()', s.isEmpty())
    s.push('R')
    s.push('D')
    print('Content of stack', str(s))
    print('pop:', s.pop())
    print('Content of stack', str(s))
    print('top element:', s.top())

print()


def check_parenthesis():
    a = input("Enter your expression: ")
    expression = Stack1
    for i in len(expression):
        j = expression.items[i]
        if not (i != "(" and i != ")"):
            expression.push(i)
