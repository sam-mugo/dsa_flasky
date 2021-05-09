class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        
    def to_list(self):
        users_arr = []
        if self.head is None:
            return users_arr
        
        node = self.head
        while node:
            users_arr.append(node.data)
            node = node.next_node
        return users_arr
        
        
    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
            
            
        ll_string += " None"
        print(ll_string)
    
    def insert_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.last_node = self.head
        
     
    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        
        
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
        
        
        
        
