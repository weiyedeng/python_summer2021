#%%
import os
from datetime import datetime
import time
import random

# Create the node class
class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)

# Create the LinkedList class
# Note: Only allow inputting a Node class - Just to keep consistency
# Alterntively, codes can be also changed to accomodate inputs of pure values
class LinkedList:     
    def __init__(self, initial_value):
        self.value = initial_value
        self.linkedlist = [initial_value.value]
    
    def length(self):
        return len(self.linkedlist)
    
    def addNode(self,new_value):
        if isinstance(new_value.value, int) == True:
            self.linkedlist.append(new_value.value)
            return self.linkedlist
        else:
            return "You node should contain an integer."
    
    def addNodeAfter(self, new_value, after_node):
        position_to_add = self.linkedlist.index(after_node.value)
        self.linkedlist.insert(position_to_add+1, new_value.value)
        return self.linkedlist
    
    def addNodeBefore(self, new_value, after_node):
        position_to_add = self.linkedlist.index(after_node.value)
        self.linkedlist.insert(position_to_add, new_value.value)
        return self.linkedlist
    
    def removeNode(self, node_to_remove):
        try:
            return self.linkedlist.remove(node_to_remove.value)
        except ValueError:
            return "You do not have this node in your list."
    
    def reverse(self):
        return self.linkedlist.reverse()
    
    def __str__(self):
        return "The linkedlist is %s" % " -> ".join([str(elem) for elem in self.linkedlist])

    


#%%
node_1 = Node(_value=1)
node_2 = Node(_value=5)
node_3 = Node(_value=9)
node_4 = Node(_value=6)
node_5 = Node(_value=7)

# Test
first_list = LinkedList(node_1)
first_list.addNode(node_2)
first_list.addNode(node_3)
first_list.addNodeAfter(node_4,node_1)
first_list.addNodeBefore(node_5,node_2)

first_list.length()
first_list.reverse()
first_list.removeNode(node_2)
print(first_list)
