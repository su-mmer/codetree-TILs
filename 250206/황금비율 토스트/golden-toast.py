n, m = map(int, input().split())
buns = input()

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def push_front(self, new_data):
        new_node = Node(new_data)  # 새 노드 생성

        new_node.next = self.head  # 새 노드 next = self.head
        self.head.prev = new_node  # head.prev = new node
        
        new_node.prev = None  # 새 노드의 prev = None
        self.head = new_node  # self.head = 새 노드

    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)  # 새 노드 생성

            new_node.next = self.tail  # 새 노드 , tail 연결
            new_node.prev = self.tail.prev  # 새 노드 prev 연결

            self.tail.prev.next = new_node  # tail prev와 tail 사이에 new node 삽입
            self.tail.prev = new_node

    def insert (self, node, new_data):
        if node == self.end():
            self.push_back(new_data)

        elif node == self.begin():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)

            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
        
    def erase(self, node):
        next_node = node.next
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            # return next

        # elif node == self.end():
        #     return next_node
        
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            # return next_node
        return next_node

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

# DLL 생성, 값 할당
l = DoublyLinkedList()
for i in range(n):
    l.push_back(buns[i])

it = l.end()
for _ in range(m):
    s = input()
    if s[0] == "L" and it != l.begin():
        it = it.prev
    elif s[0] == "R" and it != l.end():
        it = it.next
    elif s[0] == "D" and it != l.end():
        it = l.erase(it)
    elif s[0] == "P":
        l.insert(it, s[2])
    
    # print("it: ", it.data)
    # i = l.begin()
    # while i != l.end():
    #     print(i.data)
    #     i = i.next

it = l.begin()
while it != l.end():
    print(it.data, end='')
    it = it.next