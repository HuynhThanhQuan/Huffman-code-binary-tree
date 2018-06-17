class Node:                                                                     
    def __init__(self, val):                                         
        self.val = val                                                        
        self.left = None   
        self.right = None  
class BST:
	def __init__(self):
		self.root = None					
	def isEmpty(self):
		return self.root == None
	def add(self,val):                                                           		                                                        
		p= Node(val)	
		tmp=self.root
		pre =None   
		while (tmp is not None):
		    pre = tmp
		    if (val <= tmp.val):
		        tmp= tmp.left
		    else:
		        tmp= tmp.right        
		if (self.root is None):
		    self.root=p
		else:
		    if (val > pre.val):
		        pre.right =p
		    else:
		        pre.left=p
	def inorder(self,t):
	    if (t is not None):
	        self.inorder(t.left)
	        print(" " , t.val)
	        self.inorder(t.right) 
	def postorder(self, t):
	    if (t is not None):
	        self.postorder(t.left)            
	        self.postorder(t.right)
	        print(" ",t.val)
	def preorder(self, t):
	    if (t is not None):
	        print(" ", t.val)
	        self.preorder(t.left)            
	        self.preorder(t.right)            
	def CountLeaf(self, p):
	    if (p is None):
	        return 0
	    if ((p.left is None) and (p.right is None)): 
	        print(" ", p.val)
	        return 1       
	    return self.CountLeaf(p.left) + self.CountLeaf(p.right)
	
	
	def Count1Child(self,p):
	    if (p is None): 
	        return 0
	    if (((p.left is None) and (p.right is not None)) or ((p.left is not None) and (p.right is None))):
	        print(" ",p.val)
	        return 1+self.Count1Child(p.left) + self.Count1Child(p.right)  
	    return self.Count1Child(p.left) + self.Count1Child(p.right)    
    
    
	def Count2Childs(self, p):
		if (p is None):
			return 0
		if ((p.left is not None) and (p.right is not None)):       
			print(" ",p.val)
			return 1+self.Count2Childs(p.left) + self.Count2Childs(p.right)       
		return self.Count2Childs(p.left) + self.Count2Childs(p.right)
	
	def CalHeight(self,p):
		if (p is None):
			return 0
		a= self.CalHeight(p.left)
		b= self.CalHeight(p.right)
		if (a>b): 
			return a+1
		else:
			return b+1
	
	
	
	def RightmostOfRoot(self,p):
		pre=None
		if (p is not None):
		    p=p.left
		    while (p is not None):
		        pre=p
		        p=p.right
		return pre
   
   
	def Rightmost(self,el):
		p=self.root
		while ((p.val ==el or p is None) == False):  
		    if (el>p.val):
		        p=p.right
		    if (el<p.val):
		        p=p.left 
		pre=None
		if (p is not None):   
			p=p.left
			while (p is not None):
				pre=p
				p=p.right
		return pre
   
	def PrintByLevel(self, p,k):
		if (p is not None):       
			k -= 1
			if (p.left is not None):
				self.PrintByLevel(p.left,k)
			if (k==0):
				print(" ",p.val)
			if (p.right is not None):
				self.PrintByLevel(p.right,k)
	def deleteByCopying(self,el):
		p = self.root
		prev = None
		while (p is not None and p.val != el):
			prev = p
			if (p.val < el):
				p = p.right
			else:
				p = p.left
		node = p
		if (p is not None and p.val == el):
		    if (node.right is None): 
		        node = node.left
		    elif (node.left is None): 
		        node = node.right
		    else:
		        tmp = node.left
		        previous = node
		        while (tmp.right is not None):
		            previous = tmp
		            tmp = tmp.right                
		        node.val = tmp.val
		        if (previous == node):                
		            previous.left = tmp.left
		        else:
		            previous.right = tmp.left
		    if (p == self.root):
		        self.root = node
		    elif (prev.left == p):
		        prev.left = node
		    else:
		        prev.right = node
		elif (self.root is not null):
		    print("key ",el, " is not in the tree")
		else:
		    print("the tree is empty")
        		
if __name__ == "__main__":
    bst=BST()													        
    a= [5,7,1,2,9,12,6]    
    for i in range(len(a)):
        bst.add(a[i])
    print("LNR")
    bst.inorder(bst.root)
    print(" LRN")        
    bst.postorder(bst.root)
    print(" NLR")
    bst.preorder(bst.root)
    print("Count of leaf: ", bst.CountLeaf(bst.root))
    print("Count 1 Child: ", bst.Count1Child(bst.root))
    print("Count 2 Childs: ",bst.Count2Childs(bst.root))
    print("Height of the tree: ",bst.CalHeight(bst.root))
    print("Rightmost of Root: ", bst.RightmostOfRoot(bst.root).val)
    print("Rightmost of 7: ", bst.Rightmost(7).val)
    for i in range(1, bst.CalHeight(bst.root)+1):
        print("Level ", i, ":   ")
        bst.PrintByLevel(bst.root, i)  
    print("BST after deleting Node 5")
    bst.deleteByCopying(5)
    bst.preorder(bst.root)    