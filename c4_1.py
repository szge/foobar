# https://en.wikipedia.org/wiki/Maximum_flow_problem#Algorithms
# https://brilliant.org/wiki/ford-fulkerson-algorithm/
# https://www.programiz.com/dsa/ford-fulkerson-algorithm
from collections import defaultdict

MAX_FLOW = 2000000

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def solution(entrances, exits, path):
    # first idea: push through as many bunnies as possible through the entrances
    # then keep pushing through the max possible bunnies in the intermediary rooms until it reaches equilibrium
    # do we fit bunnies at the start or do we fit them from the end? is there a difference?
    # num_rooms = len(path)
    # inter_rooms = [x for x in range(0, num_rooms) if (x not in entrances and x not in exits)]
    # throughput = [0] * num_rooms # keeps track of the max number of bunnies that can pass through each room
    # # note: throughput[n] <= sum(path[n])
    # for entrance in entrances:
    #     # these will never change since it is already the max
    #     throughput[entrance] = sum(path[entrance])
    # stable = False
    # while not stable:
    #     stable = True
    #     for room in inter_rooms:
    #         throughput[room] = min(sum())
    #         stable = False

    # solve maximum flow problem with Ford-Fulkerson

    # create a single source and sink vertex, which means adding two extra vertices
    num_vertices = len(path) + 2
    # extend the existing arrays by two to accomodate
    for room in path:
        room += [0, 0]

    # create a source
    source_vertex = [0] * num_vertices
    for entrance in entrances:
        source_vertex[entrance] = MAX_FLOW
    path.append(source_vertex)

    # create a sink
    sink_vertex = [0] * num_vertices
    for exit in exits:
        path[exit][num_vertices - 1] = MAX_FLOW * num_vertices
    path.append(sink_vertex)
    g = Graph(path)
    source = num_vertices - 2
    sink = num_vertices - 1
    return g.ford_fulkerson(source, sink)

if __name__ == "__main__":
    print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))