class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class Queue:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear 
        self.count=0
        
    def is_empty(self):
        return self.front==None
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        self.count +=1
        print("Enqueued Element: ",data)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.count==1:
            popped_val=self.front.item
            self.front=None
            self.rear=None
        else:
            popped_val=self.front.item
            self.front=self.front.next
        self.count -=1
        return popped_val
            
    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Front value: ",self.front.item)
    
    def get_rear(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Rear value: ",self.rear.item)
            
    def size(self):
        return self.count

q1=Queue()
print("Size: ",q1.size())
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
print("Size: ",q1.size())
print("Element Dequeued: ",q1.dequeue())
q1.get_front()
q1.get_rear()