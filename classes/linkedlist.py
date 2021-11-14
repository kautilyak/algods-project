class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

    def push(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
    
    def pop(self):
        if self.length == 1 or self.length == 0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            currentNode = self.head
            while currentNode.next.val != self.tail.val:
                currentNode = currentNode.next
            self.tail == currentNode
            currentNode.next = None
            self.length -= 1

    def get(self, pos):
        if pos >= self.length:
            return None
        currentPos = 0
        currentNode = self.head
        while currentPos != pos:
            currentPos += 1
            currentNode = currentNode.next
        return currentNode