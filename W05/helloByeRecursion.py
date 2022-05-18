import sys

sys.setrecursionlimit(10000)


def rec1(a):

    if a > 3:
        return a

    print("hello " + str(a))
    ret = rec1(a + 1)
    print("bye " + str(a))
    return ret + a

rec1(1)
