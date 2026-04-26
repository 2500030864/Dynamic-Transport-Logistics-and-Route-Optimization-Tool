import csv

def load_graph_from_csv(filename, graph):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 3:
                continue
            u, v, w = row
            graph.add_edge(u.strip(), v.strip(), int(w))
