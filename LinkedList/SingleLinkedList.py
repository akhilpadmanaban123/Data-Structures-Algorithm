class SingleNode:
    def __init__(self, value=None, nextNode=None):
        self.value= value
        self.nextNode=nextNode
    


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = None
    


    # Inserting to Front
    def Inserting_to_front(self, value):
        new_node=SingleNode(value)
        if self.head is None:
            self.head= new_node
            return
        
        new_node.nextNode=self.head
        self.head=new_node
        return

    
    #   Inserting to back of the linked list
    def Insert_to_back(self, value):
        new_node=SingleNode(value)
        if self.head is None:
            self.head = new_node
            return
        
        currentNode=self.head
        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode
        
        currentNode.nextNode=new_node
        new_node.nextNode=None
        return

    
    #   Inserting to a specific position
    def Insert_to_specific(self, value, position):
        new_node=SingleNode(value)
        if self.head is None:
            self.head=new_node
            return
        
        currentNode=self.head
        count=0 #   TO reach the position
        while currentNode.nextNode is not None and count<position:
            count+=1
            currentNode=currentNode.nextNode
        
        new_node.nextNode=currentNode.nextNode
        currentNode.nextNode=new_node
        return

    #   Deleting from front
    def delete_front(self):
        if self.head is None:
            print("Linked List is empty..")
            return
        
        self.head=self.head.nextNode
        return
    
    # Deleting from back
    def delete_back(self):
        if self.head is None:
            print("Linked list is empty...")
            return
        currentNode=self.head
        while currentNode.nextNode.nextNode is not None:
            currentNode=currentNode.nextNode
        
        currentNode.nextNode=None
        return

    #   Deleting a specific element
    def delete_specific(self, value):
        if self.head is None:
            print("Linked list is empty...")
            return
        
        currentNode=self.head
        prev=None
        while currentNode.nextNode is not None and currentNode.value is not value:
            prev=currentNode
            currentNode=currentNode.nextNode
        
        prev.nextNode=currentNode.nextNode
        return


    # Printing data
    def printing_data(self):
        if self.head is None:
            return
        
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.value,"-->",end="")
            currentNode=currentNode.nextNode
        return


s1=SingleLinkedList()
s1.Insert_to_back(10)
s1.Insert_to_back(12)
s1.Insert_to_back(13)
s1.Inserting_to_front(9)
s1.Inserting_to_front(7)
s1.Inserting_to_front(5)
s1.Insert_to_specific(21,3)
s1.Insert_to_specific(33,6)
s1.delete_back()
s1.delete_front()
s1.delete_specific(10)
s1.printing_data()
