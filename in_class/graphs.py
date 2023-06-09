from stacks import Stack
from queue import Queue

class Arc:
    def __init__(self, start, end, weight=None):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = nodes
        self.arcs = arcs
        self.adj_matrix = self.adj_matrix()

    def adj_matrix(self):
        pass

    """def depth_first_search(self):
        paths = []
        my_stack = Stack()
        start_node = self.nodes[0]
        tail_nodes = self.nodes[1::]
        target_node = input(f"Pick the target node: " + "".join([f"{i}, " if tail_nodes.index(i) != len(tail_nodes)-1 else f"{i}" for i in tail_nodes]) + ": ")
        current_node = start_node
        visited_nodes = []

        def recursion(self):
            pass"""

    def breadth_first_search(self):
        my_queue = Queue(len(self.nodes))
        current_node = self.nodes[0]
        nodes_to_visit = self.nodes[1:]
        my_queue.put(current_node)
        while True:
            for arc in self.arcs:
                if arc.start == current_node and arc.end in nodes_to_visit:
                    current_node = arc.end
                    my_queue.put(current_node)
                    nodes_to_visit.remove(current_node)
                    
            my_queue.get()
            print(str(my_queue))
            if not nodes_to_visit: break

my_graph = Graph(
    ["1", "2", "3", "4", "5"],
    [Arc("1", "2"), Arc("1", "3"), Arc("1", "5"), 
    Arc("2", "4"), Arc("3", "5"), Arc("3", "4"), Arc("4", "5")]
)

my_graph.breadth_first_search()