from slist import SList
from slist import SNode

class SSList(SList):
    def fix_loop(self):
        """This function fixes the loop in the list, with the time complexity != O(n^^2) or using Ids or length"""
        

    def move(self, slow, fast):
        slow = slow.next
        fast = fast.next.next
        return slow, fast



if __name__ == "__main__":
    a = SSList()
    a.addLast("a")
    a.addLast("b")
    a.addLast("c")
    a.addLast("d")
    a.addLast("e")
    a._head.next.next.next.next.next = a._head.next.next
    a.fix_loop()
    print(a)
