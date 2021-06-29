#function to heapify
def heapify(arr,n,i):
   #find largest among the roots 
   largest=i
   l=2*i+1
   r=2*i+2
   if l<n and arr[i]<arr[l]:
      largest=l
   if r<n and arr[largest]<arr[r]:
      largest=r
   #swap and continue if root is not largest
   if largest!=i:
      arr[i],arr[largest]=arr[largest],arr[i]
      heapify(arr,n,largest)
#function to insert an element into tree
def insert(array,new):
   size=len(array)
   if size==0:
      array.append(new)
   else:
      array.append(new)
      for i in range((size//2)-1,-1,-1):
         heapify(array,size,i)
#delete a node in tree:
def delete(array,num):
   size=len(array)
   i=0
   for i in range(0,size):
      if num == array[i]:
         break
   array[i],array[size-1]=array[size-1],array[i]
   array.remove(size-1)
   for i in range((len(array)//2)-1,-1,-1):
      heapify(array,len(array),i)
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

delete(arr, 4)
print("After deleting an element: " + str(arr))
