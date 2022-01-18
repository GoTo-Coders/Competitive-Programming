# Link --> https://www.hackerrank.com/challenges/30-binary-search-trees/problem

# Code:
def getHeight(self,root):
        if not root:
            return -1
        else:
            leftH = self.getHeight(root.left)
            rightH = self.getHeight(root.right)
            
            if leftH > rightH:
                return leftH + 1
            else:
                return rightH + 1
