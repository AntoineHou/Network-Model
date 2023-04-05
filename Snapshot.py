import igraph as ig
import json 

class Snapshot:
    def __init__(self, G , Current_Step) -> None:
        self.G = G
        self.Current_Step = Current_Step

    def Gini (self , Distribution) :
        n = len(Distribution)
        B = sum([(i+1)*Distribution[i] for i in range(n)])
        A = n * sum(Distribution)
        return (A - B) / A 

    def return_novelty_dict (self) :
        Dict = {}
        for i in range(len(self.G.vs)):
            Dict[i] = self.G.vs[i]['novelty']
        return Dict
    
    def degree_distribution(self):
        return self.G.degree()
    
    def Network_Topology (self) : 
        return {'Network_Size' : len(self.G.vs), 'Network_Density' : float(self.G.density()), 'Network_Gini' : self.Gini(self.degree_distribution()) , 
                'Degree_Distribution' : self.degree_distribution()} 
    
    # export the network topology to a json file
    def export_Network_Topology (self, path):
        with open(path + '/Network_Topology_{}.json'.format(self.Current_Step), 'w') as f:
            json.dump(self.Network_Topology(), f)

    




    