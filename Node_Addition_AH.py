import uuid
import igraph as ig
import random
from pprint import pprint
import numpy as np


class Node_Addition:
    def __init__(self, G , N_Node_Addition , Novelty_Dict , Break_point = 0.5 ,  novelty_time = 3 ) -> None:
        self.G = G
        self.N_Node_Addition = N_Node_Addition
        self.Novelty_Dict = Novelty_Dict
        self.Break_point = Break_point
        self.novelty_time = novelty_time
        self.Novel_Vertex, self.Old_Vertex = self.Old_New()
        self.Novel_Attributes = self.Nodes_relevant_attribute()
   
    def Old_New (self):
        Novel_Vertex =[]
        Old_Vertex = []
        for i in self.G.vs:
            if i['novelty'] > 0:
                Novel_Vertex.append(i)
            else:
                Old_Vertex.append(i)
        return Novel_Vertex, Old_Vertex     

    def Nodes_relevant_attribute (self) :
        Attributes = {}
        for i in self.G.vs :
            # get in degree of each node
            Attributes[i.index] = {'degree': i.degree(mode='in'), 'novelty': i['novelty'] , 'hype': i['hype']}
        return Attributes
    
    def Consitute_Library (self):
        k_Novel = int(random.normalvariate(75, 2))
        if k_Novel >len(self.Novel_Vertex) :
            k_Novel = len(self.Novel_Vertex)
        k_Old = int(random.normalvariate(75, 2))
        Novel_Picked = np.random.choice(self.Novel_Vertex, p = np.array([i['hype'] for i in self.Novel_Attributes.values() if i['novelty'] > 0]) / sum([i['hype'] for i in self.Novel_Attributes.values() if i['novelty'] > 0] ), size=k_Novel , replace=False)
        Old_Picked = np.random.choice(self.Old_Vertex, p=np.array([i['degree'] for i in self.Novel_Attributes.values() if i ['novelty'] == 0]) / sum([i['degree'] for i in self.Novel_Attributes.values() if i ['novelty'] == 0] ), size=k_Old , replace=False)
        
        # List of vertex to list of index
        Novel_Picked = dict(zip([i.index for i in Novel_Picked] , Novel_Picked)) 
        Old_Picked = dict(zip([i.index for i in Old_Picked] , Old_Picked)) 
        
        return Novel_Picked, Old_Picked
    
    def Pick_In_Library (self):
        Picked = []
        Novel_Picked , Old_Picked = self.Consitute_Library()
        for i in range(int(random.normalvariate(15, 1))) : 
            Break_point = random.uniform(0,1)
            if Break_point > self.Break_point :
                Nodes_old_Probability = {}
                for key ,  nodes in Old_Picked.items():
                    Nodes_old_Probability[nodes.index] = self.Novel_Attributes[nodes.index]['degree'] 
                Sum = sum(Nodes_old_Probability.values())
                for i in Nodes_old_Probability:
                    Nodes_old_Probability[i] = Nodes_old_Probability[i] / Sum
                Choice= np.random.choice(list(Nodes_old_Probability.keys()), p=list(Nodes_old_Probability.values()))
                Picked.append(Choice)
                del Old_Picked[key]
            else :
                Nodes_Novel_Probability = {}
                for key ,  nodes in Novel_Picked.items():
                    if self.Novel_Attributes[nodes.index]['novelty'] > 0:
                        Nodes_Novel_Probability[nodes.index] = 9
                    else : 
                        Nodes_Novel_Probability[nodes.index] = 1
                Sum = sum(Nodes_Novel_Probability.values())
                for i in Nodes_Novel_Probability:
                    Nodes_Novel_Probability[i] = Nodes_Novel_Probability[i] / Sum
                Choice = np.random.choice(list(Nodes_Novel_Probability.keys()), p=list(Nodes_Novel_Probability.values()))
                del Novel_Picked[key]
        return Picked

    def Add_Vertex (self) : 
        G = self.G
        uniform_samples  = np.random.uniform(0,1 , self.N_Node_Addition)
        for i in range(self.N_Node_Addition):
            Name = str(uuid.uuid4())
            Pick = self.Pick_In_Library()            
            V = G.add_vertex(name = Name , novelty = self.novelty_time , hype = uniform_samples[i])
            for j in range(len(Pick)):
                G.add_edge(V.index, Pick[j])
        return G
            
