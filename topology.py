# -*- coding: utf-8 -*-
#######topology gen####
"""
Created on Mon Jan 14 14:24:10 2019

@author: user
"""

MAXR =100
MAX_VC = 64
MAX_NODE = 50

topo = [ [ (-1) for i in range(MAX_NODE)] for j in range(MAX_NODE)] 
tmptopo=[ [ ([]) for i in range(MAX_NODE)] for j in range(MAX_NODE)] 
found= [[]for i in range(MAX_NODE)]
route=[ [ ([]) for i in range(MAX_NODE)] for j in range(MAX_NODE)] 
distance= [[]for i in range(MAX_NODE)]
path= [[]for i in range(MAX_NODE)]
sroute= [[]for i in range(MAX_NODE)]
#分行讀取並成link
def readtopology(topology):
    global node
    try:
        Readtopo=open(topology)
    except:
        print ('topology.txt error')
    cordata = Readtopo.readline()
    line=0 
    for i in cordata:
        
        if cordata[0:1]=='!':
            print (cordata.strip('!').strip())
        elif cordata[0:1]=='@':
            print(cordata)
         
            node,direct,maxlink,maxwavelength=cordata.replace('@','').replace('#','').split(',')
            node=int(node) 
            direct=int(direct) 
            maxlink=int(maxlink)   
            maxwavelength=int(maxwavelength)                                      
            
            
                                                             
        else:
            if(cordata!=''):
                line+=1
                a = cordata.strip('#\n').split(',')
                print(a[0],a[1])                               
                topo[int(a[0])][int(a[1])]=1
        cordata = Readtopo.readline()    
      

    
    print('%d,%d,%d,%d' %(node,direct,maxlink,maxwavelength))
    return node

    
def disjoit_path(s,dl):  
    i=0
    tmp=-1
    d=dl
    global path
    global route
    global sroute
    rr= [[]for i in range(MAX_NODE)]
    r= [[]for i in range(MAX_NODE)]
    st=[[]for i in range(10)]

    for i in range (MAX_NODE):
        path[i]=-1
        i=0
    rr[i]=d;
    i+=1
    while(tmp!=s):
        tmp=route[s][d]
        rr[i]=tmp
        i+=1
        d=tmp
    rr[i]=-1
    i-=1
    while(i>=0):
        j=0
        r[j]=rr[i]
        r[j]=-1
        j+=1
        i-=1
    rr=""
    if(s==dl):
        print(rr,'%d,%d,'%(s,dl))
        path[0]=s
        path[1]=dl
    else:
        i=0
        while(r[i]!=-1):
            path[i]=r[i]
            st=('%d'%(r[i]))
            rr+st
            i+=1
    sroute=rr        


def sh_path(source):
    i=0 
    pNext=0
    global router 
    done=0
    for i in range (node):
        found[i]=0
        distance[i]=topo[source][i]
    found[source]=1
    distance[source]=0
    pNext=source
    while not done:
        for pathi in range (node):
            if (not found[pathi]):
                if (distance[pathi]>=(distance[pNext]+topo[pNext][pathi])):
                    distance[pathi]=distance[pNext]+topo[pNext][pathi]
                    route[source][i]=pNext
        done=1
        for nexti in range (node):
            if(not found[pNext]):
                done=0
        if (done==0):
            pNext-choose()
            found[pNext]=1
    return 
                
    
def choose(void):
    global node
    min=30000
    minpos=-1
    i=0
    while(i<node):
        if (distance[i]<min and not found[i]):
            min=distance[i]
            minpos=i
        i+=1    
    return minpos

        



  
      
