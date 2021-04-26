# File: binarytree.py
# Date: April 27, 2021
# Author: COMP 120
# Description: Contains binary tree class,
#        with traversal methods.  

from collections import deque

class BinaryTreeNode:
    def __init__(self, val, left = None, right = None):
        """ 
        Initialize the node with a value,
        with left child from the parameter left 
        and the right child from the parameter right.
        """
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """ 
        Returns string representation of the node,
        with just the value stored in the node.
        """
        return str(self.val)

class BinaryTree:
    def __init__(self, root = None):
        """ 
        Initialize the root of the tree
        from the parameter root.
        """
        self.root = root

    def breadth_first(self):
        """ 
        Performs breadth-first traversal
        of the tree, printing out the value
        stored in each node.
        """
        # Initialize a queue of nodes with the root
        queue = deque()
        if self.root != None:
            queue.append(self.root)

        while len(queue) > 0:
            # Dequeue a node.
            node = queue.popleft()
            # Print it out
            print(node)
            # Enqueue its children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def depth_first(self):
        """ 
        Perform depth-first traversal
        of the tree, starting at the root.
        """
        # you will write the body of this method
        pass

    def depth_first_recursive(self, node):
        """
        Perform depth-first traversal of the 
        subtree rooted at the parameter node.
        """
        # you will write the body of this method.
        pass


    def num_leaf_nodes(self):
        """ Returns number of leaf nodes in tree. """
        
        # you will write the body of this method
        pass

    def num_leaf_nodes_recursive(self, subtree_root):
        """ 
        Returns number of leaf nodes in tree
        rooted at subtree_root.
        """
        
        # you will write the body of this method
        pass

    def depth(self):
        """ Returns depth of the tree. """
        
        # you will write this method
        pass

    def depth_recursive(self, subtree_root):
        """ 
        Returns number of leaf nodes in tree
        rooted at subtree_root.
        """
        # you will write this method
        pass

if __name__ == "__main__":
    # Create tree nodes
    d = BinaryTreeNode('d')
    g = BinaryTreeNode('g')
    j = BinaryTreeNode('j')
    k = BinaryTreeNode('k')
    m = BinaryTreeNode('m')
    h = BinaryTreeNode('h', j, k)
    l = BinaryTreeNode('l', None, m)
    i = BinaryTreeNode('i', None, l)
    e = BinaryTreeNode('e', g, h)
    f = BinaryTreeNode('f', None, i)
    b = BinaryTreeNode('b', d, e)
    c = BinaryTreeNode('c', f)
    a = BinaryTreeNode('a', b, c)

    # Create tree
    tree = BinaryTree(a)

    print("Testing breadth-first traversal")
    print("Should print a, b, c, d, e, f, g, h, i, j, k, l, m")
    tree.breadth_first()

    print("\nTesting depth-first traversal")
    print("Should print a, b, d, e, g, h, j, k, c, f, i, l, m")
    tree.depth_first()

    print("\nTesting num_leaf_nodes() method")
    print("Should print 5")
    print("num leaf nodes=", tree.num_leaf_nodes())

    print("\nTesting depth() method")
    print("Should print 5")
    print("Tree depth =", tree.depth())