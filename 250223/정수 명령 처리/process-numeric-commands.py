n = int(input())

class Stack:
    def __init__(self):
        self.items = []

    def push (self, item):
        self.items.append(item)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            temp = self.items[-1]
            self.items = self.items[:-1]
            return temp
    
    def size(self):
        return len(self.items)

    def empty(self):
        return 0 if self.size() else 1

    def top(self):
        return self.items[-1]

s = Stack()

for _ in range(n):
    command = input().split()
    # print(command[0])
    if command[0] == "push":
        # print(command[0], command[1])
        s.push(command[1])
    elif command[0] == "pop":
        print(s.pop())
    elif command[0] == "size":
        print(s.size())
    elif command[0] == "empty":
        print(s.empty())
    elif command[0] == "top":
        print(s.top())