'''
Created on 6 dec. 2012 

@author: David
inspired by Telmo Menezes's work : telmomenezes.com
''' 

""" 
this class inherits from networkx.Diself. It stores a distance matrix and some global variables about the network. 
It allows us to update them easily instead of computing them many times.
       

"""
import networkx as nx
import numpy as np

class DiGraphWithUpdate(nx.DiGraph):
    
    def __init__(self):
        """ The creator of DiselfWithUpdate Class """
        
        nx.DiGraph.__init__(self)
        self.shortest_path_dict = None
        self.max_distance = None
        self.max_in_degree = None
        self.max_in_strength = None
        self.max_out_degree = None
        self.max_out_strength = None
       
    def add_edge(self,u,v,**args):
        nx.DiGraph.add_edge(self, u, v, args)
        
        #update info about the network : not really an update but a computation
        if self.shortest_path_dict is not None :
            self.shortest_path_dict = nx.shortest_path_length(self,weight="weight")
        if self.max_distance is not None :
            self.max_distance = max(max(dictionnaire.values()) for dictionnaire in self.get_shortest_path_dict().values())
        if self.max_in_degree is not None :
            self.max_in_degree = float(max(self.in_degree().values()))
        if self.max_out_degree is not None :
            self.max_out_degree = float(max(self.out_degree().values()))
        if self.max_in_strength is not None :
            self.max_in_strength = max(self.in_degree(weight="weight").values())
        if self.max_out_strength is not None :
            self.max_out_strength = max(self.out_degree(weight="weight").values())
        
        
    
    
      
    def OrigInDegree(self) : 
        ''' returns a 2d array containing the in degree of the origin node for all edges
        '''
        probas = np.dot( 
                        np.array(self.in_degree().values(),dtype=float).reshape(-1,1),
                        np.ones((1,self.number_of_nodes())))
        return probas
    
    def NormalizedOrigInDegree(self) : 
        ''' returns a 2d array containing in degree of origin divided by max of in_degrees 
        '''
        return self.OrigInDegree()/self.get_max_in_degree()
    
    def OrigInStrength(self) : 
        ''' returns a 2d array containing the in strength = weighted in degree of the origin node for all edges
        '''
        probas = np.dot( 
                      np.array(self.in_degree(weight="weight").values()).reshape(-1,1),
                      np.ones((1,self.number_of_nodes())))
        return probas
    
    def NormalizedOrigInStrength(self) : 
        ''' returns a 2d array containing the in strength of the origin node divide by max of in_strength for all edges
        '''
        if self.get_max_in_strength() == 0 :
            return np.zeros((self.number_of_nodes(), self.number_of_nodes())) 
        return self.OrigInStrength()/self.get_max_in_strength()
    
    def OrigOutDegree(self) :
        ''' returns a 2d array containing the out degree of the origin node for all edges
        '''
        probas = np.dot( 
                      np.array(self.out_degree().values(),dtype=float).reshape(-1,1),
                      np.ones((1,self.number_of_nodes())))
        return probas
    
    def NormalizedOrigOutDegree(self) :
        ''' returns a 2d array containing the out degree of the origin node for all edges divide by max of out_degrees
        '''
        
        return self.OrigOutDegree()/self.get_max_out_degree()
    
    def OrigOutStrength(self) :
        ''' returns a 2d array containing the out degree of the origin node for all edges
        '''
        probas = np.dot( 
                      np.array(self.out_degree(weight="weight").values()).reshape(-1,1),
                      np.ones((1,self.number_of_nodes())))
        return probas
    
    def NormalizedOrigOutStrength(self) :
        ''' returns a 2d array containing the out degree of the origin node for all edges divided by max of out_strength
        '''
        if self.get_max_out_strength() == 0 :
            return np.zeros((self.number_of_nodes(), self.number_of_nodes())) 
        return self.OrigOutStrength()/self.get_max_out_strength()
    
    def OrigId(self) : 
        ''' returns a 2d array containing the identity number (0 to n=number of nodes) of the origin node for all edges
        ''' 
        probas = np.dot( 
                      np.array(range(self.number_of_nodes()),dtype=float).reshape(-1,1),
                      np.ones((1,self.number_of_nodes())))
        return probas
    
    def NormalizedOrigId(self) :
        ''' returns a 2d array containing the identity number (0 to n=number of nodes) of the origin node for all edges divide by the total number of nodes
        ''' 
        
        return self.OrigId()/self.number_of_nodes()
    
    def TargInDegree(self) : 
        ''' returns a 2d array containing the in degree of the target node for all edges
        ''' 
        probas =  np.dot( 
                      np.ones((self.number_of_nodes(),1)),
                      np.array(self.in_degree().values(),dtype=float).reshape(1,-1)
                      )       
        return probas
    
    def NormalizedTargInDegree(self) : 
        ''' returns a 2d array containing the in degree of the target node for all edges divided by max of in_degrees
        ''' 
          
        return self.TargInDegree()/self.get_max_in_degree()
    
    def TargInStrength(self) : 
        ''' returns a 2d array containing the in degree of the target node for all edges
        ''' 
        probas =  np.dot( 
                      np.ones((self.number_of_nodes(),1)),
                      np.array(self.in_degree(weight="weight").values()).reshape(1,-1)
                      )       
        return probas
    
    def NormalizedTargInStrength(self) : 
        ''' returns a 2d array containing the in degree of the target node for all edges divided by max of in_strength
        '''   
        if self.get_max_in_strength() == 0 :
            return np.zeros((self.number_of_nodes(), self.number_of_nodes()))     
        return self.TargInStrength()/self.get_max_in_strength()
    
    def TargOutDegree(self) :
        ''' returns a 2d array containing the out degree of the target node for all edges
        ''' 
        probas =  np.dot( 
                      np.ones((self.number_of_nodes(),1)),
                      np.array(self.out_degree().values(),dtype=float)
                      )       
        return probas
    
    def NormalizedTargOutDegree(self) :
        ''' returns a 2d array containing the out degree of the target node for all edges
        '''       
        return self.TargOutDegree()/self.get_max_out_degree()
    
    
    def TargOutStrength(self) :
        ''' returns a 2d array containing the out degree of the target node for all edges
        ''' 
        probas =  np.dot( 
                      np.ones((self.number_of_nodes(),1)),
                      np.array(self.out_degree(weight="weight").values(), dtype=float).reshape(1,-1)
                      )       
        return probas
    
    def NormalizedTargOutStrength(self) :
        ''' returns a 2d array containing the out degree of the target node for all edges divided by max of out strengths
        '''
        if self.get_max_out_strength() == 0 :
            return np.zeros((self.number_of_nodes(), self.number_of_nodes()))         
        return self.TargOutStrength()/self.get_max_out_strength()
       
    def TargId(self) : 
        ''' returns a 2d array containing the identity number of the target node for all edges
        ''' 
        probas =  np.dot( 
                      np.ones((self.number_of_nodes(),1)),
                      np.array(range(self.number_of_nodes()),dtype=float).reshape(1,-1)
                      )               
        return probas
    
    def NormalizedTargId(self) : 
        ''' returns a 2d array containing the identity number of the target node for all edges divided by the number of nodes
        '''       
        return self.TargId()/self.number_of_nodes()
    
    
    def DirectDistance(self) :
        ''' returns a 2d array containing the direct distance = shortest path length, takes weights into account, takes direction of edges into account'''
        ''' gives +infinity if no path'''
        
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        #every path that does not exist has distance +infinity
        probas.fill(float('+inf'))
        
        for node1, row in self.get_shortest_path_dict().iteritems():
            for node2, length in row.iteritems():
                probas[node1, node2] = length 
        return probas
    
    def NormalizedDirectDistance(self) :
        ''' returns a 2d array containing the direct distance = shortest path length, takes weights into account, takes direction of edges into account'''
        ''' gives +infinity if no path'''
        ''' divides by distance maximal distance which is always real but can be 0 ''' 
        return self.DirectDistance()/self.get_max_distance()
    
    
    def ReversedDistance(self) :
        ''' returns a 2d array containing the reversed distance = reversed shortest path length, takes weights into account, takes direction of edges into account'''
        ''' gives +infinity if no path'''
       
        #every path that does not exist has distance +infinity
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        probas.fill(float('+inf'))
        
        for node1, row in self.get_shortest_path_dict().iteritems():
            for node2, length in row.iteritems():
        #This line is the difference with direct distance function:  direct shortest path length from key1 to key2 = reversed sortest path length from key2 to key1        
                probas[node2, node1] = length 
        return probas
    
    def NormalizedReversedDistance(self) :
        '''' returns a 2d array containing the reversed distance = reversed shortest path length, takes weights into account, takes direction of edges into account'''
        ''' gives +infinity if no path'''
        ''' divides by distance maximal distance which is always real but can be 0 ''' 
        return self.ReversedDistance()/self.get_max_distance()
    
    def NumberOfNodes(self):
        ''' returns a 2d array filled with only one value : the number of nodes of the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.number_of_nodes()
        probas.fill(value)
        return probas
    
    def NumberOfEdges(self):
        ''' returns a 2d array filled with only one value : the number of edges of the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.number_of_edges()
        probas.fill(value)
        return probas
    
    def MaxInDegree(self):
        ''' returns a 2d array filled with only one value : the maximal in degree among nodes in the network'''
      
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.get_max_in_degree()
        probas.fill(value)
        return probas
    
    def AverageInDegree(self):
        ''' returns a 2d array filled with only one value : the average of  in degrees in teh network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = sum(self.in_degree().values())/self.number_of_nodes()
        probas.fill(value)
        return probas
    
    def MaxOutDegree(self):
        ''' returns a 2d array filled with only one value : the maximal out degree among nodes in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.get_max_out_degree()
        probas.fill(value)
        return probas
    
    def AverageOutDegree(self):
        ''' returns a 2d array filled with only one value : the average of out degrees in teh network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = sum(self.out_degree().values())/self.number_of_nodes()
        probas.fill(value)
        return probas
    
    
    def MaxInStrength(self):
        ''' returns a 2d array filled with only one value : the sum of in strengths in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.get_max_in_strength()
        probas.fill(value)
        return probas
    
    def AverageInStrength(self):
        ''' returns a 2d array filled with only one value : the sum of in strengths in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = sum(self.in_degree(weight="weight").values())/self.number_of_nodes()
        probas.fill(value)
        return probas
    
    
    def MaxOutStrength(self):
        ''' returns a 2d array filled with only one value : the sum of in strengths in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.get_max_out_strength()
        probas.fill(value)
        return probas
    
    def AverageOutStrength(self):
        ''' returns a 2d array filled with only one value : the sum of in strengths in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = sum(self.out_degree(weight="weight").values())/self.number_of_nodes()
        probas.fill(value)
        return probas
    
    def TotalWeight(self):
        ''' returns a 2d array filled with only one value : the sum of strengths of links in the network = size of the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        value = self.size(weight="weight")
        probas.fill(value)
        return probas
    
    
    def AverageWeight(self):
        ''' returns a 2d array filled with only one value : the sum of in strengths in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        if self.number_of_edges() == 0 : 
            value = 0
        else :
            value = self.size(weight="weight")/self.number_of_edges()
        probas.fill(value)
        return probas
    
    def MaxWeight(self):
        ''' returns a 2d array filled with only one value : the maximal weight in the network'''
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        list_of_weights = nx.get_edge_attributes(self, "weight").values()
        if len(list_of_weights) == 0 :
            value = 0
        else :
            value = max(list_of_weights)
        probas.fill(value)
        return probas
    
    def MaxDistance(self) :
        ''' returns a 2d array filled with only one value : the max of distances in the network'''

        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        max_distance = self.get_max_distance()
        probas.fill(max_distance)  
        return probas
    
    def AverageDistance(self) :
        ''' returns a 2d array filled with only one value : the average of distances in the network'''
        
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        shortest_path_dict = self.get_shortest_path_dict()
        number_of_distances = sum(len(dictionnaire.values()) for dictionnaire in shortest_path_dict.values())
        sum_of_distances = sum(sum(dictionnaire.values()) for dictionnaire in shortest_path_dict.values())
        value = sum_of_distances/number_of_distances
        probas.fill(value)  
        return probas
    
    def TotalDistance(self) :
        ''' returns a 2d array filled with only one value : the sum of distances in the network'''
        
        
        probas = np.empty((self.number_of_nodes(), self.number_of_nodes()))
        shortest_path_dict = self.get_shortest_path_dict()
        value = sum(sum(dictionnaire.values()) for dictionnaire in shortest_path_dict.values())
        probas.fill(value)  
        return probas
    
    def Constant(self) :
        ''' returns a 2d array filled with only one value : 1'''
        
        probas = np.ones((self.number_of_nodes(), self.number_of_nodes()))  
        return probas
    
    def Random(self) :
        ''' returns a 2d array filled with only random value between 0 and 1'''
        
        probas = np.random.rand(self.number_of_nodes(), self.number_of_nodes())  
        return probas
    
    def get_shortest_path_dict(self) :
        ''' returns the dict od dict of shortest path lengths, if it does not exist, it creates it'''
        if self.shortest_path_dict is None :
            self.shortest_path_dict = nx.shortest_path_length(self,weight="weight")
        return self.shortest_path_dict
    
    def get_max_in_degree(self):
        ''' returns the maximum of in_degrees, if it does not exist, it computes it'''
        if self.max_in_degree is None :
            self.max_in_degree = max(self.in_degree().values())
        return self.max_in_degree 
    
    def get_max_out_degree(self):
        ''' returns the maximum of out_degrees, if it does not exist, it computes it'''
        if self.max_out_degree is None :
            self.max_out_degree = max(self.out_degree().values())
        return self.max_out_degree
    
    def get_max_in_strength(self):
        ''' returns the maximum of in_strengths, if it does not exist, it computes it'''
        if self.max_in_strength is None :
            self.max_in_strength = max(self.in_degree(weight="weight").values())
        return self.max_in_strength 
    
    def get_max_out_strength(self):
        ''' returns the maximum of out_strengths, if it does not exist, it computes it'''
        if self.max_out_strength is None :
            self.max_out_strength = max(self.out_degree(weight="weight").values())
        return self.max_out_strength
    
    def get_max_distance(self):
        if self.max_distance is None :
            self.max_distance = max(max(dictionnaire.values()) for dictionnaire in self.get_shortest_path_dict().values())
        return self.max_distance
    
    #useless functions but must to be there to work in the same conditions as graphWithUpdate
    def OrigDegree(self) : 
        pass   
    def NormalizedOrigDegree(self) : 
        pass    
    def OrigStrength(self) : 
        pass    
    def NormalizedOrigStrength(self) : 
        pass    
    def TargDegree(self) : 
        pass   
    def NormalizedTargDegree(self) : 
        pass    
    def TargStrength(self) : 
        pass    
    def NormalizedTargStrength(self) : 
        pass   
    def Distance(self) :
        pass    
    def NormalizedDistance(self) :
        pass    
    def MaxDegree(self):
        pass   
    def AverageDegree(self):
        pass   
    def MaxStrength(self):
        pass  
    def AverageStrength(self):
        pass
        