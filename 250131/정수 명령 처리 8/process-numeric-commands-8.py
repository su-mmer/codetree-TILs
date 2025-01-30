n = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node

        else:
            self.head = new_node
            self.tail = new_node
        
        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.tail = new_node
            self.head = new_node

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print("List is Empty")

        elif self.size() == 1:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num -= 1

            return temp.data

        else:
            temp = self.head

            self.head = self.head.next
            self.head.prev = None
            self.node_num -= 1

            return temp.data

    def pop_back(self):
        if self.tail == None:
            print("List is Empty")

        elif self.size() == 1:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num -= 1

            return temp.data

        else:
            temp = self.tail

            self.tail = self.tail.prev
            self.tail.next = None
            self.node_num -= 1

            return temp.data           

    def size(self):
        return self.node_num

    def empty(self):
        return 1 if self.node_num == 0 else 0
    
    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data

dll = DoublyLinkedList()

for _ in range(n):
    command = input().split()

    if command[0] == "push_front":
        dll.push_front(int(command[1]))
    elif command[0] == "push_back":
        dll.push_back(int(command[1]))
    elif command[0] == "pop_front":
        print(dll.pop_front())
    elif command[0] == "pop_back":
        print(dll.pop_back())
    elif command[0] == "size":
        print(dll.size())
    elif command[0] == "empty":
        print(dll.empty())
    elif command[0] == "front":
        print(dll.front())
    elif command[0] == "back":
        print(dll.back())