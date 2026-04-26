from graph import Graph
from data_loader import load_graph_from_csv
from traffic import apply_traffic
from utils import display_graph, print_route

def main():
    g = Graph()
    load_graph_from_csv('data/routes.csv', g)

    # Apply dynamic traffic
    apply_traffic(g)

    display_graph(g.graph)

    source = input("Enter source location: ").strip()
    destination = input("Enter destination location: ").strip()

    if source not in g.graph or destination not in g.graph:
        print("\nInvalid source or destination!")
        return

    distances, parent = g.dijkstra(source)
    path = g.get_path(parent, source, destination)

    if path and distances[destination] != float('inf'):
        print_route(path, distances[destination])
    else:
        print("\nNo route found!")

if __name__ == "__main__":
    main()
