class queue:
   def __init__(self):
      self.que=[]
   #add tge element
   def enque(self,ele):
      self.que.append(ele)
   def deque(self):
      if len(self.que)<1:
         return(None)
      return(self.que.pop(0))
   def display(self):
      print(self.que)
   def size(self):
      return(len(self.que))
q = queue()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)

q.display()

q.deque()

print("After removing an element")
q.display()
