#%%
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
        ## Complexity: O(1), because it always takes a vlue and inputs and done
    
    def length(self):
        return len(self.linkedlist)
        ## Complexity：O(1), because len() only assesses once
    
    def addNode(self,new_value):
        if isinstance(new_value.value, int) == True:
            self.linkedlist.append(new_value.value)
            return self.linkedlist
        else:
            return "You node should contain an integer."
        ## Complexity: O(1), because it only evaluates append() method once
    
    def addNodeAfter(self, new_value, after_node):
        position_to_add = self.linkedlist.index(after_node.value)
        self.linkedlist.insert(position_to_add+1, new_value.value)
        return self.linkedlist
        ## Complexity: O(1), because regardless of the length of the input,
        ## the insert() method is only evaluated once
    
    def addNodeBefore(self, new_value, after_node):
        position_to_add = self.linkedlist.index(after_node.value)
        self.linkedlist.insert(position_to_add, new_value.value)
        return self.linkedlist
        ## Complexity: O(1), with similar reasons above
    
    def removeNode(self, node_to_remove):
        try:
            self.linkedlist.remove(node_to_remove.value)
            return self.linkedlist
        except ValueError:
            return "You do not have this node in your list."
        ## Complexity: O(1), because the remove() method is only evaluted once
        
    def removeNodesbyValue(self, value):
        for elem in self.linkedlist:
            if elem == value:
                self.linkedlist.remove(value)
        return self.linkedlist
        ## Complexity: O(n), because the method loops over the linkedlist to
        ## decide which element to remove
        ## I think this is the least complex way? Without looping over the list,
        ## I will not know whether there is any element that can be matched.
            
    def reverse(self):
        self.linkedlist.reverse()
        return self.linkedlist
        ## Complexity: O(1), Straightforward
    
    def __str__(self):
        return "The linkedlist is %s" % " -> ".join([str(elem) for elem in self.linkedlist])
        ## Complexity: O(1), Straightforward
    



#%%
node_1 = Node(_value=1)
node_2 = Node(_value=2)
node_3 = Node(_value=3)
node_4 = Node(_value=4)
node_5 = Node(_value=5)
node_6 = Node(_value=6)
node_6_1 = Node(_value=6)
node_7 = Node(_value=7)

# Test
first_list = LinkedList(node_1)
first_list.addNode(node_2)
first_list.addNode(node_3)
first_list.addNodeAfter(node_4,node_1)
first_list.addNodeBefore(node_5,node_2)
first_list.addNodeBefore(node_6,node_4)
first_list.addNodeBefore(node_6_1,node_5)

first_list.length()
first_list.reverse()
first_list.removeNode(node_2)
first_list.removeNodesbyValue(6)
print(first_list)
