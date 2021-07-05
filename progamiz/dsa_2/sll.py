class node:
    def __init__(self,item):
        self.item=item
        self.next=None
class LL():
    def __init__(self):
        self.head=None
    #insertion in the begining
    def inst_front(self,item):
        new_node=node(item)
        new_node.next=self.head
        self.head=new_node
    #insertion in the middle(after a node)
    def inst_after(self,data):
        ite=int(input("enter the number after which node is inserted: "))
        new_node=node(data)
        temp_node=self.head
        if self.head==None:
            self.head=new_node
            self.head.next=None
            print("Linked list is empty\nNode is inserted at head position")
        else:
            while(temp_node.next):
                p=temp_node.item
                #print(type(p),type(ite),"the count of while loop : ",c)
                #c=c+1
                if(p==ite):
                    break
                temp_node=temp_node.next
            if(temp_node.next):
                new_node.next=temp_node.next
                temp_node.next=new_node
            else:
                print("Node being searched isn't present in the list\nso the given data is inserted at the end of list")
                temp_node.next=new_node
    def inst_end(self,item):
        new_node=node(item)
        if self.head is None:
            self.head = new_node
            return
        last =self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def printList(self):
        temp_node = self.head
        print("\nlinked list")
        while (temp_node):
            print(str(temp_node.item) + " ", end="")
            temp_node = temp_node.next
    def deleteNode(self, position):

        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        # If the key is not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next

if __name__=="__main__":
    l=LL()
    l.inst_front(5)
    l.printList()
    l.inst_front(6)
    l.printList()
    l.inst_end(1)
    l.printList()
    l.inst_end(3)
    l.printList()
    l.inst_after(66)
    l.printList()
    l.deleteNode(3)
    l.printList()

