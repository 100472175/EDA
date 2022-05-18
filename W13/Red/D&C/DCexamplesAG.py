
# FIND MAXIMUM ELEMENT IN AN ARRAY
def findMax(A):
    """returns the greatest element of A"""
    # A none or A=[] "empty array"
    if A is None or len(A) == 0:
        return None

    # base case
    if len(A) == 1:
        return A[0]

    # Recursive case
    # DIVIDE
    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    # CONQUER
    max1 = findMax(part1)  # maximum in array part1
    max2 = findMax(part2)  # maximum in array part2

    # COMBINE
    return max(max1, max2)


# FIND MAXIMUM ELEMENT IN AN ARRAY
def findMax2(A):
    if A is None or len(A) == 0:
        return None

    return _findMax(A, 0, len(A) - 1)


def _findMax(A, start, end):
    if start == end:
        return A[start]

    mid = (start + end) // 2
    max1 = _findMax(A, start, mid)
    max2 = _findMax(A, mid + 1, end)

    return max(max1, max2)

###############################################################################

# FIND THE LONGEST WORD
def longestWord(words):
    # Protection
    if words is None or len(words) == 0:
        return None

    # Base case
    if len(words) == 1:
        return words[0]

    # Recursive case
    # DIVIDE
    m = len(words) // 2
    part1 = words[0:m]
    part2 = words[m:]

    # CONQUER
    max1 = longestWord(part1)  # maximum in array part1
    max2 = longestWord(part2)  # maximum in array part2

    # COMBINE
    if len(max1) > len(max2):
        return max1
    else:
        return max2


A = ['john', 'adam', 'alexander', 'robert', 'gerard']
print("\nlongestWord({})={}".format(A, longestWord(A)))

###############################################################################

# RETURN THE NUMBER OF OCCURRENCES OF c IN s
def count(s, c):
    # Protection
    if s is None or len(s) == 0:
        return 0

    # Base case
    if len(s) == 1:
        if s[0] == c:
            return 1
        else:
            return 0

    # Recursive case
    # DIVIDE
    m = len(s) // 2
    part1 = s[0:m]
    part2 = s[m:]

    # CONQUER
    count1 = count(part1, c)  # number of c in part1
    count2 = count(part2, c)  # number of c in part2

    # COMBINE
    return count1 + count2

s = "memories"
print("\ncount({},{})={}".format(s, 'm', count(s, 'm')))

###############################################################################


# RETURN A LIST OF THE STRINGS WITH LENGTH <=2
def getWordsLength2(words):
    # Protection
    if words is None or len(words) == 0:
        return None

    # Base case
    if len(words) == 1:
        if len(words[0]) <= 2:
            return [words[0]]
        else:
            return []

    # Recursive case
    # DIVIDE
    m = len(words) // 2
    part1 = words[0:m]
    part2 = words[m:]

    # CONQUER
    words1 = getWordsLength2(part1)  # words with length <=2 in part1
    words2 = getWordsLength2(part2)  # words with length <=2 in part2

    # COMBINE
    return words1 + words2



words = ["the", "doctor", "arrived", "at", "the", "door", "of", "his", "home"]
print("\ngetWordsLength2({})  =\n    {}".format(words, getWordsLength2(words)))
