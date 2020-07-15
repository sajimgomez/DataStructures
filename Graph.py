class Node :

    def __init__(self, value) :

        self.value = value

        self.neighbors = []

        self.visited = False


    def add_neighbor(self, node) :

        self.neighbors += [node]


class Graph :

    def __init__(self, root = None) :

        self.root = root


    def execute_dfs(self) :

        if self.root == None :

            return

        self.root.visited = True

        for neighbor in self.root.neighbors :

            if not neighbor.visited :

                self.execute_dfs(neighbor)


    def make_all_nodes_unvisited_by_dfs(self) :

        if self.root == None :

            return

        self.root.visited = False

        for neighbor in self.root.neighbors :

            if neighbor.visited :

                self.make_all_nodes_unvisited_by_dfs(neighbor)


    def execute_bfs(self) :

        queue = []

        self.root.visited = True

        queue += [self.root]

        while len(queue) != 0 :

            current_node = queue.pop(0)

            for neighbor in current_node.neighbors :

                if not neighbor.visited :

                    neighbor.visited = True

                    queue += [neighbor]


    def make_all_nodes_unvisited_by_bfs(self) :

        queue = []

        self.root.visited = False

        queue += [self.root]

        while len(queue) != 0 :

            current_node = queue.pop(0)

            for neighbor in current_node.neighbors :

                if neighbor.visited :

                    neighbor.visited = False

                    queue += [neighbor]