from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        if not self.empty():
            return self.dq.popleft()
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        return 0 if self.size() else 1

    def front(self):
        if not self.empty():
            return self.dq[0]

n = int(input())
que = Queue()

for _ in range(n):
    command = input()
    if command.startswith("push"):
        que.push(int(command.split()[1]))
    elif command == "pop":
        print(que.pop())
    elif command == "size":
        print(que.size())
    elif command == "empty":
        print(que.empty())
    elif command == "front":
        print(que.front())