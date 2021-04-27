# File: tree.py
# Date: April 27, 2021
# Author: COMP 120
# Description: Contains basic tree class,
#        with traversal methods.  The code
#        here is for a general tree, where
#        each node can have any number of children.

from collections import deque

class TreeNode:
    """ Stores one node of a general tree."""
    def __init__(self, val):
        """ 
        Initialize the node with a value,
        and no children.
        """
        self.val = val
        self.children = []

    def __str__(self):
        """ 
        Returns string representation of the node,
        with just the value stored in the node.
        """
        return str(self.val)

    def add_children(self, new_children):
        """
        Adds the nodes in the children parameter
        to the list of children for the node.
        """
        self.children.extend(new_children)

class Tree:
    """ 
    Stores a general tree, where each node
    can have any number of children.
    """

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
        # you will write this method
        pass

    def depth_first(self):
        """ 
        Perform depth-first traversal
        of the tree, starting at the root.
        """
        if self.root != None:
            self.depth_first_recursive(self.root)

    def depth_first_recursive(self, node):
        """
        Perform depth-first traversal of the 
        subtree rooted at the parameter node.
        """
        print(node)
        for child in node.children:
            self.depth_first_recursive(child)

    def num_leaf_nodes(self):
        """ Returns number of leaf nodes in tree. """
        if self.root == None:
            return 0
        else:
            return self.num_leaf_nodes_recursive(self.root)

    def num_leaf_nodes_recursive(self, subtree_root):
        """ 
        Returns number of leaf nodes in tree
        rooted at subtree_root.
        """
        if len(subtree_root.children) == 0:
            return 1
        else:
            count = 0
            for child in subtree_root.children:
                count += self.num_leaf_nodes_recursive(child)

            return count

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
    # Create a tree
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")
    g = TreeNode("g")
    h = TreeNode("h")
    i = TreeNode("i")
    j = TreeNode("j")
    k = TreeNode("k")
    l = TreeNode("l")
    m = TreeNode("m")
    j.add_children([k, l, m])
    h.add_children([j])
    e.add_children([h, i])
    c.add_children([e,f])
    d.add_children([g])
    a.add_children([b, c, d])
    tree = Tree(a)

    print("Testing breadth-first traversal")
    print("Should print a, b, c, d, e, f, g, h, i, j, k, l, m")
    tree.breadth_first()

    print("\nTesting depth-first traversal")
    print("Should print a, b, c, e, h, j, k, l, m, i, f, d, g")
    tree.depth_first()

    print("\nTesting num_leaf_nodes() method")
    print("Should print 7")
    print("num leaf nodes=", tree.num_leaf_nodes())

    print("\nTesting depth() method")
    print("Should print 5")
    print("Tree depth =", tree.depth())