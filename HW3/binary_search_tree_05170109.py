#!/usr/bin/env python
# coding: utf-8

# In[3]:


class TreeNode(object):
    def _init_(self,x):
        self.left = None
        self.right = None
        self.val = x 
    
    def node_parent(self,root,val,target,parent = None):
        if root.val > target:
            if root.left == None:
                return False
            if root.left != None:
                return self.node_parent(root.left,target)
            
        if root.val <= target:
            if root.right == None:
                return False
            if root.right != None:
                return self.node_parent(root.right,target)
            
        if root.left.val == target or root.right.val == target:
            self.parent = root
            return self.parent
            
        
class Solution(object):   
    def insert(self,val,,root):
        Newnode = TreeNode(val)
        if val <= self.val:
            if self.left == None:
                self.left = Newnode
            else: 
                if val > self.left:
                    self.left.left = Newnode
                if val <= self.left:
                    self.left.right = Newnode
                
        if val > self.val:
            if self.right == None:
                self.right = Newnode
            else: 
                if val > self.right:
                    self.right.right = Newnode
                if val <= self.right:
                    self.right.left = Newnode
                    
    def search(self,root,target):
        if root.val == target:
            return root
        if root.val > target:
            if root.left != None:
                return self.search(left,root,target)
            else:
                return False
        if root.val <= target:
            if root.right != None:
                return self.search(right,root,target)
            else:
                return False
    
    def delete(self,root,node):
        if self.left == None:
            if self.right == None:
                self.node = None
                
                
        if self.right == None:
            if self.left != None:
                self.node = None
                self.left = self.node
            
        if self.left == None:
            if self.right != None:
                self.node = None
                self.right = self.node
                
        while self.right != None and self.left != None:
            if 
                
    def modify(self,root,target,new_val):
        while self.search(root,target) != False:
            self.delete(root,target)
            self.insert(root,new_val)
        return root
    
        
        


# In[ ]:

#參考來源: https://github.com/a303990366/Leet-Code/blob/master/HW3/binary_search_tree_05116127.py
#          https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be
#          https://www.laurentluce.com/posts/binary-search-tree-library-in-python/


