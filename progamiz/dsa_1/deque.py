class deq():
   def __init__(self):
      self.items=[]

   def isempty(self):
      return self.items==[]
   def addrear(self,ele):
      self.items.append(ele)
   def addfront(self,ele):
      self.items.insert(0,ele)
   def removefront(self):
      self.items.pop(0)
   def removerear(self):
      self.items.pop()
   def size(self):
      return(len(self.items))
   def display(self):
      print("\n------ARRAY--------")
      for i in self.items:
         
         print(i,end=" ")
d=deq()
print(d.isempty())
d.addrear(23)
d.display()
d.addfront(45)
d.display()
d.addfront(89)
d.display()
d.addrear(77)
d.display()
d.removefront()
d.display()
d.removefront()
d.display()
d.removerear()
d.display()
