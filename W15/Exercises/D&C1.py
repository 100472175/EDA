# Function that returns the smallest even number in a python list
def smallest_even(lists):
    if lists is None or len(lists) == 0:
        return None

    if len(lists) == 1:
        if lists[0] % 2 == 0:
            return lists[0]
        else:
            return None

    m = len(lists) // 2
    part1 = lists[:m]
    part2 = lists[m + 1:]

    min1 = smallest_even(part1)
    min2 = smallest_even(part2)

    if min1 is not None and min2 is not None:
        return min(min1, min2)
    elif min1 is None:
        return min2
    elif min2 is None:
        return min1
    else:
        return None


def get_indexes(data: list, x):
    return _get_indexes(data, x, 0, len(list)-1)


def _get_indexes(lists: list, x, start: 0, end):
    if lists is None or len(lists) == 0:
        return None

    if start > end:
        return []
    if start == end:
        if lists[start] == x:
            return [start]
        else:
            return []

    mid = (start + end) // 2
    index1 = _get_indexes(lists, x, start, mid)
    index2 = _get_indexes(lists, x, mid + 1, end)

    return index1 + index2


def sumMultiples(data, x):
    if data is None or len(data) == 0 or x is None:
        return -1

    if len(data) == 1:
        if data[0] % x == 0:
            return data[0]
        else:
            return 0

    mid = len(data) // 2
    half1 = sumMultiples(data[:mid], x)
    half2 = sumMultiples(data[mid+1:], x)

    return half1 + half2


def maximumList(data):
    if data is None or len(data) == 0:
        return None

    if len(data) == 1:
        return data[0]

    mid = len(data) // 2
    half1 = maximumList(data[:mid])
    half2 = maximumList(data[mid + 1:])

    return max(half1, half2)


def findLowestEvenOdd(a):
    if a is None or len(a) == 0:
        return None, None

    if len(a) == 1:
        if a[0] % 2 == 0:
            return a[0], None
        else:
            return None, a[0]

    m = len(a) // 2
    part1 = a[0:m]
    part2 = a[m:]

    even1, odd1 = findLowestEvenOdd(part1)
    even2, odd2 = findLowestEvenOdd(part2)

    if even1 is not None and even2 is not None:
        even = min(even1, even2)
    elif even1 is not None:
        even = even1
    else:
        even = even2

    if odd1 is not None and odd2 is not None:
        odd = min(odd1, odd2)
    elif odd1 is not None:
        odd = odd1
    else:
        odd = odd2

    return even, odd


def LongestString(data):
    if data is None or len(data) == 0:
        return None

    if len(data) == 0:
        return data[0]

    m = len(data) // 2
    part1 = data[:m]
    part2 = data[m+1:]

    word1 = LongestString(part1)
    word2 = LongestString(part2)

    if len(word1) > len(word2):
        return word1
    else:
        return word2


def count(data, letter):
    if data is None or len(data) == 0:
        return 0

    if len(data) == 1:
        if data[0] == letter:
            return 1
        else:
            return 0

    m = len(data) // 2
    part1 = data[:m]
    part2 = data[m+1:]

    count1 = count(part1, letter)
    count2 = count(part2, letter)

    return count1 + count2


def WordsLengthSmallerEqual(data, length):
    if data is None or len(data) == 0:
        return 0

    if len(data) == 1:
        if len(data[0]) <= length:
            return data[0]
        else:
            return []

    m = len(data) // 2
    part1 = data[:m]
    part2 = data[m + 1:]

    words_left = WordsLengthSmallerEqual(part1, length)
    words_right = WordsLengthSmallerEqual(part2, length)

    return words_right + words_left


def IndexOfElement(a, x):
    if a is None or len(a) == 0:
        return -1
    return _IndexOfElement(a, x, 0, len(a)-1)


def _IndexOfElement(a, x, start, end):
    if start > end:
        return -1

    m = (start + end) // 2
    if x == a[m]:
        return m

    if x < a[m]:
        return _IndexOfElement(a, x, start, m - 1)
    else:
        return _IndexOfElement(a, x, m + 1, end)


def getIndices(data, x):
    if data == None or len(data) == 0:
        return []
    return _getIndices(data, x, 0, len(data)-1)

def _getIndices(data, x, start, end):

    if start == end:
        if data[start] == x:
            return [start]
        else:
            return []

    m = (start + end) // 2
    half1 = _getIndices(data, x, start, m)
    half2 = _getIndices(data, x, m+1, end)

    return half1 + half2



data = [1,2,3,4,5,6,7,8,9,1,"a",20,50,2]
data2 = getIndices(data, 2)
print(len(data))
print(data2)


def BinarySeach(data, x):
    # Devuelve índices
    if data is None or len(data) == 0 or x is None:
        return -1

    return _BinarySearch(data, x, 0, len(data)-1)


def _BinarySearch(data, x, start, end):
    if start == end:
        if data[start] == x:
            return [start]
        else:
            return []

    m = (start + end) // 2
    left = _BinarySearch(data, x, start, m)
    right = _BinarySearch(data, x, m+1, end)

    return left + right

data = [1, 2, 3, 4, 5, 6, 7, 8]
print(data)
print("Binary Search", BinarySeach(data, 2))

