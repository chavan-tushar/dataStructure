class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node    
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 
    
    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        else:
            temp = self.head
            pre = self.head
            while (temp.next is not None):
                pre = temp 
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -=1
            return temp
    
    def prepend(self,value):
        new_node = Node(value)
        self.length += 1
        if self.head is not None:
            temp = self.head
        self.head = new_node
        if temp is not None:
            self.head.next = temp
        return True
        
    
    def pop_first(self):
        temp = self.head
        self.length -= 1
        if self.length == 1:
            self.tail = self.head
            self.head.next = None
        elif self.length == 0:
            self.head = None
            self.tail = None 
        else:
            self.head = self.head.next
        
        return temp
    
    def get(self, index):
        if (self.length <= index or index < 0):
            return None
        elif index == 0:
            return self.head
        else:
            currentNode = self.head
            for _ in range(1, index+1):
                currentNode = currentNode.next
            return currentNode
        
    def set_value(self, index, value):
        if self.get(index):
            self.get(index).value = value
            return True
        else:
            return False
            
        
myLinkedList = LinkedList(4)
# myLinkedList.append(3)
# myLinkedList.append(31)
print(myLinkedList.set_value(-1,1))
# myLinkedList.print_list()
# myLinkedList.prepend(1)
# myLinkedList.prepend(110)
# myLinkedList.print_list()
# myLinkedList.pop_first()
myLinkedList.print_list()
# print(myLinkedList.get(1))
# print(myLinkedList.head.value)


{
    "value":4,
    "left":{
        "value":3,
        "left":None,
        "right":None
    },
    "right":{
        "value":23,
        "left":None,
        "right":None
    }
}