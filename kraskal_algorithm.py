class KruskalMST:
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def find_min_spanning_tree(self, graph):
        edges = []
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                if graph[i][j] != float('inf'):
                    edges.append((i, j, graph[i][j]))

        edges.sort(key=lambda edge: edge[2])

        parent = [i for i in range(len(graph))]
        rank = [0] * len(graph)
        mst = []

        for edge in edges:
            i, j, weight = edge
            x = self.find(parent, i)
            y = self.find(parent, j)

            if x != y:
                mst.append((i, j, weight))
                self.union(parent, rank, x, y)

        return mst


