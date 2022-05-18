class Calculator:
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def wrongAdd(self, a, b):
        return a + b/0

    def sumList(self,l):
        total = 0
        for i in l:
            total += i
        return total

    