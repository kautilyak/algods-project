# Name: Kautilya Kondragunta


from . import edge


class Node:
    def __init__(self, val: edge.Edge):
        self.val = val
        self.next = None #here value is the weight of the edge.


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, val: edge.Edge):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length = self.length + 1

    def insert(self, val: edge.Edge):
        newNode = Node(val)
        # Special case for the empty linked list 
        if self.head is None:
            newNode.next = self.head
            self.head = newNode
  
        # Special case for head at end
        elif self.head.val.destination.name >= newNode.val.destination.name:
            newNode.next = self.head
            self.head = newNode
  
        else :
  
            # Locate the node before the point of insertion
            current = self.head
            while(current.next is not None and current.next.val.destination.name < newNode.val.destination.name):
                current = current.next
              
            newNode.next = current.next
            current.next = newNode
        
    
    def deleteNode(self, key):
        current = self.head
        if self.head == None:
            return
        # If head node itself holds the key to be deleted
        if self.head.val == key:
            self.head = current.next
            current = None
            self.length -= 1
            return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while current != None:
            if current.val == key:
                break
            prev = current
            current = current.next
            # if key was not present in linked list
            if(current == None):
                return
 
            # Unlink the node from linked list
            prev.next = current.next
            self.length -= 1
    
            current = None

    # Get the value of node at position: pos
    def get(self, pos):
        if pos >= self.length:
            return None
        currentPos = 0
        currentNode = self.head
        while currentPos != pos:
            currentPos += 1
            currentNode = currentNode.next
        return currentNode
    
    # Print the list
    def print(self):
        currentNode = self.head
        list = []
        while currentNode != None:
            list.append(currentNode.val)
            currentNode = currentNode.next
        print(list)

