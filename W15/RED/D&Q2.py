def OA(s, c):
    if s is None or len(s) == 0:
        return None

    if len(s) > 1:
        if s == c:
            return

    m = len(s) // 2
    half1 = s[:m]
    half2 = s[m + 1:]

    max1 = OA(half1, c)
    max2 = OA(half2, c)

    if len(max1) < len(max2):
        return max2
    else:
        return max1


data = ['john', 'adam', 'alexander', 'robert', 'gerard']


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

datas = [1, 2, 3, 4, 5, 2, 7, 8, 2]
print(getIndices(datas, 2))
