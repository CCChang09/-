#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Graph:
    def _init_(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self,s):
        
    def DFS(self,s):
        

