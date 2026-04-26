def optimize_route(graph, stops, start):
    route = []
    current = start

    for stop in stops:
        distances, parent = graph.dijkstra(current)
        if distances[stop] == float('inf'):
            continue
        route.append(stop)
        current = stop

    return route
