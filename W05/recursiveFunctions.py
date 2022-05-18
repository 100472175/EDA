a = [17, 15, 67, -9, 0, 33]


def minimum(e: list):
    if len(e) == 1:
        return e[0]

    return min(e[0], minimum(e[1:]))


print(minimum(a))


def palindrome_test(w: str):
    if len(w) <= 1:
        return True

    if w[0] == w[-1]:
        return palindrome_test(w[1:-1])
    else:
        return False


def check_sorted(l: list):
    if len(l) <= 1:
        return True
    if l[0] <= l[1]:
        return check_sorted(l[1:])
    else:
        return False


def SUMD(n):
    if n < 10:
        return n
    return SUMD(n//10) + n % 10


def russianMult(a: int, b: int):
    if a == 1:
        return b
    if b == 1:
        return a
    if a == 0:
        return 0
    if b == 0:
        return 0

    if a % 2 == 0:
        return russianMult(a/2, b*2)
    return b + russianMult(a//2, b*2)



