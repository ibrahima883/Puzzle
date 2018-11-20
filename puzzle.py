#!/usr/bin/env python

# Diallo Ibrahima & Thiam Moustapha
# Projet: Resolution automatique d'un puzzle
# 11/01/2016

import numpy as np
import copy as cp

def Read_Data(my_puzzle):
    with open(my_puzzle, 'r') as file_in:
        contents= file_in.readlines()
        n=0
        m=0                 
        for i, line in enumerate(contents):          
            if i==0:    
                  k=0 
                  height=str() 
                  width=str()   
                  while line[k]!=' ':
                     height+=line[k]
                     k+=1
                  if k!=0 and line[k]==' ' :
                      while k < len(list(line))-1 :
                         width+= line[k]
                         k+=1
                  n=int(height)
                  m=int(width)
                  size=n*m
                  degres= [0]*size
                  degres=np.array(degres)
                  degres.resize(n,m)
            else :
                 j=0
                 for j in xrange(m):
                      if line[j] != '.' :
                         degres[i-1][j]= int(line[j])
                      else :
                         degres[i-1][j]=0
                      j+=1
    return degres

def News_Neighbors(degres):
        Degres_Neighbors = list()
        Index_Neighbors = list()
        n,m=np.shape(degres)
        for i in xrange(n):
           for j in xrange(m):               
                deg_neighbors=list()
                idx_neighbors=list() 
                if j < m-1 : #right neighbour
                   u=degres[i][j+1:]
                   idx=np.nonzero(u)
                   if idx[0].tolist() !=[] : 
                     idx=idx[0][0]+j+1
                     idx_neighbors.append(i*m+idx)
                     deg_neighbors.append(degres[i][idx])
                if j > 0 :#left neighbour
                   u=degres[i][:j] 
                   idx=np.nonzero(u)
                   if idx[0].tolist() !=[] : 
                     idx=idx[0][-1]
                     idx_neighbors.append(i*m+idx)
                     deg_neighbors.append(degres[i][idx])
                if i < n-1 : #bottom neighbour
                   u=degres[:,j][i+1:]
                   idx=np.nonzero(u)
                   if idx[0].tolist() !=[] :
                     idx=i+1+idx[0][0]
                     idx_neighbors.append(idx*m+j)
                     deg_neighbors.append(degres[idx][j])
                if i > 0 : #top neighbour
                   u=degres[:,j][i-1::-1]
                   idx=np.nonzero(u)
                   if idx[0].tolist() !=[] :
                     idx= i-1-idx[0][0]
                     idx_neighbors.append(idx*m+j)
                     deg_neighbors.append(degres[idx][j])
                Degres_Neighbors.append(deg_neighbors)
                Index_Neighbors.append(idx_neighbors)
        return Degres_Neighbors, Index_Neighbors
        
def Combination(old_A,coef): 
    new_A = [ cp.deepcopy(old_A), cp.deepcopy(old_A), cp.deepcopy(old_A)  ]
    for i in xrange(coef):
      for j in xrange(len(old_A)):
          new_A[i][j] = str(i)+str(new_A[i][j])

    res = cp.deepcopy(new_A[0])
    for i in xrange(coef-1):
        res += new_A[i+1]
    return res

def Possibilities(Nmax):
    n=len(Nmax)
    res = n*[[]]
    if Nmax[-1] == 2:
       res[0]=['0','1']
    if Nmax[-1] == 3:
        res[0] =['0','1', '2']
    for i in xrange(n-1):
        res[i+1]= Combination(res[i],Nmax[-i-2])
        
    for elt in list(res):
        for ch in list(elt):
            if ch[0] =='0':
                elt.remove(ch)
    return res

# for connexity
def find_Edges(k, idx_Vk, Edges):
    l=str(k)   
    for idx in idx_Vk:
        if k>idx:
            a=[idx,k]
        else:
            a=[k,idx]
        if a in Edges and str(idx) not in l:
           l+=str(idx)
    return l
    
 
def computeEdges(my_puzzle):   
        degres = Read_Data(my_puzzle)
        deg_1D = degres.flatten()
        Degres_Neighbors, Index_Neighbors = News_Neighbors(degres)
        k=0
        Edges=list()
        n,m=np.shape(degres)
        size=n*m
        for i in xrange(size):
          Edges.append([])

        Iter=0
        Essay=np.zeros(size,np.int)
        Nbmax_Essay=np.zeros(size,np.int)
        Passage=np.zeros(size,np.int)
        count=99*np.ones(size,np.int)
        p=0
        j=0
        c=0
        possibilities=list()
        idx_essays=([-1],)
        nb_vertex_essay=0
        bounds=list()
        comeback=0
        last=0
        while k < size and Iter < 1000:
           deg = deg_1D[k]
           if deg !=0:
             idrow_vr = -1
             idcol_vr  = -1
             idrow_vb = -1
             idcol_vb  = -1
             idl=-1
             idh=-1
             idr=-1
             idb=-1
             vr=0
             vb=0
             for q in Index_Neighbors[k]: 
                if abs(q-k) < m  and q < k :
                      idl = q
                if abs(q-k) >= m and q < k :
                      idh = q 
                if abs(q-k) < m  and q > k :
                      idr = q   
                      vr=deg_1D[idr] 
                      idrow_vr = q/m
                      idcol_vr = q%m
                if abs(q-k) >= m and q > k :
                      idb = q
                      vb=deg_1D[idb] 
                      idrow_vb = q/m
                      idcol_vb = q%m

             nb_edges_left=0  #number of edges build between idl and k
             if k>0 and idl >=0:             
               for o in Edges[idl]:
                  if k in o:
                     nb_edges_left+=1 
                     
             nb_edges_high=0  #number of edges build between idh and k
             if k>=m and idh >=0:
               for o in Edges[idh]:
                  if k in o:
                     nb_edges_high+=1  

             nb_remaining_edges = deg-nb_edges_left-nb_edges_high 
 
             count[k] = 0 # nb Edges en trop ou en moins
             if nb_remaining_edges == 4:
                 if vr > 1 and vb > 1:
                     Edges[k] = [[k,idr], [k,idr], [k,idb], [k,idb]] 
                 else : # we have not been able to place the edges for the index k
                     count[k] = nb_remaining_edges 
             elif nb_remaining_edges == 3:
                 if (vr == 8 and vb > 0) or (vb == 1 and vr > 1):
                     Edges[k] = [[k,idr], [k,idr], [k,idb]]
                 elif (vb == 8 and vr > 0) or (vr == 1 and vb > 1) :
                     Edges[k] = [[k,idr], [k,idb], [k,idb]]
                 elif idcol_vr == m-1 and vr == 6 and vb > 0:
                     Edges[k] = [[k,idr], [k,idr], [k,idb]]
                 elif idrow_vr == 0 and vr == 6 and vb > 0:
                     Edges[k] = [[k,idr], [k,idb], [k,idb]]
                 elif idcol_vr == m-1 and idrow_vr == 0 and vr == 4 and vb > 0:
                     Edges[k] = [[k,idr], [k,idr], [k,idb]]
                 elif idcol_vb == 0 and idrow_vb == n-1 and vb == 4 and vr > 0:
                     Edges[k] = [[k,idr], [k,idb], [k,idb]]
                 else:
                     Nbmax_Essay[k]=2 # Maximum number of possible essays on k
                     if vr > 0 and vb > 0:
                         if Essay[k] == 0: #--> we did a first essai
                             Edges[k] = [[k,idr], [k,idr], [k,idb]]    
                             Passage[k]=1  #--> means we did a esay on the index k
                         else: #--> we did a second essai
                             Edges[k] = [[k,idr], [k,idb], [k,idb]]  
                     else : # we have not been able to place the edges for the index k
                            count[k] = nb_remaining_edges
             elif nb_remaining_edges == 2:
                 if vr == 8 or (vb == 0 and vr > 1) :
                     Edges[k] = [[k,idr], [k,idr]]
                 elif vb == 8 or (vr == 0 and vb > 1):
                     Edges[k] = [[k,idb], [k,idb]]
                 elif (idrow_vr == 0 or idrow_vr == n-1 or idcol_vr == m-1) and vr == 6 :
                     Edges[k] = [[k,idr], [k,idr]]
                 elif (idcol_vb == 0 or idcol_vb == m-1 or idrow_vb == n-1) and vb == 6 :
                     Edges[k] = [[k,idb], [k,idb]]
                 elif (idcol_vr == m-1 and idrow_vr == 0) and vr == 4 :
                     Edges[k] = [[k,idr], [k,idr]]
                 elif (idcol_vb == 0 and idrow_vb == n-1) and vb == 4 :
                     Edges[k] = [[k,idb], [k,idb]]
                 elif (idcol_vr == m-1 and idrow_vr == n-1) and vr == 4 :
                     Edges[k] = [[k,idr], [k,idr]]
                 elif (idcol_vb == m-1 and idrow_vb == n-1) and vb == 4 :
                     Edges[k] = [[k,idb], [k,idb]]
                 else :
                     Nbmax_Essay[k] = 3 # Maximum number of possible essays on k
                     if vr > 0 and vb > 0:
                         if Essay[k] ==0: #--> we did a first essai
                             Edges[k] = [[k,idr], [k,idb]] 
                             Passage[k]=1 #--> means we did a esay on the index k
                         elif vr > 1 and Essay[k] == 1: #--> we did a second essai
                             Edges[k] = [[k,idr], [k,idr]]
                             Passage[k]=1                              
                         elif vb > 1 :   #--> we did a third essai 
                             Edges[k] = [[k,idb], [k,idb]]                                                         
                     else : # we have not been able to place the edges for the index k
                            count[k] = nb_remaining_edges
             elif nb_remaining_edges == 1:
                 if (deg == 1 and vr == 7) or (vb == 0 and vr > 0):
                     Edges[k] = [[k,idr]]
                 elif (deg == 1 and vb == 7) or (vr == 0 and vb > 0):
                     Edges[k] = [[k,idb]]
                 elif deg == 1 and vr == 3 and idrow_vr == 0 and idcol_vr == m-1 :
                     Edges[k] = [[k,idr]]
                 elif deg == 1 and vr == 3 and idrow_vr == n-1 and idcol_vr == m-1 :
                     Edges[k] = [[k,idr]]
                 elif deg == 1 and vb == 3 and idrow_vb == n-1 and idcol_vb == 0 :
                     Edges[k] = [[k,idb]]
                 elif deg == 1 and vb == 3 and idrow_vb == n-1 and idcol_vb == m-1 :
                     Edges[k] = [[k,idb]]
                 else : 
                     Nbmax_Essay[k] = 2  # Maximum number of possible essays on k
                     if vr > 0 and Essay[k] == 0:  #--> we did a first essai                           
                         Edges[k] = [[k,idr]]  
                         Passage[k]=1 #--> means we did a esay on the index k
                     elif vb > 0 and Essay[k] == 1: #--> we did a second essai
                         Edges[k] = [[k,idb]] 
                     else : # we have not been able to place the edges for the index k
                           count[k] = nb_remaining_edges 
             else: # we have not been able to place the edges for the index k
                 count[k] = nb_remaining_edges 

             
             if count[k] == 1 or count[k] == 2 or count[k] == 3 or count[k]==4 or count[k]<0:
                if idh >= 0 and Passage[idh] == 1 : 
                    if idh not in idx_essays[0]: 
                        k = idh-1  
                        Essay[idh]+=1
                    else:
                        comeback=1
                elif idl >= 0 and Passage[idl] == 1 :
                    if idl not in idx_essays[0]:
                        k = idl-1
                        Essay[idl]+=1
                    else:
                        comeback=1
                else: # recover the last index essay
                    last = np.nonzero(Passage[:k])[0][-1]
                    while Essay[last] == Nbmax_Essay[last]-1 and last >=0:
                        last = np.nonzero(Passage[:last])[0][-1]
                    Essay[last:]=0
                    Essay[last]+=1
                    k=last-1
                for i in xrange(size-k-1):
                     Edges[k+i+1]=list()
               
             if (count[k] > 4 and count[k]<9) or comeback==1:   
                 comeback=0                                 
                 if p==0: 
                     idx_essays = np.nonzero(Passage[:k]) 
                     nb_vertex_essay= len(idx_essays[0])
                     Nmax= nb_vertex_essay*[3]
                     possibilities= Possibilities(Nmax)
                     bounds= np.ones(nb_vertex_essay)
                     j= 0
                     c= 0
                     bounds[0]= len(possibilities[0])
                     for i in xrange(nb_vertex_essay-1):
                        bounds[i+1]=len(possibilities[i+1])+bounds[i]

                 bound =bounds[j]
                 p+=1
                 if bounds!=list() and p < bounds[-1]:                                    
                    ch=possibilities[j][c]
                    Essay[idx_essays[0]]=nb_vertex_essay*[0]
                    for i in xrange(j+1): 
                         Essay[idx_essays[0][-i-1]]=int(ch[-i-1])
                 
                 k= idx_essays[0][-j-1]-1
                 for i in xrange(size-k-1):
                    Edges[k+i+1]=list()
                    
                 if p==bound:                     
                        j+=1
                        c=0
                 else:
                        c+=1     

           k+=1
           Iter+=1
 
        if Edges!=[]:
          N=0
          N_vides=Edges.count([])
          while N < N_vides:
             Edges.remove([])
             N+=1 

          res=Edges[0]
          if len(Edges)>1:
             for i in xrange(len(Edges)-1):
               res+=Edges[i+1]

          return res 


