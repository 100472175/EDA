# Exercise 1:

# Implement a recursive function taking two parameters _ a string s and a character c. The method returns the number of
# occurrences of c in s. The solution must be based in the divide and conquer strategy.

s = "abcdcccccccyfctfctfcfgc ftcecgccg"
c = 'c'


def count(s, c):
    if len(s) == 1 and s == c:
        return 1
    elif len(s) == 1 and s != c:
        return 0
    else:
        return count(s[len(s) // 2:], c) + count(s[:len(s) // 2], c)

def countHarib(s, c):
    if s is None or len(s) == 0:
        return 0
    m = len(s) // 2
    result = 0
    if s[m] == c:
        result += 1
    count1 = countHarib(s[:m], c)
    count2 = countHarib(s[m+1:], c)
    return result + count1 + count2


print(count(s, c))
print(countHarib(s, c))
#


# Exercise 2:
# Suppose that BST is a class thet implements a binart search tree. Wrrite a method that takes an ascenfin array of integers as a parameter and returns a pe