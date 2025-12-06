#Postorder: left -> right -> root

def postorder_iterative(self, root):
    postorder = []
    st1 = [root]
    st2 = []
    if not root:
        return postorder

    while st1:
        node = st1.pop()
        st2.append(node)

        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)

    while st2:
        postorder.append(st2.pop().val)
    return postorder