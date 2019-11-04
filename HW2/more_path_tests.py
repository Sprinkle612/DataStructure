from graph_adjacency_list import Graph as AdjacencyGraph
from graph_edge_list import Graph as EdgeGraph
from shortest_path import shortest_path
import sys

# ####################### RANDOM TEST
# # generate graph inputs
# for x in range(10000):
#   import random
#   random_weights = [random.randint(1,20) for i in range(16)]
#   nodelist1 = ['s','s','b','s','a','b','c','c','d','d','d','e','g','g','e','t']
#   nodelist2 = ['a','b','s','d','c','d','e','d','e','t','f','g','e','t','t','f']

#   # insert inputs
#   adjacency_graph = AdjacencyGraph()
#   edge_graph = EdgeGraph()
#   from dijkstar import Graph, find_path
#   graph = Graph()

#   for i in range(len(nodelist1)):
#     adjacency_graph.add_edge(nodelist1[i], nodelist2[i], random_weights[i])
#     edge_graph.add_edge(nodelist1[i], nodelist2[i], random_weights[i])
#     graph.add_edge(nodelist1[i], nodelist2[i], {'cost': random_weights[i]})

#   cost_func = lambda u, v, e, prev_e: e['cost']
#   test_function = find_path(graph, 'a', 'c', cost_func=cost_func)
#   if shortest_path(edge_graph, 's', 't') != (test_function[0], test_function[3]):
#     print("pass edge_graph")
#   else:
#     break
#   if shortest_path(adjacency_graph, 's', 't') != (test_function[0], test_function[3]):
#     print("pass adjacency_graph")
#   else:
#     break


####################### TEST 0

try:
  adjacency_graph = AdjacencyGraph()
  adjacency_graph.add_edge('s', 'a', 4)
  adjacency_graph.add_edge('a', 't', 3)
  adjacency_graph.add_edge('s', 'b', 5)
  adjacency_graph.add_edge('b', 't', 5)
  if shortest_path(adjacency_graph, 's', 't') != (['s','a','t'], 7):
    print("ERROR: TEST 0A, WRONG DISTANCE")
  else:
    print("pass test 0A")
except:
  print("ERROR: TEST 0A, ADDING EDGE")
  print(sys.exc_info()[0])

try:
  edge_graph = EdgeGraph()
  edge_graph.add_edge('s', 'a', 4)
  edge_graph.add_edge('a', 't', 3)
  if shortest_path(edge_graph, 's', 't') != (['s','a','t'], 7):
    print("ERROR: TEST 0B, WRONG DISTANCE")
  else:
    print("pass test 0B")
except:
  print("ERROR: TEST 0B, ADDING EDGE")
  print(sys.exc_info()[0])

####################### TEST 1

try:
  adjacency_graph = AdjacencyGraph()
  adjacency_graph.add_edge('s', 'a', 4)
  adjacency_graph.add_edge('s', 'b', 3)
  adjacency_graph.add_edge('b', 's', 3)
  adjacency_graph.add_edge('s', 'd', 7)
  adjacency_graph.add_edge('a', 'c', 1)
  adjacency_graph.add_edge('b', 'd', 4)
  adjacency_graph.add_edge('c', 'e', 1)
  adjacency_graph.add_edge('c', 'd', 3)
  adjacency_graph.add_edge('d', 'e', 1)
  adjacency_graph.add_edge('d', 't', 3)
  adjacency_graph.add_edge('d', 'f', 5)
  adjacency_graph.add_edge('e', 'g', 2)
  adjacency_graph.add_edge('g', 'e', 2)
  adjacency_graph.add_edge('g', 't', 3)
  adjacency_graph.add_edge('e', 't', 4)
  adjacency_graph.add_edge('t', 'f', 5)
  if shortest_path(adjacency_graph, 's', 't') != (['s','a','c','e','t'], 10):
    print("ERROR: TEST 1A, WRONG DISTANCE")
  else:
    print("pass test 1B")
except:
  print("ERROR: TEST 1A, ADDING EDGE")
  print(sys.exc_info()[0])

try:
  edge_graph = EdgeGraph()
  edge_graph.add_edge('s', 'a', 4)
  edge_graph.add_edge('s', 'b', 3)
  edge_graph.add_edge('b', 's', 3)
  edge_graph.add_edge('s', 'd', 7)
  edge_graph.add_edge('a', 'c', 1)
  edge_graph.add_edge('b', 'd', 4)
  edge_graph.add_edge('c', 'e', 1)
  edge_graph.add_edge('c', 'd', 3)
  edge_graph.add_edge('d', 'e', 1)
  edge_graph.add_edge('d', 't', 3)
  edge_graph.add_edge('d', 'f', 5)
  edge_graph.add_edge('e', 'g', 2)
  edge_graph.add_edge('g', 'e', 2)
  edge_graph.add_edge('g', 't', 3)
  edge_graph.add_edge('e', 't', 4)
  edge_graph.add_edge('t', 'f', 5)
  if shortest_path(edge_graph, 's', 't') != (['s','a','c','e','t'], 10):
    print("ERROR: TEST 1B, WRONG DISTANCE")
  else:
    print("pass test 1B")
except:
  print("ERROR: TEST 1B, ADDING EDGE")
  print(sys.exc_info()[0])

