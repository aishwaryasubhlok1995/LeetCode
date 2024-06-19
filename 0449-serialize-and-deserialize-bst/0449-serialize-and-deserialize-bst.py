# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''
        
        queueList = deque()
        queueList.append(root)
        ans = str(root.val) + ','
        while queueList:
            tree = queueList.popleft()
            if tree.left != None:
                ans += str(tree.left.val) + ','
                queueList.append(tree.left)
            else:
                ans += 'None' + ','
            if tree.right != None:
                ans += str(tree.right.val) + ','
                queueList.append(tree.right)  
            else:
                ans += 'None' + ','
        return ans[:len(ans)-1]
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return []
        lisOfNodes = data.split(',')
        queueList = deque()
        root = TreeNode(int(lisOfNodes[0]))
        queueList.append(root)
        i = 0
        while queueList:
            tree = queueList.popleft()
            i += 1
            if lisOfNodes[i] != 'None':
                NodeLeft = TreeNode(int(lisOfNodes[i]))
                tree.left = NodeLeft
                queueList.append(NodeLeft)
            i += 1
            if lisOfNodes[i] != 'None':
                NodeRight = TreeNode(int(lisOfNodes[i]))
                tree.right = NodeRight
                queueList.append(NodeRight)
        return root
            
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))