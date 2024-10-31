from queue import PriorityQueue
import copy

class Node():
    def __init__(self, state, parent, empty_cell_position):
        self.state = state 
        self.parent = parent
        self.empty_cell_position = empty_cell_position

def print_path(root):
    if root is None:
        return
     
    print_path(root.parent)
    print(root.state)
    print()

def aStar(initial_state, empty_cell_position, goal_state):
    node = Node(state=initial_state, parent=None, empty_cell_position=empty_cell_position)
    
    frontier = PriorityQueue()
    frontier.put((manhattan(node), node))
    explored = set()

    while not frontier.empty():
        node = frontier.get()[1]
        explored.add(tuple(map(tuple, node.state))) 

        if node.state == goal_state:
            print("GOAL REACHED !!!\n")
            print("Path to goal: ")
            print_path(node)
            return node

        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]

        for i in range(4):
            new_empty_cell_position = [
                node.empty_cell_position[0] + row[i],
                node.empty_cell_position[1] + col[i],
            ]
            
            # Check if the new position is within bounds
            if 0 <= new_empty_cell_position[0] < 3 and 0 <= new_empty_cell_position[1] < 3:
                child = new_node(state=node.state, parent=node, 
                                 empty_cell_position=node.empty_cell_position, 
                                 new_empty_cell_position=new_empty_cell_position)

                # Check if child state has been explored
                if tuple(map(tuple, child.state)) not in explored:
                    frontier.put((manhattan(child), child))

    return None  # Return None if no solution is found

def manhattan(node):
    goal_keys = {
        1: [0, 1],
        2: [0, 2],
        3: [1, 0],
        4: [1, 1],
        5: [1, 2],
        6: [2, 0],
        7: [2, 1],
        8: [2, 2]
    }
    mat = node.state
    cost = 0 
    for i in range(3):
        for j in range(3):
            x = mat[i][j]
            if x == 0:
                continue
            key = goal_keys[x]  # [n,m]
            cost += (abs(i - key[0])) + (abs(j - key[1]))
    return cost

def new_node(state, parent, empty_cell_position, new_empty_cell_position):
    new_state = copy.deepcopy(state)
    x1, y1 = empty_cell_position
    x2, y2 = new_empty_cell_position

    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]

    return Node(state=new_state, parent=parent, empty_cell_position=new_empty_cell_position)

def find_zeros(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return [i, j]

if __name__ == "__main__":
    inital_state = [[1,2,5],[3,4,0],[6,7,8]]
    goal_state = [[0,1,2],[3,4,5],[6,7,8]]

    aStar(initial_state = inital_state, empty_cell_position = find_zeros(inital_state), goal_state = goal_state)