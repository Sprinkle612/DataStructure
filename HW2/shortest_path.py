# TODO: Rain Liang, XL778
# TODO: Thomas Kennedy Shanahan, TKS46

# Please see instructions.txt for the description of this problem.
#from exceptions import NotImplementedError

def shortest_path(graph, source, target):
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    #
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path
    #
    # NOTE: Please see instructions.txt for additional information about the
    # return value of this method.

    # store nodes that have been visited
    visited = []
    visited.append(source)
    # store weights from node to source
    lengths = {}
    lengths[source] = 0
    # store the parent of node
    parents = {}
    parents[source] = source
    while target not in visited:
        start = visited[-1]
        # update the adjacent nodes
        for (end, weight) in graph.get_neighbors(start):
            if end not in lengths:
                lengths[end] = lengths[start] + weight
                parents[end] = start
            else:
                if lengths[end] > lengths[start] + weight:
                    lengths[end] = lengths[start] + weight
                    parents[end] = start
        shortest_edge = 9999999999999999
        shortest_node = None
        # find the node with smallest weight
        for n, v in lengths.items():
            if n not in visited:
                if v < shortest_edge:
                    shortest_edge = v
                    shortest_node = n
        if shortest_path != None:
            visited.append(shortest_node)

    # print the path
    path = []
    path.append(target)
    while path[0] != source:
      par = parents[path[0]]
      path.insert(0,par)

    return (path, lengths[target])