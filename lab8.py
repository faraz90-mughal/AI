# from heapq import heappop, heappush
# # import numpy as np

# # Define the goal state
# GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# # Define possible moves for the empty tile (row, column)
# MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# def heuristic(state):
#     """Calculate the number of misplaced tiles heuristic."""
#     count = 0
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] != GOAL_STATE[i][j] and state[i][j] != 0:
#                 count += 1
#     return count

# def get_neighbors(state):
#     """Generate possible moves from the current state."""
#     zero_pos = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
#     neighbors = []
    
#     for move in MOVES:
#         new_row, new_col = zero_pos[0] + move[0], zero_pos[1] + move[1]
#         if 0 <= new_row < 3 and 0 <= new_col < 3:
#             new_state = [list(row) for row in state]
#             new_state[zero_pos[0]][zero_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_pos[0]][zero_pos[1]]
#             neighbors.append(tuple(tuple(row) for row in new_state))
    
#     return neighbors

# def a_star_search(start_state):
#     """Perform A* search algorithm to solve the 8-puzzle."""
#     start_state = tuple(tuple(row) for row in start_state)
#     if start_state == GOAL_STATE:
#         return []

#     open_list = []
#     heappush(open_list, (heuristic(start_state), 0, start_state, []))
#     closed_set = set()
    
#     while open_list:
#         _, g_cost, current_state, path = heappop(open_list)
        
#         if current_state in closed_set:
#             continue
#         closed_set.add(current_state)
        
#         if current_state == GOAL_STATE:
#             return path
        
#         for neighbor in get_neighbors(current_state):
#             if neighbor not in closed_set:
#                 h_cost = heuristic(neighbor)
#                 heappush(open_list, (g_cost + 1 + h_cost, g_cost + 1, neighbor, path + [neighbor]))
    
#     return None

# # Example usage
# if __name__ == "__main__":
#     start_state = ((1, 2, 3), (4, 5, 6), (7, 0, 8))  # You can change this to any valid 8-puzzle state
#     path = a_star_search(start_state)
    
#     if path is not None:
#         print("Solution path:")
#         for step in path:
#             for row in step:
#                 print(row)
#             print()
#     else:
#         print("No solution found.")


# import heapq

# class Node:
#     def __init__(self, name, heuristic=0):
#         self.name = name
#         self.heuristic = heuristic
#         self.neighbors = []

#     def add_neighbor(self, neighbor, cost):
#         self.neighbors.append((neighbor, cost))

#     def __lt__(self, other):
#         return self.heuristic < other.heuristic

# def greedy_first_search(start_node, goal_node):
#     open_list = []
#     heapq.heappush(open_list, (start_node.heuristic, start_node))
#     came_from = {}
    
#     while open_list:
#         _, current_node = heapq.heappop(open_list)
        
#         if current_node == goal_node:
#             return reconstruct_path(came_from, goal_node)
        
#         for neighbor, _ in current_node.neighbors:
#             if neighbor not in came_from:
#                 came_from[neighbor] = current_node
#                 heapq.heappush(open_list, (neighbor.heuristic, neighbor))
    
#     return None

# def reconstruct_path(came_from, goal_node):
#     path = []
#     while goal_node:
#         path.append(goal_node.name)
#         goal_node = came_from.get(goal_node)
#     return path[::-1]

# # Example usage
# if __name__ == "__main__":
#     # Create nodes with heuristic values
#     a = Node('A', 6)
#     b = Node('B', 5)
#     c = Node('C', 4)
#     d = Node('D', 3)
#     e = Node('E', 2)
#     f = Node('F', 0)
    
#     # Define neighbors
#     a.add_neighbor(b, 1)
#     a.add_neighbor(c, 4)
#     b.add_neighbor(d, 2)
#     c.add_neighbor(d, 1)
#     d.add_neighbor(e, 5)
#     e.add_neighbor(f, 1)

#     # Perform Greedy First Search
#     path = greedy_first_search(a, f)
#     print("Path:", path)


import heapq

class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = []
        self.g_cost = float('inf')  # Cost to reach this node from the start node
        self.parent = None

    def add_neighbor(self, neighbor, cost):
        self.neighbors.append((neighbor, cost))

    def __lt__(self, other):
        return (self.g_cost + self.heuristic) < (other.g_cost + other.heuristic)

def a_star_search(start_node, goal_node):
    open_list = []
    heapq.heappush(open_list, (start_node.heuristic, start_node))
    start_node.g_cost = 0
    came_from = {}
    
    while open_list:
        _, current_node = heapq.heappop(open_list)
        
        if current_node == goal_node:
            return reconstruct_path(came_from, goal_node)
        
        for neighbor, cost in current_node.neighbors:
            tentative_g_cost = current_node.g_cost + cost
            if tentative_g_cost < neighbor.g_cost:
                neighbor.g_cost = tentative_g_cost
                neighbor.parent = current_node
                came_from[neighbor] = current_node
                if neighbor not in open_list:
                    heapq.heappush(open_list, (neighbor.g_cost + neighbor.heuristic, neighbor))
    
    return None

def reconstruct_path(came_from, goal_node):
    path = []
    while goal_node:
        path.append(goal_node.name)
        goal_node = came_from.get(goal_node)
    return path[::-1]

# Example usage
if __name__ == "__main__":
    # Create nodes with heuristic values
    a = Node('A', 6)
    b = Node('B', 5)
    c = Node('C', 4)
    d = Node('D', 3)
    e = Node('E', 2)
    f = Node('F', 0)
    
    # Define neighbors
    a.add_neighbor(b, 1)
    a.add_neighbor(c, 4)
    b.add_neighbor(d, 2)
    c.add_neighbor(d, 1)
    d.add_neighbor(e, 5)
    e.add_neighbor(f, 1)

    # Perform A* Search
    path = a_star_search(a, f)
    print("Path:", path)
