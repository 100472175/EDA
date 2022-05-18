from dlist import DList


def checkPalindrome(word: str):
    dl = DList()
    for c in word:
        dl.addLast(c)

    pal = True
    front = dl.head
    back = dl.tail
    """
    for i in range(dl.size//2):
        if front.elem == back.elem:
            front = front.next
            back = back.prev
            pal = True
        else:
            pal = False
    # return pal
    """

    sz2 = dl.size // 2
    it = 0
    while pal is True and it < sz2:
        if front.elem == back.elem:
            front = front.next
            back = back.prev
        else:
            return False
        it += 1
    return True

