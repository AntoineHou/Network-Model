import igraph as ig

class Time_Passing:
    def __init__(self , G , Current_Step , Number_of_Step , Previous_Step_Novel , Distribution , distribution_type ) -> None:
        self.G = G
        self.Current_Step = Current_Step
        self.Number_of_Step = Number_of_Step
        self.Previous_Step_Dict_Novel = Previous_Step_Novel
        self.Distribution = Distribution
        self.distribution_type = distribution_type

    def Number_of_Node_Addition (self):
        if self.distribution_type == 'Power' or self.distribution_type == 'Linear':
            return int(len(self.Previous_Step_Dict_Novel)* self.Distribution[self.Current_Step]/100)
        elif self.distribution_type == 'Fixed':
            return int(self.Distribution[self.Current_Step])
        else:
            print('Distribution type not found')
            raise ValueError

    def Novelty_Back_to_Zero (self):
        G = self.G
        for i in self.Previous_Step_Dict_Novel:
            if G.vs[i]['novelty'] > 0:
                G.vs[i]['novelty'] -= 1
        return G