class DoubleNode:
    def __init__(self, value=None, nextNode=None, prevNode=None):
        self.value=value
        self.nextNode=nextNode
        self.prevNode=prevNode
    
# Linked List, Addition to back, front and specific position, Deletion from back, front and specific position, printing

class DoubleLinkedList:
    def __init__(self, head=None):
        self.head=head

    
    #   Inserting to front of the LinkedList
    def Insert_to_front(self, value):
        new_node=DoubleNode(value)
        if self.head is None:
            self.head=new_node
            return
        
        new_node.nextNode=self.head   
        self.head.prevNode=new_node
        self.head=new_node

        '''
        -> New Node
        ______________________________
        |         |         |        |
        | PrevNode|  Value  |nextNode|
        |         |         |        |
        |_________|_________|________|

                        -> Self.head
                    ______________________________
                    |         |         |        |
                    | PrevNode|  Value  |nextNode|
                    |         |         |        |
                    |_________|_________|________|

                1) Pointing the newnode.nextNode to self.head
                2) Pointing the self.head.prevNode to the new Node so that it is linked
                3) Setting the newNode as the head node   self.head=newNode
        '''
        return


    # Insert to back
    def insert_to_back(self, value):
        '''
         -> Traversing and reaching the last Node, as setting currentNode=currentNode.nextNode, until currentNOde.nextNode becomes None
         ->Setting the newNode  to currentNode.nextNode
         -> Setting newNode.prevNode to currentNode
         -> Return

        ______________________________
        |         |         |        |
        | PrevNode|  Value  |None    |
        |         |         |        |
        |_________|_________|________|

                        -> New Node  
                    ______________________________
                    |         |         |        |
                    | PrevNode|  Value  |nextNode|
                    |         |         |        |
                    |_________|_________|________|
        '''
        new_node=DoubleNode(value)
        if self.head is None:
            self.head=new_node
            return
        
        # Finding the end position by traversing
        currentNode=self.head
        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode
        
        currentNode.nextNode=new_node
        new_node.prevNode=currentNode
        new_node.nextNode=None
        return

    # Inserting to specific Position
    def Insert_to_specific(self, value, position):
        new_node=DoubleNode(value)

        # If the list is empty and the position is set as 0
        if self.head is None and position ==0:
            self.head =new_node
            return

        # Looping until the position is reached, even check the condition that it does not crosses last element
        count=0
        currentNode=self.head
        while currentNode.nextNode is not None and count<position:
            currentNode=currentNode.nextNode
            count+=1
        
        new_node.nextNode=currentNode.nextNode
        new_node.prevNode=currentNode
        currentNode.nextNode=new_node
        if new_node.nextNode is not None:
            new_node.nextNode.prevNode=new_node
            return

        
    # Deleting the front node
    def delete_front(self):
        if self.head is None:
            return
        
        self.head=self.head.nextNode
        return
    
    # Deleting the last node
    def delete_last(self):
        if self.head is None:
            return
        
        currentNode=self.head
        while currentNode.nextNode.nextNode is not None:
            currentNode=currentNode.nextNode
        currentNode.nextNode=None
        return
        
    
    # Deleting a particular node
    def delete_specific(self, item):
        if self.head is None:
            return
        
        currentNode=self.head
        prev=None
        while currentNode.nextNode is not None and currentNode.value is not item:
            prev=currentNode
            currentNode=currentNode.nextNode
        
        print(prev.value)
        print(currentNode.value)
        prev.nextNode=currentNode.nextNode
        if currentNode.nextNode is not None:
            prev=currentNode.nextNode.prevNode
            return
        return
    # Printing data
    def Printing_list(self):
        if self.head is None: 
            return
        
        currentNode=self.head
        # Printing each value, running through the node till the end
        while currentNode is not None:
            print(currentNode.value,"-->",end="")
            currentNode=currentNode.nextNode
        return


d1=DoubleLinkedList()
d1.insert_to_back(10)       # 10-->
d1.insert_to_back(11)       # 10-->11-->
d1.insert_to_back(12)       # 10-->11-->12
d1.Insert_to_front(9)       # 9-->10-->11-->12
d1.Insert_to_front(7)       # 7-->9-->10-->11-->12
d1.Insert_to_specific(44,2) # 7-->9-->10-->44-->11-->12

d1.delete_front()   # 9-->10-->44-->11-->12
d1.delete_last()    # 9-->10-->44-->11
d1.delete_specific(44)
d1.Printing_list()

