#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def _init_(self,val):
        self.val = val
        self.next = None
        
class Stack:
    def _init_(self):
        self.head = None
        self.size = 0
        
    def insert(self,k):
        if self.head != None:
            for i in range(self.size-1):
                self.head = self.head.next
            self.head.next = Node(k)
            
        if self.head == None:
            self.head = Node(k)
        
class Graph:
    def _init_(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self,s):
        
    def DFS(self,s):
        

