# implmentation of iterative bst node class and bst tree class for MIT 6.006 ps3

class node(object):
    def __init__(self, value = None, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.tree_size = 0
        self.height = 0

    def __str__(self):
        return str(self.value)

class bst(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = node(value=key)
            self.root.height = 0
            self.root.tree_size = 1
            return self.root

        current = self.root
        p = None

        while current is not None:
            p = current
            if key is current.value:
                return None
            elif key < current.value:
                current  = current.left
            else:
                current  = current.right

        current = node(value=key, parent=p)

        if key < p.value:
            p.left = current
        else:
            p.right = current

        x = current

        while current is not None:
            self.update_node_height(current)
            self.update_node_tree_size(current)
            current = current.parent

        return x
            
    def find(self, key):
        current = self.root
        parent = None
        
        while current is not None and key is not current.value:
            parent = current
            
            if key < current.value:
                current = current.left
            else:
                current = current.right

        return current, parent

    def delete(self, key):
        node, _ = self.find(key)
        
        # Empty tree
        if node is None:
            return None
        
        current = None
        
        # If to be deleted is root
        if node is self.root:
            if node.left is None:
                self.root = node.right
                node.right = None
                
                if self.root:
                    self.root.parent = None
            
            elif node.right is None:
                self.root = node.left
                node.left = None
                self.root.parent = None
                
            else:
                successor = self.successor(node)
                current = successor.parent
                
                if successor is node.right:
                    self.root = node.right
                    successor.left = node.left
                    successor.parent = None
                    node.left = None
                    node.right = None
                    current = self.root
                    
                elif successor.right is None:
                    self.root = successor
                    successor.left = node.left
                    successor.right = node.right
                    current.left = None
                    successor.parent = None
                    node.left = None
                    node.right = None
                    
                else:
                    self.root = successor
                    current.left = successor.right
                    successor.left = node.left
                    successor.right = node.right
                    successor.parent = None
                    node.left = None
                    node.right = None

                while current is not None:
                    self.update_node_height(current)
                    self.update_node_tree_size(current)
                    current = current.parent
                    
            return node
        
        # If to be deleted is left child
        if node is node.parent.left:
            if node.left is None:
                current = node.parent
                current.left = node.right
                
                if node.right:
                    node.right.parent = node.parent
                    node.right = None

                node.parent = None
            
            elif node.right is None:
                current = node.parent
                current.left = node.left
                node.left.parent = node.parent
                node.left = None
                node.parent = None
                
            else:
                successor = self.successor(node)
                current = successor.parent
                
                if successor is node.right:
                    node.parent.left = successor
                    successor.left = node.left
                    successor.parent = node.parent
                    current = successor
                    node.left = None
                    node.right = None
                    node.parent = None
                    
                elif successor.right is None:
                    node.parent.left = successor
                    successor.left = node.left
                    successor.right = node.right
                    successor.left.parent = successor
                    successor.right.parent = successor
                    successor.parent = node.parent
                    current.left = None
                    node.left = None
                    node.right = None
                    node.parent = None
                    
                else:
                    node.parent.left = successor
                    current.left = successor.right
                    successor.right.parent = current
                    successor.left = node.left
                    successor.right = node.right
                    successor.left.parent = successor
                    successor.right.parent = successor
                    successor.parent = node.parent
                    node.left = None
                    node.right = None
                    node.parent = None
  
        # If to be deleted is right child
        else:
            if node.left is None:
                current = node.parent
                current.right = node.right
                
                if node.right:
                    node.right.parent = node.parent
                    node.right = None

                node.parent = None
            
            elif node.right is None:
                current = node.parent
                current.right = node.left
                node.left.parent = node.parent
                node.left = None
                node.parent = None
                
            else:
                successor = self.successor(node)
                current = successor.parent
                
                if successor is node.right:
                    node.parent.right = successor
                    successor.left = node.left
                    successor.parent = node.parent
                    current = successor
                    node.left = None
                    node.right = None
                    node.parent = None
                    
                elif successor.right is None:
                    node.parent.right = successor
                    successor.left = node.left
                    successor.right = node.right
                    successor.left.parent = successor
                    successor.right.parent = successor
                    successor.parent = node.parent
                    current.left = None
                    node.left = None
                    node.right = None
                    node.parent = None
                    
                else:
                    node.parent.right = successor
                    current.left = successor.right
                    successor.right.parent = current
                    successor.left = node.left
                    successor.right = node.right
                    successor.left.parent = successor
                    successor.right.parent = successor
                    successor.parent = node.parent
                    node.left = None
                    node.right = None
                    node.parent = None
                    
        while current is not None:
            self.update_node_height(current)
            self.update_node_tree_size(current)
            current = current.parent
                    
        return node
            
    def predecessor(self, node):
        if not node:
            return node
        
        if node.left:
            return self.find_max(node.left)
        
        while node.parent is not None and node.parent.right is not node:
            node = node.parent
            
        return node.parent

    def successor(self, node):
        if not node:
            return node
        
        if node.right:
            return self.find_min(node.right)
        
        while node.parent is not None and node.parent.left is not node:
            node = node.parent
            
        return node.parent

    def find_min(self, node):
        if node is None:
            return None

        while node.left:
            node = node.left

        return node

    def find_max(self, node):
        if node is None:
            return None

        while node.right:
            node = node.right

        return node

    def rank(self, key):
        node, parent = self.find(key)
        
        if node is None and parent is None:
            return None
        
        elif node is None:
            if key > parent.value:
                node = parent
                x = self.successor(parent)
                
                while x is not None and key > x.value:
                    node = x
                    x = self.successor(x)
                    
                if x is not None and key > x.value:
                    node = x
            
            else:
                node = parent
                x = self.predecessor(parent)
                
                while x is not None and key < x.value:
                    node = x
                    x = self.predecessor(x)
                    
                if x is not None:
                    node = x
                
                else:
                    return 0

        r = 1
        
        if node.left:
            r += node.left.tree_size
        
        while node.parent:
            if node is node.parent.right:
                r += 1
                
                if node.parent.left:
                    r += node.parent.left.tree_size
            
            node = node.parent
            
        return r

    def bst_sort(self, node, A):
        if node is None:
            return
        self.bst_sort(node.left, A)
        A.append(node.value)
        self.bst_sort(node.right, A)
            
    def node_height(self, node):
        if node is None:
            return -1
        
        return node.height

    def node_tree_size(self, node):
        if node is None:
            return 0

        return node.tree_size

    def update_node_height(self, node):
        node.height =  1 + max(self.node_height(node.left), self.node_height(node.right))

    def update_node_tree_size(self, node):
        node.tree_size = 1 + self.node_tree_size(node.left) + self.node_tree_size(node.right)

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        def recurse(node):
            if node is None:
                return [], 0, 0
            label = str(node.height)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

