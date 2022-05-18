import time
a = time.time()
list1 = ["A", "B", "C", "D"]
for i in range(100000000):
    list1.append(i)
b = time.time()
print("The list has appended", len(list1), "elements in", b-a, "seconds")

a = time.time()
list1.pop(0)
b = time.time()
print("And it has taken %f seconds to remove the first item" % (b-a))
