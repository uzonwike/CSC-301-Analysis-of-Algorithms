class BSTnode:
    
    def __init__(self, parent, key, value):
        """Create a new leaf node with key 'key' and value 'value'."""
        self.key = key
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def add_word(self, key):
        if self.key is None:
            self.key = key
            self.value = 1
        elif self.key.upper() == key.upper():
            self.value += 1
        elif self.key.upper() < key.upper():
            if self.right is not None:
                self.right.add_word(key)
            else:
                self.right = BSTnode(self, key, 1)
        else:
            if self.left is not None:
                self.left.add_word(key)
            else:
                self.left = BSTnode(self, key, 1)

    def insertHelper(self, newNode):
        if self is None:
            self = newNode
        elif self.key < newNode.key:
            if self.right is not None:
                self.right.insertHelper(newNode)
            else:
                self.right = newNode
        else:
            if self.left is not None:
                self.left.insertHelper(newNode)
            else:
                self.left = newNode
    
    def insert (self, key, value):
        newNode = BSTnode(None, key, value)
        self.insertHelper(newNode);

    def lookup(self, key, parent=None):
        """
        Lookup node with given key
        
        @returns node and node's parent if found or None, None
        """
        if key < self.key:
            if self.left is None:
                return None, None
            return self.left.lookup(key, self)
        elif key > self.key:
            if self.right is None:
                return None, None
            return self.right.lookup(key, self)
        else:
            return self, parent
    
    def delete(self, key):
        node, parent = self.lookup(key)

        
        node, parent = self.lookup(key)
        if node is not None:
            #Case 1: if node has no children
            if node.left is None and node.right is None:
                if parent is not None:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.value = None
            #Case 2: if node has one child
            if not (node.left is not None and node.right is not None):
                if node.right is None:
                    temp = node.left
                else:
                    temp = node.right
                if parent is not None:
                    if parent.left is node:
                        parent.left = temp
                    else:
                        parent.right = temp
                    del node
                else:
                    self.left = temp.left
                    self.right = temp.right
                    self.key = temp.key
                    self.value = temp.value
            #Case 3: if node has two children
            else:
                #find its successor
                parent = node
                successor = node.right
                while successor.left is not None:
                    parent = successor
                    successor = successor.left
                # replace node's key and value by its successor's key and value
                node.key = successor.key
                node.value = successor.value
                # fix successor's parent's child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                

    def minimum (self):
        if self.left is None:
            return self
        else:
            return self.left.minimum()
    def maximum (self):
        if self.right is None:
            return self
        else:
            return self.right.maximum()

    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print [self.key, self.value]
        if self.right:
            self.right.print_tree()
