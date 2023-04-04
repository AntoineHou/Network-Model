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
        self.Novel_Vertex, self.Old_Vertex = self._old_new()
        self.Novel_Attributes = self._nodes_relevant_attribute()
   
    def _old_new(self):
        novel_vertex = [v for v in self.G.vs if v['novelty'] > 0]
        old_vertex = [v for v in self.G.vs if v['novelty'] == 0]
        return novel_vertex, old_vertex

    def _nodes_relevant_attribute(self):
        return {
            v.index: {
                'degree': v.degree(mode='in'),
                'novelty': v['novelty'],
                'hype': v['hype']
            } for v in self.G.vs
        }

    
    def constitute_library(self):
        k_novel = int(random.normalvariate(75, 2))
        k_novel = min(k_novel, len(self.Novel_Vertex))
        k_old = int(random.normalvariate(75, 2))

        novel_attributes_novel = [i for i in self.Novel_Attributes.values() if i['novelty'] > 0]
        novel_probs = np.array([i['hype'] for i in novel_attributes_novel]) / sum(i['hype'] for i in novel_attributes_novel)
        novel_picked = np.random.choice(self.Novel_Vertex, size=k_novel, replace=False, p=novel_probs)

        novel_attributes_old = [i for i in self.Novel_Attributes.values() if i['novelty'] == 0]
        old_probs = np.array([i['degree'] for i in novel_attributes_old]) / sum(i['degree'] for i in novel_attributes_old)
        old_picked = np.random.choice(self.Old_Vertex, size=k_old, replace=False, p=old_probs)

        Novel_Picked = dict(zip([i.index for i in novel_picked], novel_picked))
        Old_Picked = dict(zip([i.index for i in old_picked], old_picked))

        return Novel_Picked, Old_Picked
    
    def pick_in_library(self):
        picked = []
        novel_picked, old_picked = self.constitute_library()

        for _ in range(int(np.random.normal(15, 1))):
            break_point = np.random.uniform(0, 1)

            if break_point > self.Break_point:
                nodes_old_probability = {node.index: self.Novel_Attributes[node.index]['degree'] for node in old_picked.values()}
                sum_old_probabilities = sum(nodes_old_probability.values())
                nodes_old_probability = {index: value / sum_old_probabilities for index, value in nodes_old_probability.items()}
                choice = np.random.choice(list(nodes_old_probability.keys()), p=list(nodes_old_probability.values()))
                picked.append(choice)
                old_picked = {key: value for key, value in old_picked.items() if value.index != choice}
            else:
                nodes_novel_probability = {node.index: 9 if self.Novel_Attributes[node.index]['novelty'] > 0 else 1 for node in novel_picked.values()}
                sum_novel_probabilities = sum(nodes_novel_probability.values())
                nodes_novel_probability = {index: value / sum_novel_probabilities for index, value in nodes_novel_probability.items()}
                choice = np.random.choice(list(nodes_novel_probability.keys()), p=list(nodes_novel_probability.values()))
                novel_picked = {key: value for key, value in novel_picked.items() if value.index != choice}

        return picked

    def add_vertex (self) : 
        G = self.G
        uniform_samples  = np.random.uniform(0,1 , self.N_Node_Addition)
        for i in range(self.N_Node_Addition):
            Name = str(uuid.uuid4())
            Pick = self.pick_in_library()            
            V = G.add_vertex(name = Name , novelty = self.novelty_time , hype = uniform_samples[i])
            for j in range(len(Pick)):
                G.add_edge(V.index, Pick[j])
        return G
            
