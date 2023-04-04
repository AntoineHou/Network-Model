import numpy as np

class Distribution():
    def __init__(self, distribution_type , alpha, yearly_evolution, fixed_value, xmin, xmax, Number_of_Step):
        self.distribution_type = distribution_type
        self.alpha = alpha
        self.yearly_evolution = yearly_evolution
        self.fixed_value = fixed_value
        self.xmin = xmin
        self.xmax = xmax
        self.Number_of_Step = Number_of_Step
        

    def power_sample(self):
        q = np.random.uniform(0, 1, self.Number_of_Step)
        return (q * (self.xmax**(-self.alpha + 1) - self.xmin**(-self.alpha + 1)) + self.xmin**(-self.alpha + 1))**(1 / (-self.alpha + 1))

    def return_power_distribution(self):
        power_law_samples = self.power_sample()
        power_law_samples = power_law_samples + np.random.uniform(0, 5, self.Number_of_Step+1)
        power_law_samples.sort()
        return list(power_law_samples)
    
    def linear_sample(self):
        return [self.yearly_evolution]*self.Number_of_Step+1
    
    def fixed_sample(self):
        return [self.fixed_value]*self.Number_of_Step+1
    
    def return_distribution(self):
        if self.distribution_type == 'Power':
            return self.return_power_distribution()
        elif self.distribution_type == 'Linear':
            return self.linear_sample()
        elif self.distribution_type == 'Fixed':
            return self.fixed_sample()
        else:
            print('Distribution type not found')
            raise ValueError



