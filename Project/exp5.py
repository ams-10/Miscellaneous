from collections import defaultdict, deque
class Graph:
 	def __init__(self):
 		self.graph = defaultdict(list)

 	def add_edge(self, u, v):
 		self.graph[u].append(v)

 	def bfs(self, start_node):
 		visited = set()
 		queue = deque([start_node])

		while queue:
 			current_node = queue.popleft()

 			if current_node not in visited:
 				print(current_node, end=" ")
 				visited.add(current_node)

 				for neighbor in self.graph[current_node]:
 					if neighbor not in visited:
 						queue.append(neighbor)

# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

start_node = 2
print("Breadth-First Search Traversal starting from node", start_node)
graph.bfs(start_node)