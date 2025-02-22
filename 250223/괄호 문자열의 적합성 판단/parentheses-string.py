arr = input()

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.empty():
            return False
        else:
            self.items.pop()
            return True

    def size(self):
        return len(self.items)

    def empty(self):
        return False if self.size() else True

s = Stack()

for i in arr:
    if i == "(":
        s.push(i)
    else:
        if not s.pop():
            break

# print(s.size())
print("Yes") if s.empty() else print("No")