class DoctorNode:
    """
    A class to represent a node in the binary tree.
        Attributes:
            name (str): The name of the doctor.
            left (DoctorNode): The left child node, representing the left subordinate doctor.
            right (DoctorNode): The right child node, representing the right subordinate doctor.
    """
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    """ 
    A class to represent a binary tree for managing a doctor team structure.
        Attributes:
            root (DoctorNode): The root node of the tree, representing the lead doctor.
        Methods:
            insert(self, parent_node, new_node, side, current_node=None): Inserts a new doctor under the specified supervising doctor.
            preorder(self, node): Accepts a node and traverses the tree using the preorder traversal method. Returns a list of doctor names in the order they were visited in.
            inorder(self, node): Accepts a node and traverses the tree using the inorder traversal method. Returns a list of doctor names in the order they were visited in.
            postorder(self, node): Accepts a node and traverses the tree using the postorder traversal method. Returns a list of doctor names in the order they were visited in.
    """
    def __init__(self):
        self.root = None

    def insert(self, parent_node, new_node, side, current_node=None):
        """ Inserts a new doctor under the specified supervising doctor """
        #Case 1: empty tree
        if self.root is None:
            print("Tree is empty. Cannot insert without root.")
            return

        #Start from root if not part of recursive call
        if current_node is None:
            current_node = self.root

        #Case 2: Found the parent node
        if current_node.name == parent_node:

            #Check if side choice is valid
            if side != "left" and side != "right":
                print("Invalid side choice.")
                return True

            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(new_node)

                print(f"{new_node} added under {parent_node} on the left.") 
                return True 
                
            elif side == "right" and current_node.right is None: 
                current_node.right = DoctorNode(new_node)

                print(f"{new_node} added under {parent_node} on the right.") 
                return True 
            
            else: 
                print(f"{parent_node} already has a {side} subordinate.") 
                return True
                
        #Case 3: Search the subtrees
        found_left = False
        found_right = False
        
        if current_node.left:
            found_left = self.insert(parent_node, new_node, side, current_node.left)
    
        if current_node.right and not found_left:
            found_right = self.insert(parent_node, new_node, side, current_node.right)
    
        #Case 4: Parent node not found
        if not(found_left or found_right):

        #Avoid multiple searches by only printing when at the root
            if current_node == self.root:
                print(f"Parent node {parent_node} not found in the tree")
            return False
        
        return True
    
    def preorder(self, node):
        """ Prints the tree by visiting the root node of the subtree first. Next, the left subtree is traversed. Finally, the right subtree is traversed """

        #Base case - at a leaf
        if node is None:
            return []
        
        try:
            result = [node.name]
        except AttributeError:
            return "Error: Invalid data"

        #Recursive cases - append to list
        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result

    def inorder(self, node):
        """ The left subtree is traversed first. Next, the root node is processed. Finally, the right subtree is traversed last."""
        
        if node is None: # Base case, we've reached a leaf
            return []
        
        result = []
       
        try:
            result += self.inorder(node.left)
            
            result.append(node.name)
            
            result += self.inorder(node.right)
        
        except AttributeError:
            return "Error: invalid data"

        return result

    def postorder(self, node):
        """ The left subtree is traversed first. Next, the right subtree is traversed. Finally, the root node is visited last. """
        
        if node is None: # Base case, we've reached a leaf
            return []
        
        result = []

        try:
            result += self.postorder(node.left)
            result += self.postorder(node.right)
            result.append(node.name)
        except AttributeError:
            return "Error: invalid data"

        return result
    

# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()

#Define root of tree
tree.root = DoctorNode("Dr. Croft")

#Insert nodes into the tree
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")

#Test the insert method with edge cases
tree.insert("Dr. Brown", "Dr. Smith", "right")  #Invalid parent node
tree.insert("Dr. Croft", "Dr. Smith", "right")  #Parent node that already has 2 children
tree.insert("Dr. Carson", "Dr. Smith", "whatever")  #Invalid side


"""
Tree structure:

         Dr. Croft
        /           \
   Dr. Phan      Dr. Goldsmith
   /      \
Dr. Morgan  Dr. Carson

"""

#test the traversal methods
print("\n-------------------")
print("Preorder traversal:")
print("-------------------")
print(tree.preorder(tree.root))  #Start at root (Dr. Croft)
print(tree.preorder(tree.root.left))  #Start at left subtree (Dr. Phan)
print(tree.preorder(tree.root.left.right))  #Start at a leaf (Dr. Carson)
print(tree.preorder("a"))  #Invalid data

print("\n------------------")
print("Inorder traversal:")
print("------------------")
print(tree.inorder(tree.root))  #Start at root (Dr. Croft)
print(tree.inorder(tree.root.left))  #Start at left subtree (Dr. Phan)
print(tree.inorder(tree.root.left.right))  #Start at a leaf (Dr. Carson)
print(tree.inorder("a"))  #Invalid data

print("\n--------------------")
print("Postorder traversal:")
print("--------------------")
print(tree.postorder(tree.root))  #Start at root (Dr. Croft)
print(tree.postorder(tree.root.left))  #Start at left subtree (Dr. Phan)
print(tree.postorder(tree.root.left.right))  #Start at a leaf (Dr. Carson)
print(tree.postorder("a"))  #Invalid data
