# implmentation of iterative bst node class and bst tree class for MIT 6.006 ps3

class node(object):
    def __init__(self,value=None, left=None, right=None, parent=None):
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

        current = node(value=key,parent=p)

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
        if self.root is None:
            return None

    def delete(self, key):
        pass

    def predecessor(self, key):
        pass

    def successor(self, key):
        pass

    def find_min(self, node):
        pass

    def find_max(self, node):
        pass

    def rank(self, node):
        pass
    
    def bst_sort(self, node):
        if node is None:
            return
        self.bst_sort(node.left)
        print(node.value)
        self.bst_sort(node.right)
            

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
            label = str(node.value)
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

