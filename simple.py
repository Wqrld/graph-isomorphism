from itertools import permutations

# Five undirected graphs.
graph_1 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph_2 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['X']}  # isomorphic to graph_1
graph_3 = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}  # not isomorphic to g1
graph_4 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['Y']} # not isomorphic to g1
graph_5 = {'A': ['A', 'U'], 'C': ['A'], 'U': ['A']} #isomorphic to g1
graph_6 = {'J': ['J', 'U'], 'C': ['J', 'C'], 'U': ['J']} #iso to 7
graph_7 = {'A': ['A', 'U'], 'U': ['A'], 'C': ['C', 'A']} #iso to 6


# Check for graph isomorphism
def is_isomorphic(g1: 'dict[str,list[str]]', g2: 'dict[str,list[str]]') -> bool:

    # Simple case: vertex count does not match
    if len(g1.keys()) != len(g2.keys()):
        print("Vertex count is not equal.")
        return False

    # Simple case: edge count does not match
    g1_edges_flattened = [edge for node_edges in g1.values()
                          for edge in node_edges]
    g2_edges_flattened = [edge for node_edges in g2.values()
                          for edge in node_edges]
    
    if len(g1_edges_flattened) != len(g2_edges_flattened):
        print("Edge count is not equal")
        return False

    # Simple case: degree distributions
    if sorted(map(len, g1.values())) != sorted(map(len, g2.values())):
        print("Degree distribution is not equal")
        return False

    """
    TODO:
     Try *all permutations of all groups of same-degree vertices* and check if this results in a graph isomorphism.
     - If applicable you may try to make the groups of similar vertices smaller before trying all permutations (which significantly reduces the number of attempts).
     For example, sort (secondary to the vertex degree) to the sum of neighbour degrees ... 
    """
    mappings = [dict(zip(g1.keys(), g2_keys_permutation)) for g2_keys_permutation in permutations(g2.keys())] #[{a:x, b:y}, {a:y, b:x}]
    for mapping in mappings:
        for vertex in g1.keys():
            for edge in g1[vertex]:
                if mapping[edge] not in g2[mapping[vertex]]: 
                    break
            else:
                continue # No break, all edges of this vertex match.
            break # some edge did not match, try next mapping.
        else:   
            # All edges matched for all vertices.
            print("Found isomorphism:", mapping)
            return True
        
    return False



print("Is the graph isomorphic?:", is_isomorphic(graph_6, graph_7))
