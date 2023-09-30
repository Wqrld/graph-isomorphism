graph_1 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph_2 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['X']}  # isomorphic to graph_1

def write_graph(g):
    for key in g.keys():
        for edge in g[key]:
            file.write(f"{key} -- {edge}\n")

file = open("./graphs.dot", "w")
file.write("strict graph {\n")

write_graph(graph_1)
write_graph(graph_2)

file.write("}\n")

file.flush()
file.close()

# A graphs.dot has now been created. You can convert it to an svg with:
# dot -Tsvg graphs.dot > graphs.sv