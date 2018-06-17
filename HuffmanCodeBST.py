# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 03:42:13 2018

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:07:32 2018

@author: ASUS
"""
class Node:
    def __init__(self, val, symbol):
        self.sym = symbol
        self.val = val
        self.left = None
        self.right = None

class HuffmanCodeBST:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def add(self, val, symbol):
        n = Node(val, symbol)
        if self.isEmpty() == True:
            self.root = Node(None, None)
            self.root.left = n
        else:
            current_node = self.root
            while current_node is not None:
                pre_node = current_node
                if current_node.right is None:
                    current_node = current_node.right
                elif current_node.right.val is not None:
                    temp = Node(None, None)
                    temp.left = current_node.right
                    pre_node.right = temp
                    current_node = current_node.right
                else:
                    current_node = current_node.right
                    
            pre_node.right = n
            
    def inorder(self, t):
        if t is not None:
            self.inorder(t.left)
            print(' ', t.val)
            self.inorder(t.right)
    def preorder(self, t):
        if t is not None:
            print(' ', t.val)
            self.preorder(t.left)
            self.preorder(t.right)
    def postorder(self, t):
        if t is not None:
            self.postorder(t.left)
            self.postorder(t.right)
            print(' ', t.val)
    def findLeafs(self, t):
        if t.left == None and t.right == None:
            print(t.val)
        else:
            if t.left != None:
                self.findLeafs(t.left)
            if t.right != None:
                self.findLeafs(t.right)
    def CountLeaf(self, t):
        if t is None:
            return 0
        if t.left is None and t.right is None:
            print(' ', t.val)
            return 1
        return self.CountLeaf(t.left) + self.CountLeaf(t.right)
    def findNodeHasOneChild(self, t):
        if t is not None:
            if t.left == None and t.right != None:
                print(t.val)
                self.findNodeHasOneChild(t.right)
                return 1
            if t.right == None and t.left != None:
                print(t.val)
                self.findNodeHasOneChild(t.left)
                return 1
            if t.right != None and t.left != None:
                return self.findNodeHasOneChild(t.left) + self.findNodeHasOneChild(t.right)
        return 0
    def findNodeHas2SubNode(self, t):
        if t is not None:
            if t.left != None and t.right != None:
                print(t.val)
                self.findNodeHas2SubNode(t.left)
                self.findNodeHas2SubNode(t.right)
                return 1
            return 0
        return 0
    def findHeightOfTree(self, t, h):
        if t is None:
            return h
        else:
            h+=1
            hl = self.findHeightOfTree(t.left, h)
            hr = self.findHeightOfTree(t.right, h)
            if hl>=hr:
                return hl
            else:
                return hr
    def printBFT(self, t, k):
        if (k > 1):
            if t is not None:
                k -= 1
                self.printBFT(t.left, k)
                self.printBFT(t.right, k)
        else:
            if t is not None:
                if t.val is not None:
                    print(t.sym)
    def leftMost(self, t):
        if t.left is not None:
            self.leftMost(t.left)
        else:
            print(t.val)
    def leftMostOfRoot(self):
        temp = self.root.right
        if temp is not None:
            self.leftMost(temp)
        else:
            print(temp)
    def rightMost(self, t):
        if t.right is not None:
            self.rightMost(t.right)
        else:
            print(t.val)
    def rightMostOfRoot(self):
        temp = self.root.left
        if temp is not None:
            self.rightMost(temp)
        else:
            print(temp)
    def getNode(self, t, val):
        if t is not None:
            if t.val == val:
                return t
            else:
                l = self.getNode(t.left, val)
                r = self.getNode(t.right, val)
                if l is not None:
                    return l
                elif r is not None:
                    return r
        return None
    def findRightMostOfNode(self, val):
        node = self.getNode(self.root, val)
        if node is not None:
            if node.left is not None:
                self.rightMost(node.left)
            else:
                print(node.val)
        else:
            print('No such node in the tree')
    def findLeftMostOfNode(self, val):
        node = self.getNode(self.root, val)
        if node is not None:
            if node.right is not None:
                self.leftMost(node.right)
            else:
                print(node.val)
        else:
            print('No such node in the tree')
    def traverseTree(self, node, direction, dictionary):
        if node is not None:
            if node.sym is not None:
                print(node.sym, direction)
                dictionary[node.sym] = direction
            self.traverseTree(node.left, direction + '0', dictionary)
            self.traverseTree(node.right, direction + '1', dictionary)
