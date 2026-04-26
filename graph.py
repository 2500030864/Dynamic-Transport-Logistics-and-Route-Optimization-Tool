import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start):
        pq = []
        heapq.heappush(pq, (0, start))

        distances = {node: float('inf') for node in self.graph}
        parent = {node: None for node in self.graph}

        distances[start] = 0

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, parent

    def get_path(self, parent, start, end):
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        if path and path[0] == start:
            return path
        return []
