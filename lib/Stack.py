class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit


        for item in items:
            if not self.full():
                self.items.append(item)

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def push(self, item):
        if self.full():
            return self.items
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            return self.items.pop()
        return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() >= self.limit:
            return True
        else:
            return False


    def search(self, target):
        for i in range(len(self.items)):
            back = len(self.items) -1 - i
            if self.items[i] == target:
                return back
        return -1


stack = Stack([1,2,3,4,5,6,7,8])
# print(stack.pop())
print(stack.full())
print(stack.search(9))