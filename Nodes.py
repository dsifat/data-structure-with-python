class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

x1=Node("Sun")
x2=Node("Mon")
x3=Node("Tue")
x1.next=x2
x2.next=x3

