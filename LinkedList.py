from Node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.length=0

    def size(self) -> int:
        return self.length

    def get(self,i:int) -> object: # returns the node at the given index
        current_node=None
        if i>=0 and i<self.length:
            if i<self.length//2:
                current_node=self.head
                for _ in range(i):
                    current_node=current_node.get_next()
            else: # makes it faster since you only have to go over half of the list in the worst case
                current_node=self.tail
                for _ in range(self.length-1,i,-1):
                    current_node=current_node.get_previous()
            return current_node

    def __getitem__(self,i:int) -> object: # returns the object inside the node at the given index and allows you to say list[0]
        if i>=0 and i<self.length:
            return self.get(i).get_data()
        
    def __setitem__(self,i:int,value:object) -> None:
        if i==self.length:
            self.add(value)
        elif i>=0 and i<self.length:
            self.get(i).set_data(value)
    
    def __iter__(self) -> object:
        for i in range(self.length):
            yield self[i]

    def add(self,object:object) -> None: # adds the inputted object to the end of the list in a new Node while updating tail
        if self.length==0: # update the heads if the list is empty
            node=Node(object)
            self.head=node
            self.tail=node
        else: # update the tail
            node=Node(object,None,self.tail) # class Node: __init__(data,next,previous) -> None:
            self.tail.set_next(node) 
            self.tail=node
        self.length+=1

    def insert(self,i:int,object:object) -> None: # adds the object anywhere specified into the list inside a Node and updates head and tail as needed
        if i>=0 and i<=self.length:
            if self.length==0:
                node=Node(object)
                self.head=node
                self.tail=node
            elif i==0:
                self.head=Node(object,self.head)
                self.head.get_next().set_previous(self.head)
            elif i==self.length:
                self.tail=Node(object,None,self.tail)
                self.tail.get_previous().set_next(self.tail)
            else:
                node_before=self.get(i-1)
                node_before.get_next().set_previous(Node(object,node_before.get_next(),node_before)) # Sets the Nodes next and previous in the constructor. Look at Node.py 
                node_before.set_next(node_before.get_next().get_previous())
            self.length+=1

    def delete(self,i:int) -> None: # removes the Node at the given index and updates head and tail as needed
        if self.length>0 and i>=0 and i<self.length:
            if self.length==1: # if we remove the last element, reset the list
                self.head=None
                self.tail=None
            elif i==0: # head edge case
                self.head=self.head.get_next()
                self.head.set_previous(None)
            elif i==self.length-1: # tail edge case
                self.tail=self.tail.get_previous()
                self.tail.set_next(None)
            else:
                node_before=self.get(i-1)
                node_before.set_next(node_before.get_next().get_next()) # delete it
                node_before.get_next().set_previous(node_before) 
            self.length-=1
    
    def find(self,node:Node,i:int=0) -> int: # returns the first index of the given Node starting at the inputted index with a default of 0
        current_node=self.head if i==0 else self.get(i) if i<=self.length else None
        while current_node is not None:
            if current_node==node:
                return i
            current_node=current_node.get_next()
            i+=1
        return -1

    def insert_after(self,after_this_val:object,val:object) -> bool:
        node_before=Node(after_this_val)
        i=self.find(node_before)
        found=True if i!=-1 else False
        while i!=-1: # while we still have Nodes we haven't inserted after, insert and find the next node
            self.insert(i+1,val) 
            i=self.find(node_before,i+2) # skip to the next occurence of this node
        return found

    def count(self,target:object) -> int:
        count=0
        node=Node(target)
        i=self.find(node)
        while i!=-1: # while we move more nodes in the list with data equal to target, update the count and move to the next
            count+=1
            i=self.find(node,i+1) # skip to the next occurence of this node
        return count

    def swap(self,i:int,j:int) -> bool:
        if i>=0 and j>=0 and i<self.length and j<self.length: # only run if they are in range
            i_node=self.get(i)
            j_node=self.get(j)
            temp_j_data=j_node.get_data() # perform the data swap
            j_node.set_data(i_node.get_data())
            i_node.set_data(temp_j_data)
            return True
        return False
        
    def move_to_front(self,target:object) -> None:
        node=Node(target)
        i=self.find(node)
        while i!=-1: # while there are more nodes with data equal to target, remove them and put them back in the front and then move onto the next one
            current_node=self.get(i)
            self.delete(i)
            self.insert(0,current_node.get_data())
            i=self.find(node,i+1)

    def remove_every_i(self,i:int) -> int:
        if i>0:
            count=0
            for j in range(i-1,self.length,i-1):
                self.delete(j)
                count+=1
            return count
    
    def remove_after(self,i:int,val:object) -> int:
        count=0
        node=Node(val)
        i=self.find(node,i) # find the first node after the inputted index
        while i!=-1: # while there are more nodes, delete them and update the count and next index
            self.delete(i) 
            count+=1
            i=self.find(node,i)
        return count
    
    def reflect(self) -> None:
        current_node=self.tail
        for _ in range(self.length): # add every node to the end of the list starting at the end and working down
            self.add(current_node.get_data()) # add a new node not pointing to anything and let the.add method update its pointers
            current_node=current_node.get_previous()
        
    def is_symmetric(self) -> bool: # check if the front and the back are the same all the way up to the middle
        front=self.head
        front_i=0
        back=self.tail
        back_i=self.length-1
        while back_i>front_i:
            if front!=back:
                return False
            front=front.get_next()
            back=back.get_previous()
            front_i+=1
            back_i-=1
        return True
    
    def replace(self,old_value,new_value) -> None:
        current_node=self.head
        while current_node is not None:
            if current_node.get_data()==old_value:
                current_node.set_data(new_value)
            current_node=current_node.get_next()

    def sort(self) -> None:
        for i in range(self.length-1,0,-1):
            self.bubble_once(i)

    def bubble_once(self,end:int) -> None : # swap up the largest value at an index prior or equal to the given index, to the given index
        if self.length>1:
            current_node=self.head.get_next()
            previous_node=self.head
            for i in range(1,end+1):
                if current_node.get_data()<previous_node.get_data():
                    temp=previous_node.get_data()
                    previous_node.set_data(current_node.get_data())
                    current_node.set_data(temp)
                # print(f'currently at Node: {i}')
                current_node=current_node.get_next()
                previous_node=previous_node.get_next()

    def __str__(self) -> str:
        as_string=''
        current=self.head
        while current is not None:
            as_string+=f'{str(current)},'
            current=current.next
        return f'[{as_string[:-1]}]'
    
if __name__=='__main__':
    linkedlist=LinkedList()
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(10)
    linkedlist.add(1)
    print(f'{linkedlist} {linkedlist.size()} | Should print [1,1,1,10,1] 5')
    linkedlist.insert(0,5)
    linkedlist.insert(linkedlist.size(),100)
    linkedlist.insert(3,10)
    print(f'{linkedlist} {linkedlist.size()} | Should print [5,1,1,10,1,10,1,100] 8')
    print(linkedlist.insert_after(1,3))
    print(linkedlist.insert_after(1111,5))
    print(f'{linkedlist} {linkedlist.size()} | Should print [5,1,3,1,3,10,1,3,10,1,3,100] 12')
    print(f'{linkedlist.count(1)} | Should print 4')
    print(linkedlist.swap(0,1))
    print(f'{linkedlist} {linkedlist.size()} | Should print [1,5,3,1,3,10,1,3,10,1,3,100] 12')
    print(linkedlist.swap(0,11))
    print(f'{linkedlist} {linkedlist.size()} | Should print [100,5,3,1,3,10,1,3,10,1,3,1] 12')
    linkedlist=LinkedList()
    linkedlist.add(10)
    linkedlist.add(20)
    linkedlist.add(30)
    linkedlist.add(40)
    print(f'{linkedlist} {linkedlist.size()} | Should print [10,20,30,40] 4')
    linkedlist.move_to_front(30)
    print(f'{linkedlist} {linkedlist.size()} | Should print [30,10,20,40] 4')
    print(linkedlist.remove_every_i(2))
    print(f'{linkedlist} {linkedlist.size()} | Should print [30,20] 2')
    linkedlist=LinkedList()
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(2)
    print(linkedlist.remove_after(2,1))
    print(f'{linkedlist} {linkedlist.size()} | Should print [1,1,2] 3')
    linkedlist.reflect()
    print(f'{linkedlist} {linkedlist.size()} | Should print [1,1,2,2,1,1] 6')
    print(f'{linkedlist.is_symmetric()} | Should print True')
    linkedlist.add(1)
    print(f'{linkedlist} {linkedlist.size()} | Should print [1,1,2,2,1,1,1] 7')
    print(f'{linkedlist.is_symmetric()} | Should print False')
    linkedlist=LinkedList()
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.replace(1,2)
    print(f'{linkedlist} {linkedlist.size()} | Should print [2,2,2,2] 4')
    linkedlist.add(-10)
    linkedlist.sort()
    print(f'{linkedlist} {linkedlist.size()} | Should print [-10,2,2,2,2] 5')
    linkedlist[0]=10
    print(f'{linkedlist} {linkedlist.size()} | Should print [10,2,2,2,2] 5')
    linkedlist[linkedlist.size()]=1
    print(f'{linkedlist.get(linkedlist.size()-1)} | Should print 1')