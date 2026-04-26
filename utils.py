def display_graph(graph):
    print("\nAvailable locations:")
    for node in graph:
        print(node, end=" ")
    print()

def print_route(path, distance):
    print("\nShortest Route:", " -> ".join(path))
    print("Total Distance:", distance, "km")
