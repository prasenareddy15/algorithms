class cq:
   def __init__(self,k):
      self.le=k
      self.que=[None]*k
      self.front=self.rear=-1
   def enque(self,data):
      if((self.rear+1)%self.le==self.front):
         print("The circular queue is full\n")
      elif(self.front==-1):
         self.front=0
         self.tail=0
         self.que[self.rear]=data
      else:
         self.rear=(self.rear+1)%self.le
         self.que[self.tail]=data
   def deque(self):
      if(self.front==-1):
         print("the circular que is empty\n")
      elif(self.front==self.rear):
         temp=self.que[self.front]
         self.front=-1
         self.rear=-1
         return temp
      else:
         temp=self.que[self.front]
         self.front=(self.front+1)%self.le
         return temp
   def printcq(self):
      if(self.front==-1):
         print("NO element in circular queue")
      elif(self.rear>=self.front):
         for i in range(self.front,self.rear+1):
            print(self.que[i],end=" ")
         print()
      else:
         for i in range(self.front,self.le):
            print(self.que[i],end=" ")
         for i in range(0,self.rear+1):
            print(self.que[i],end=" ")
         print()
c=cq(5)
c.enque(1)
c.enque(2)
c.enque(3)
c.enque(4)
c.enque(5)
c.printcq()
c.deque()
c.printcq()
c.enque(6)
c.printcq()
c.deque()
c.enque(7)
c.printcq()

