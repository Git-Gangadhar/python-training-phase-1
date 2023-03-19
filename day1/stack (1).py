"""class stack:
    arr=[]
    size=5
    def push(self,element):
        
        if len(self.arr)==self.size:
            print("stack is full")
        else:
            self.arr.append(element)
            
    def pop(self):
        if len(self.arr)==0:
            print("underflow condition")
        else:
            self.arr.pop()
    def stack_peek(self):
        if len(self.arr)==0:
            print("stack is empty")
        else:
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=stack()
s.push(6)
s.push(26)
s.push(63)
s.push(66)
s.push(68)
s.push(77)
print(s.arr)
s.pop()
s.pop()#removes the last element in the stack
print(s.arr)
print(s.stack_peek())##returns the top element in the stack 


##problem

class stack:
    arr=[]
    size=5
    def s_push(self,element):
        
        if len(self.arr)==self.size:
            print("stack is full")
        else:
            self.arr.append(element)
            
    def s_pop(self):
        if len(self.arr)==0:
            print("underflow condition")
        else:
            return self.arr.pop()
    def stack_peek(self):
        if len(self.arr)==0:
            print("stack is empty")
        else:
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=stack()
s1=stack()
s.s_push(6)
s.s_push(26)
s.s_push(63)
s.s_push(66)
s.s_push(68)
print("s: ",s.arr)
s1.s_push(s.s_pop())
s1.s_push(s.s_pop())
s1.s_push(s.s_pop())
s1.s_push(s.s_pop())
print("s: ",s.arr)
s1.s_push(s.s_pop())
print("s1: ",s1.arr)  
### implementing queue


class queue:
    arr=[]
    size=5
    def enqueue(self,element):
        
        if len(self.arr)==self.size:
            print("queue is full")
        else:
            self.arr.append(element)
            
    def dequeue(self):
        if len(self.arr)==0:
            print("underflow condition")
        else:
            return self.arr.pop()
    def queue_peep(self):
        if len(self.arr)==0:
            print("queue is empty")
        else:
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=queue()

s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)

print("s: ",s.arr)
s.dequeue()
s.dequeue()
s.dequeue()
print(s.arr) """

"""##implementing the functionality of stack using queues lifo


class queue:
    arr=[]
    size=5
    def enqueue(self,element):
        
        if len(self.arr)==self.size:
            print("queue is full")
        else:
            self.arr.append(element)
            
    def dequeue(self):
        if len(self.arr)==0:
            print("underflow condition")
        else:
            return self.arr.pop()
    def queue_peep(self):
        if len(self.arr)==0:
            print("queue is empty")
        else:
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
    def push(self,element):
        
        if len(self.arr)==self.size:
            print("stack is full")
        else:
            self.arr.append(element)
    
s=queue()
s1=queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
print(s.arr)
s1.push(s.dequeue())
s1.push(s.dequeue())
s1.push(s.dequeue())
s1.push(s.dequeue())
s1.push(s.dequeue())
print("s:", s1.arr)
s1.enqueue(s.dequeue())
s1.enqueue(s.dequeue())
s1.enqueue(s.dequeue())
s1.enqueue(s.dequeue())
s1.enqueue(s.dequeue())
print(s1.arr)
"""
"""

class queue:
    def __init__(self):
        self.temp=[]
        self.original=[]
    
    def enqueue(self,element):
        self.temp.append(pop_ele)
        
        while len(self.arr)!=0:
            pop_ele=self.temp.pop(0)
            self.temp.append(pop_ele)
            
    def dequeue(self):
        return self.original.pop(0)
    def printqueue(self):
        print("temp:", self.temp)

        print("original: ",self.original)  """
"""arr=[1,2,3,4]
key=int(input())
for i in range(len(arr)):
    if arr[i]==key:
        print("key found at ",i)

    """
"""time complexity is calculated based on iterations

n=10
for (i=0;i<n;i++){
for (i=0;i<n/2;i++){
}
i=n
j=n/2
big o O(n)*O(n/2)== n^2/2  neglect constants so time complexity is n^2   MASTERS THEORM"""


##binary search

def binary(arr,low,high,key):
    while low <=high:
        mid=(low+high)//2
        if arr[mid]==key:
            print("found: ",mid)
            
            return 
        elif key< arr[mid]:
            high=mid-1
            return binary(arr,low,high,key)
        elif key> arr[mid]:
            low=mid+1
            return binary(arr,low,high,key)

arr=[i for i in range(1,11^77)]
key=int(input())
low=0
high=len(arr)-1
binary(arr,low,high,key)

##reverse the first half of stack and queue


           
            

        

    













