# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, element):
        self.stack1.append(element)
                
    def dequeue(self):
        if(not self.stack1):
            self.stack2.pop()
        elif(not self.stack2):
            self.remove()
        else:
            self.stack2.pop()
        
        
    def remove(self):
        while(len(self.stack1) > 1):
            self.stack2.append(self.stack1.pop())
        self.stack1.pop()
                
    def front(self):
        if(self.stack1):
            if(self.stack2):
                print(self.stack2[-1])
            else:
                print(self.stack1[0])        
        elif(self.stack2):
            print(self.stack2[-1])


        
q = int(input())
queue = Queue()
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        queue.enqueue(query[1])
    elif query[0] == 2:
        queue.dequeue()
    else:
        queue.front()

