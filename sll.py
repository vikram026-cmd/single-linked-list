class node: 
    def __init__(self,data): 
        self.data=data 
        self.next=None 
class sll: 
    def __init__(self): 
        self.head=None 
        self.tail=None 
    def create(self,data): 
        if(self.head==None): 
            self.head=node(data) 
            self.tail=self.head 
        else: 
            newnode=node(data) 
            self.tail.next=newnode 
            self.tail=newnode 
    def display(self): 
        temp=self.head 
        while(temp!=None): 
            print(temp.data,id(temp.next)) 
            temp=temp.next 
obj=sll() 
n=int(input()) 
for i in range(n): 
    m=int(input()) 
    obj.create(m) 
obj.display() 
