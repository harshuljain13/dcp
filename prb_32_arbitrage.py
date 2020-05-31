from math import log

def arbitrage(graph):
    modified_graph = [[-log(v) for v in row] for row in graph]
    n = len(graph)
    s=0
    min_costs = [float('inf') for i in range(n)]
    min_costs[0] = 0

    for _ in range(n-1):
        for v in range(n):
            for w in range(n):
                min_costs[w] = min(min_costs[w], min_costs[v]+ modified_graph[v][w])

    for v in range(n):
        for w in range(n):
            if min_costs[w]> min_costs[v]+modified_graph[v][w]:
                return True

    return False

graph = [
    [1, 0.741, 0.657, 1.061, 1.0011],
    [1.35, 1, 0.889, 1.433, 1.366],
    [1.521, 1.126, 1, 1.614, 1.538],
    [0.943, 0.698, 0.62, 1, 0.952],
    [0.955, 0.732, 0.65, 1.049, 1]]
print(arbitrage(graph))