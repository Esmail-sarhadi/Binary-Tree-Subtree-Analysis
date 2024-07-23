class Node:
    """
    This class represents a node in a binary tree. Each node can hold a value
    and has references to its parent, left child, and right child.
    """
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent  # Reference to the parent node. Needed to trace the path to the root.
        self.left_child = None
        self.right_child = None

def create_tree(values):
    """
    This function constructs a binary tree from a list of values. The values are processed in reverse order.
    The root is represented by '*', and each '+' indicates the presence of two child nodes (left and right).
    Values are assigned to leaf nodes, while internal nodes are represented by '+'.
    """
    current_node = None  # The node currently being processed; initially, this is the root.
    empty_spots = []  # A list used to keep track of nodes waiting to be filled with child nodes.
    
    for x in reversed(values):  # Start constructing the tree from the end of the list.
        if x == '*':
            root = Node()  # Create the root node.
            current_node = root
        elif x == '+':
            current_node.left_child = Node(None, current_node)
            current_node.right_child = Node(None, current_node)
            empty_spots.append(current_node.left_child)  # Add the left child to the list of empty spots.
            current_node = current_node.right_child  # Move to the right child for further processing.
        else:
            current_node.value = int(x)  # Assign the value to the current node (leaf node).
            if len(empty_spots) > 0:
                current_node = empty_spots.pop()  # Get the next node from the list of empty spots.
    
    return root

def divide_and_conquer(node):
    """
    This function uses the divide-and-conquer approach to find the maximum sum of a subtree in the binary tree.
    It recursively calculates the maximum sum and maximum node for both left and right subtrees and determines
    the maximum value among them.
    """
    if node.left_child is None and node.right_child is None:
        # Base case: If the node is a leaf, its maximum sum is its value and the maximum node is itself.
        return node.value, node.value, node
    else:
        # Recursively find the maximum sum and node for the left and right subtrees.
        max_of_left_subtree, sum_of_left_subtree, max_node_of_left_subtree = divide_and_conquer(node.left_child)
        max_of_right_subtree, sum_of_right_subtree, max_node_of_right_subtree = divide_and_conquer(node.right_child)
        
        sum_of_all = sum_of_left_subtree + sum_of_right_subtree
        
        # Determine the maximum value among the left subtree, right subtree, and the combined sum of both subtrees.
        if max_of_left_subtree >= max_of_right_subtree:
            if max_of_left_subtree >= sum_of_all:
                return max_of_left_subtree, sum_of_all, max_node_of_left_subtree
            else:
                return sum_of_all, sum_of_all, node
        else:
            if max_of_right_subtree >= sum_of_all:
                return max_of_right_subtree, sum_of_all, max_node_of_right_subtree
            else:
                return sum_of_all, sum_of_all, node

def find_path_of_max_subtree(node):
    """
    This function traces the path from a given node to the root of the tree.
    It returns a string where '0' indicates a left child and '1' indicates a right child.
    """
    path = ''
    while node.parent is not None:
        if node.parent.left_child == node:
            path += '0'
        else:
            path += '1'
        node = node.parent
    path += '*'  # Append '*' to indicate the root.
    return path[::-1]  # Reverse the path to get the correct order from root to leaf.

def print_tree(node):
    """
    This function prints the structure of the tree. It is useful for testing the correctness of the tree construction.
    """
    if node.parent is None:
        if node.value is None:
            print('*')
            print('+')
        else:
            print(node.value)
        print_tree(node.right_child)
        print_tree(node.left_child)
    elif node.value is None:
        print('+')
        print_tree(node.right_child)
        print_tree(node.left_child)
    else:
        print(node.value)

# Read the input values from a file and construct the tree.
file = open('input.txt')
values = file.read().split()  # Split the input string into a list of values based on spaces.
root = create_tree(values)
max_value, _, max_node = divide_and_conquer(root)
max_node_path = find_path_of_max_subtree(max_node)
print('Max Value = ', max_value)
print('Max Node Path: ', max_node_path)
