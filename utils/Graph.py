import sys


class Node:
    def __init__(self, x, y):
        self.id = y * 28 + x
        self.x = x
        self.y = y


def copy_arr(grid):
    copy = [[0 for k in range(len(grid[0]))] for j in range(len(grid))]
    for k in range(len(grid)):
        for j in range(len(grid[0])):
            copy[k][j] = grid[k][j]
    return copy


def get_number_of_nodes_from_grid(grid):
    grid_nodes = 0
    copy = copy_arr(grid)
    print(copy)
    for k in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            node_sum = 0
            if grid[k][j] == 1:
                node_sum = grid[k + 1][j] + grid[k - 1][j] - grid[k][j + 1] - grid[k][j - 1]
                if node_sum != -2 and node_sum != 2:
                    grid_nodes += 1
                    copy[k][j] = 2

    return grid_nodes, copy


def get_id(x, y):
    return y * 28 + x


def dfs(graph, source, node_grid):
    graph.visited[source] = 1
    node_grid[graph.nodes[source].x][graph.nodes[source].y] = 3
    for next_node in range(0, graph.n_nodes):
        if graph.dTable[source][next_node] != 0 and graph.visited[next_node] == 0:
            dfs(graph, next_node, node_grid)


def get_min_unvisited(distance, visited):
    mind = sys.maxsize
    min_idx = -1
    for x in range(len(distance)):
        if distance[x] < mind and visited[x] == 0:
            mind = distance[x]
            min_idx = x

    return min_idx


def print_path(parent, source, dest):
    print("[G] Path to source: ")
    while dest != source:
        print("{} -> ".format(dest), end='')
        dest = parent[dest]
    print(source)


def create_path(parent, source, dest):
    path = []
    #print("[G] Created path to source: ")
    while dest != source:
        path.append(dest)
        #print("{} -> ".format(dest), end='')
        dest = parent[dest]
    print(source)
    path.append(source)
    return path


def dijkstra(graph, source):
    visited = [0 for i in range(len(graph.nodes))]
    distance = [sys.maxsize for i in range(len(graph.nodes))]
    parent = [0 for i in range(len(graph.nodes))]
    print("[G] Created distance arr with len {}".format(len(distance)))
    distance[source] = 0
    parent[source] = source
    #print(distance)
    #print(get_min_unvisited(distance, visited))

    for c in range(graph.n_nodes - 1):

        u = get_min_unvisited(distance, visited)
        visited[u] = 1

        for x in range(graph.n_nodes):
            if visited[x] == 0 and graph.dTable[u][x] and distance[u] != sys.maxsize and distance[u] + graph.dTable[u][
                x] < distance[x]:
                distance[x] = distance[u] + graph.dTable[u][x]
                parent[x] = u

    #print(parent)
    print("OK")
    return parent


class Graph:

    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.nodes = []
        self.visited = [0 for i in range(n_nodes)]
        self.dTable = [[0 for i in range(n_nodes)] for j in range(n_nodes)]

    def make_graph(self, node_grid):

        for k in range(1, len(node_grid) - 1):
            for j in range(1, len(node_grid[0]) - 1):
                if node_grid[k][j] == 2:
                    node = Node(j, k)
                    self.nodes.append(node)

        print("[!] Found number of nodes: {}".format(self.n_nodes))
        print("[!] Created graph nodes arr with len {}".format(len(self.nodes)))

        for node in self.nodes:

            idx_node = self.find_node_index(node.id)
            print("Avem: {}".format(idx_node))
            # Find possible connected nodes in all 4 directions
            # Down

            dist = 1
            walker_x = node.x
            walker_y = node.y+1

            while node_grid[walker_y][walker_x] != 0:

                if node_grid[walker_y][walker_x] == 2:
                    id_node_2 = get_id(walker_x, walker_y)
                    idx_node_2 = self.find_node_index(id_node_2)
                    self.dTable[idx_node][idx_node_2] = dist
                    print("[!] Created edge between {:2d} - {:2d} with distance: {:4d}".format(idx_node, idx_node_2,
                                                                                               dist))

                walker_y += 1
                dist += 1

            # up

            dist = 1
            walker_x = node.x
            walker_y = node.y - 1

            while node_grid[walker_y][walker_x] != 0:

                if node_grid[walker_y][walker_x] == 2:
                    id_node_2 = get_id(walker_x, walker_y)
                    idx_node_2 = self.find_node_index(id_node_2)
                    self.dTable[idx_node][idx_node_2] = dist
                    print("[!] Created edge between {:2d} - {:2d} with distance: {:4d}".format(idx_node, idx_node_2,
                                                                                               dist))
                walker_y -= 1
                dist += 1

            # right

            dist = 1
            walker_x = node.x + 1
            walker_y = node.y

            while node_grid[walker_y][walker_x] != 0:

                if node_grid[walker_y][walker_x] == 2:
                    id_node_2 = get_id(walker_x, walker_y)
                    idx_node_2 = self.find_node_index(id_node_2)
                    self.dTable[idx_node][idx_node_2] = dist
                    print("[!] Created edge between {:2d} - {:2d} with distance: {:4d}".format(idx_node, idx_node_2,
                                                                                               dist))
                walker_x += 1
                dist +=1

            # left

            dist = 1
            walker_y = node.y
            walker_x = node.x - 1

            while node_grid[walker_y][walker_x] != 0:

                if node_grid[walker_y][walker_x] == 2:
                    id_node_2 = get_id(walker_x, walker_y)
                    idx_node_2 = self.find_node_index(id_node_2)
                    self.dTable[idx_node][idx_node_2] = dist
                    print("[!] Created edge between {:2d} - {:2d} with distance: {:4d}".format(idx_node, idx_node_2,
                                                                                               dist))
                walker_x -= 1
                dist += 1

    def find_node_index(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return self.nodes.index(node)

    def reset(self):
        self.visited = [0 for i in range(self.n_nodes)]
