import igraph as ig 
import networkx as nx
import uuid
import random
import numpy as np

class Initial_Network:
    def __init__(self,  network_size = 1000 , m = 1 , Initial_Novelty = 0.1 ,novelty_time = 3 ) -> None:
        self.network_size = network_size
        self.m = m
        self.Initial_Novelty = Initial_Novelty
        self.novelty_time = novelty_time
        self.Graph = self.return_network()
        
    
    def Network (self):
        G = nx.barabasi_albert_graph(self.network_size , self.m)
        return ig.Graph.from_networkx(G)
    
    def Name_Nodes (self, G):
        for i in range(len(G.vs)):
            G.vs[i]['name'] = str(uuid.uuid4())
        return G
    
    def Novelty_Node (self, G) : 
        Node = random.sample(list(G.vs) , int(self.Initial_Novelty * self.network_size))
        for i in range(len(Node)):
            Node[i]['novelty'] = self.novelty_time
            Node[i]['hype'] = random.randint(1, 10)
        for i in range(len(G.vs)):
            if G.vs[i] not in Node:
                G.vs[i]['novelty'] = 0
                G.vs[i]['hype'] = 0
        return G
        
    def return_network (self):
        G = self.Network()
        G = self.Name_Nodes(G)
        G = self.Novelty_Node(G)
        return G

    

    
    
    
    
    

        
    