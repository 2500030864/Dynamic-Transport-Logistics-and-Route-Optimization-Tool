def apply_traffic(graph, factor=1.2):
    # Simulate traffic by increasing weights
    for node in graph.graph:
        new_neighbors = []
        for neighbor, weight in graph.graph[node]:
            new_weight = int(weight * factor)
            new_neighbors.append((neighbor, new_weight))
        graph.graph[node] = new_neighbors
