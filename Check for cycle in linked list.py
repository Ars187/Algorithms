#Check for cycle in the linked list 

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def Checkcycle(self):
        s=set()
        temp=self.head
        while(temp):
            # If we already have
            # this node in the hashmap it
            # means there is a cycle
            if (temp in s):
                return(True)
            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
            temp=temp.next
        return(False)
l=LinkedList()
l.push(10)
l.push(14)
l.push(15)
l.push(5)

#Cycle
l.head.next.next.next.next=l.head

if(l.Checkcycle()):
    print("Loop found") 
else:
    print("No Loop")
	
