import networkx as nx

def build_graph(gdf):
    graph = nx.Graph()
    for idx, row in gdf.iterrows():
        graph.add_node(idx, population=row["population"])
    for i, a in gdf.iterrows():
        for j, b in gdf.iterrows():
            if i >= j:
                continue
            if a.geometry.touches(b.geometry):
                graph.add_edge(i, j)
    return graph
