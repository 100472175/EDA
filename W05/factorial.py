import sys
sys.setrecursionlimit(100000)

def factorial(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# Ordenar una lista
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)

