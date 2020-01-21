class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def search(root,key):
    if root is None or root.val == key:
        return root
    else:
        if root.val < key:
            return search(root.right,key)
        else:
            return search(root.left,key)

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)

def min_value(root):
    current = root
    while current.left == None:
        current = current.left
    return current

def delete_node(root,key):
    if root is None:
        return root
    if root.val > key:
        root.left = delete_node(root.left,key)
    elif root.val < key:
        root.right = delete_node(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_value(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


if __name__ == '__main__':
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))
    inorder(r)
    print("*"*20)
    preorder(r)
    print("*" * 20)
    postorder(r)
    print("*" * 20)
    # print(search(r,5).val)
    # print("*" * 20)
    root = delete_node(r,20)
    inorder(root)