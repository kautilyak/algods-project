class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.length = self.length + 1
            
    def RemoveNode(self, Removekey):
        head = self.head
         
        if (head is not None):
            if (head.val == Removekey):
                self.head = head.next
                HeadVal = None
                return
        while (head is not None):
            if head.val == Removekey:
                break
            prev = head
            head = head.next

        if (head == None):
            return

        prev.next = head.next
        HeadVal = None

    #def pop(self):
    #    self.print()
    #    print(self.head.next.val)
    #    currentNode = self.head
    #    if self.length == 1 or self.length == 0:
    #        self.head = None
    #        self.tail = None
    #        self.length = 0
    #    else:
    #        
    #        while currentNode.next != self.tail:
    #            currentNode = currentNode.next
    #       
    #        self.tail == currentNode
    #        currentNode.next = None
    #        self.tail.next = None
    #        self.length = self.length - 1

    def get(self, pos):
        if pos >= self.length:
            return None
        currentPos = 0
        currentNode = self.head
        while currentPos != pos:
            currentPos += 1
            currentNode = currentNode.next
        return currentNode
    
    def print(self):
        currentNode = self.head
        list = []
        while currentNode != None:
            list.append(currentNode.val)
            currentNode = currentNode.next
        print(list)

