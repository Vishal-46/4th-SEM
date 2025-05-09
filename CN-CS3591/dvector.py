# distance_vector.py

def distance_vector_routing(graph, source):
    # initialize all distances to infinity
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    # relax edges |V|−1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    return distance


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 7},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 7, 'C': 3}
    }

    result = distance_vector_routing(graph, 'A')
    print("Distance Vector Routing Conclusion:",result)
