class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self,head=None):
        self.head=head
        self.count=0
        
    def push(self,data):
        n=Node(data,self.head)
        self.head=n
        self.count +=1
        
    def isEmpty(self):
        return self.head==None
    
    def pop(self):
        if not self.isEmpty():
            self.head=self.head.next
            self.count -=1
        else:
            raise IndexError("Stack empty")
        
    def peek(self):
        if not self.isEmpty():
            return self.head.item
        else:
            raise IndexError("Stack empty")
     
    def size(self):
        return self.count

s1=Stack()
print("Size: ",s1.size())
s1.push(9)
s1.push(3)
s1.push(4)
s1.push(5)
print("Top element: ",s1.peek())
print("Size: ",s1.size())
s1.pop()
print("Size: ",s1.size())
s1.pop()
s1.pop()
s1.pop()
s1.pop()       
    