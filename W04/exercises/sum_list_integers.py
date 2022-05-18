import time

start = time.time()
l = []
for i in range(10000000):
    l.append(i)
end = time.time()
print(end - start)


def sumList(l):
    start = time.time()
    addition = 0
    for i in l:
        addition += i
    end = time.time()
    print(end - start)


sumList(l)
