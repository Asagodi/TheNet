import numpy
import math

class Node(Object):
  """ 
  Useful for the opinion network.
  """
  def __init__(self, value = 0):
    value = value



#Create three possibilities to represent graph?
class Graph(Object):
  def __init__(self, matrix = None, nnodes = 1):
    if matrix != None:
      self.matrix = matrix
      #self.nodes = 
      #self.edges = 
    else:
      self.nodes = []
      self.edges = []
      #self.matrix = Graph.convertomatrix
  
  
  
#Creating different graphs
def create_erdos(n = 1, p = 1.):
  # n Number of Nodes, p Choice to get edge
  matrix = np.zeros((n, n))
  for i in range(n):
    for j in range(n):
      if math.random < p:
        matrix[i, j] = 1
        
  return Graph(matrix = matrix)
