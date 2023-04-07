# Network Model 

Citation network model with partial knowledge of the node for addition. Before adding new paper a "**Library**" is created to consider a feasible number of paper read by an author and consider a mix between novel paper and preferential attachement.

## Parameters 

The model consider the dynamic within a specific scientific field and therefore the model considers both empirical values and parameters. 

### Empirical values 

 - **Number of paper in the library** : Fixed at 250 (Tenopir, C., Volentine, R., & King, D. W. (2012). Scholarly Reading and the Value of Academic Library Collections: results of a study in six UK universities. Insights)
 - **Novelty importance** : The fraction of novel papers (published within the last 3 years) in the library. 
 - **Novelty break point** : The probability that a "novel" paper will be cited over one with large amount of citation 
 - **Novelty hype** : A parameter allowing to differentiate paper added to the model giving more or less probability to be considered as a novel paper 

Those values allow to consider both the fact that reasearcher only consider a fraction of the papers in the citation network to add a new publication and that a mix between novel papers (or paper allowing to take part in the current scientific debate) and classics is made when publishing. 


### Parameter  

- **Initial Network** : Size (N) ; Edges attachement (M) to initiate a random graph using Barabási–Albert method. 
**Initial novelty** : Initial fraction of "novel" node in the network, the value implicitly defiene the initial year on which to compare the model results to actual data 
**Novelty time** : Number of step during which a new node is considered "novel" 

- **Network growth** :  Type (Power [Parameter alpha] describing a yearly evolution [in %] following a Power law [Min/Max used to fix the minimum % of evolution and maximum] ; Linear [% of evolution per step] describing a linear growth [in %] of the network size ; fixed [N] describing a fixed number of node added at each step)

- **Time** :  Number of step 


### Output 

- Json file describing the network topology at each step 
- Final network

