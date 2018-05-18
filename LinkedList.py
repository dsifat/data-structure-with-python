class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.headvalue=None

    def traverse(self):
        temp=self.headvalue
        while temp != None:
            print(temp.value)
            temp=temp.next

x1=Node("Sun")
x2=Node("Mon")
x3=Node("Tue")
x1.next=x2
x2.next=x3

list=LinkedList()
list.headvalue=x1
list.traverse()