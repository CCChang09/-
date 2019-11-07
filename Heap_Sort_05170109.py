# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class solution:
    def heapify(self,seq,x):
        n = len(seq)
        layer = int(n/2)
        #layer為須比大小的層(詳情寫於學習歷程說明中) 此處程式碼為參考05116127林庭嘉同學之寫法
        
        
        for x in range(layer,-1,-1):
            L = 2*x+1
            R = 2*x+2
            if L < n and seq[x] > seq[L] :
                seq[x],seq[L] = seq[L],seq[x]
                #L較大的情況
            
            if R < n and seq[x] > seq[R]:
                seq[x],seq[R] = seq[R],seq[x]
                #R較大的情況
                
            else:
                seq[x],seq[L] = seq[x],seq[L] 
                seq[x],seq[R] = seq[x],seq[R]
                
        return seq 
    
    
    def heap_sort(self,seq):
        n=len(seq)
        final=[]
        for i in range(n,0,-1):
            self.heapify(seq)
            seq[0],seq[n-1]=seq[n-1],seq[0]
            final.insert(0,seq[n-1])
            n-=1
            seq=seq[0:n]
        
        
        return final


