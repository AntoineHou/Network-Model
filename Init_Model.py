import Distribution
import Initial_Network
import Snapshot
import Time_Passing
import Node_Addition
from pprint import pprint
import time 



class Parameter_Setter : 
    def __init__(self , Network_Size = 1000 , m = 1 , Initial_Novelty = 0.1 , breakpoint = 0.5 , novelty_time = 3 ,   Number_of_Step = 50 , Distribution_type = 'Power' , 
                  alpha = 1.7, yearly_evolution = 3   , fixed_value = 50,  xmin = 1, xmax = 50 ) -> None:
        self.Network_Size = Network_Size        
        self.m = m
        self.Break_point = breakpoint
        self.Initial_Novelty = Initial_Novelty
        self.novelty_time = novelty_time
        self.Number_of_Step = Number_of_Step
        self.Distribution_type = Distribution_type
        self.alpha = alpha
        self.yearly_evolution = yearly_evolution 
        self.fixed_value = fixed_value
        self.xmin = xmin
        self.xmax = xmax


class Object_Initializer : 
    def __init__(self, Parameter_Setter) :
        self.Parameter_Setter = Parameter_Setter
        self.NETWORK = Initial_Network.Initial_Network(self.Parameter_Setter.Network_Size , self.Parameter_Setter.m , self.Parameter_Setter.Initial_Novelty , self.Parameter_Setter.novelty_time )
        self.DISTRIBUTION = Distribution.Distribution(self.Parameter_Setter.Distribution_type , self.Parameter_Setter.alpha, self.Parameter_Setter.yearly_evolution, self.Parameter_Setter.fixed_value, self.Parameter_Setter.xmin, self.Parameter_Setter.xmax, self.Parameter_Setter.Number_of_Step)
        self.G = self.NETWORK.return_network()
        self.Distribution = self.DISTRIBUTION.return_distribution()


class Network_Model : 
    def __init__(self, Parameter_Setter, Object_Initializer ) :
        self.Parameter_Setter = Parameter_Setter
        self.Object_Initializer = Object_Initializer
        self.Distribution = self.Object_Initializer.Distribution
        self.G = self.Object_Initializer.G
        self.Time = 0 
        self.Node_To_Add = 0
        while self.Time < self.Parameter_Setter.Number_of_Step:
            pprint('-' * 50)
            pprint('Time: ' + str(self.Time))
            pprint('-' * 50)
            now = time.time()
            self.Snapshot = Snapshot.Snapshot(self.G , self.Time)
            self.Snapshot.export_Network_Topology('C:/Users/ahoussard/Documents/Python_Scripts/Network_Model/Snapshot')
            Novelty_Dict = self.Snapshot.return_novelty_dict()
            pprint('Time for snapshot: ' + str(time.time() - now))
            now = time.time()
            self.Time_Passing = Time_Passing.Time_Passing(self.G, self.Time , self.Parameter_Setter.Number_of_Step , Novelty_Dict , self.Distribution , self.Parameter_Setter.Distribution_type  )
            self.Node_To_Add = self.Time_Passing.Number_of_Node_Addition()
            self.Node_Addition = Node_Addition.Node_Addition(self.G , self.Node_To_Add ,  self.Parameter_Setter.Break_point, self.Parameter_Setter.novelty_time  )
            self.G = self.Node_Addition.add_vertex()
            pprint('Time to add nodes: ' + str(time.time() - now))
            now = time.time()
            self.G = self.Time_Passing.Novelty_Back_to_Zero()
            self.Time += 1
            pprint('Time to reset novelty: ' + str(time.time() - now))
    
if __name__ == "__main__":
    Parameter_Setter = Parameter_Setter()
    Object_Initializer = Object_Initializer(Parameter_Setter)
    Network_Model = Network_Model(Parameter_Setter, Object_Initializer)
        


