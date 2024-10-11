class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            # 만약 무방향 그래프를 원하면 아래 줄의 주석 제거
            # self.graph[node2].append(node1)

    def __repr__(self):
        graph_str = ""
        for node in self.graph:
            graph_str += f"{node} -> {self.graph[node]}\n"
        return graph_str

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        traversal = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                traversal.append(node)
                visited.add(node)
                queue.extend([n for n in self.graph[node] if n not in visited])

        return traversal

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        traversal = [start_node]

        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                traversal.extend(self.dfs(neighbor, visited))

        return traversal


if __name__ == "__main__":

    graph = Graph()
    nodes = ['A', 'B', 'C', 'D', 'E']

    for node in nodes:
        graph.add_node(node)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'D')

    print("Graph Representation:")
    print(graph)

    # print("BFS Traversal from A:", graph.bfs('A'))
    # print("DFS Traversal from A:", graph.dfs('A'))
