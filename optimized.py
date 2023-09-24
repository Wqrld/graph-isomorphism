from itertools import permutations

# Five undirected graphs.
graph_1 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph_2 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['X']}  # isomorphic to graph_1
graph_3 = {'A': ['B', 'C'], 'B': ['A', 'C'],
           'C': ['A', 'B']}  # not isomorphic to g1
graph_4 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['Y']}  # not isomorphic to g1
graph_5 = {'A': ['A', 'U'], 'C': ['A'], 'U': ['A']}  # isomorphic to g1
graph_6 = {'J': ['J', 'U'], 'C': ['J', 'C'], 'U': ['J']}  # iso to 7
graph_7 = {'A': ['A', 'U'], 'U': ['A'], 'C': ['C', 'A']}  # iso to 6


# Get sum of degrees of all neighbours of a vertex
# TODO memoize return value.
def neighbour_degree_sum(graph: 'dict[str,list[str]]', vertex: str) -> int:
    return sum(map(len, map(lambda neighbour: graph[neighbour], graph[vertex])))


"""
 Basic graph isomorphism algorithm with a few shortcuts for speedup.

 First, we check if the amount of vertices in both graphs are equal. If they are not then the graphs can never be isomorphic

 Then, we check if the total amount of edges in the graph are equal, again if they are not then the graphs are not isomorphic.

 And the last shortcut: Check if both graphs have the same properties in terms of the vertex degree distribution and
    the sum of degrees of neighbours.

 These checks will already rule out almost all graphs, for those that are similar enough, 
    we try all possible permutations of same-degree (and neighbour degree sum distribution) vertices.
"""


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

    # Simple case: Sorted array of (degree of vertex, sum of degrees of neighbouring vertices) for all vertices in the graph should be equal.
    if sorted(map(lambda v: (len(g1[v]), neighbour_degree_sum(g1, v)), g1.keys())) != sorted(map(lambda v: (len(g2[v]), neighbour_degree_sum(g2, v)), g2.keys())):
        print("Vertex neighbour degree does not match")
        return False

    # A(degree 2) can never be B(degree 1) and vice versa
    mappings_simple = [dict(zip(g1.keys(), g2_keys_permutation))
                for g2_keys_permutation in permutations(g2.keys())]  # [{a:x, b:y}, {a:y, b:x}]
    
    # Optimization: filter out mappings where the vertex degrees or sum of neighbour degrees do not match.
    mappings = list(filter(lambda mapping: all(map(lambda key: (len(g1[key]), neighbour_degree_sum(g1, key)) == (len(g2[mapping[key]]), neighbour_degree_sum(g2, mapping[key])), g1.keys())), mappings_simple))

    for mapping in mappings:
        for vertex in g1.keys():
            for edge in g1[vertex]:
                if mapping[edge] not in g2[mapping[vertex]]:
                    break
            else:
                continue  # No break, all edges of this vertex match.
            break  # some edge did not match, try next mapping.
        else:
            # All edges matched for all vertices.
            print("Found isomorphism:", mapping)
            return True

    return False

if __name__ == "__main__":
    print("Is the graph isomorphic?:", is_isomorphic(graph_6, graph_7))
