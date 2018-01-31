'''
Created on Jan 30, 2018

@author: sneupane
'''
from builtins import str

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}


def dijkstra(graph, start, goal):
    shortestDistance ={}
    predecessor={}
    unseenNodes=graph
    infinity = 9999
    path=[]
    
    for node in unseenNodes:
        shortestDistance[node] = infinity
    shortestDistance[start]=0  
    
    
    while unseenNodes:
        minNode= None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortestDistance[node] < shortestDistance[minNode]:
                minNode=node        
        for child, weight in graph[minNode].items():
            if weight + shortestDistance[minNode]< shortestDistance[child]:
                shortestDistance[child]  =weight + shortestDistance[minNode]  
                predecessor[child]=minNode
        unseenNodes.pop(minNode)        
        
    current = goal
    while current  !=start:
        try:
            path.insert(0, current)
            current = predecessor[current]
        except KeyError:    
            print("can't get there")
            break
    path.insert(0,start)
        
    if shortestDistance[goal]!=infinity:
        print("shortest distance: "+str(shortestDistance[goal]))
        print("path: "+ str(path))
        
dijkstra(graph, 'a', 'e')            
