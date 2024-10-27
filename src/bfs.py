from queue import Queue
from collections import deque
import copy

"""
Breadth First Search 

BFS --> search using queue => First in First out (FIFO)

An instance of the 8-puzzle game consists of a board holding 8 distinct movable tiles, plus an empty space. 
For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it.
In this assignment, the blank space is going to be represented with the number 0. 

initial node => 1,2,5,3,4,0,6,7,8 ===== [[1,2,5],[3,4,0],[6,7,8]]

|1|2|5|
|3|4|0|
|6|7|8|

Goal node => 0,1,2,3,4,5,6,7,8 ===== [[0,1,2],[3,4,5],[6,7,8]]
|0|1|2|
|3|4|5|
|6|7|8|

"""
class Node():
    """
    A node in the tree is represented by a data structure with many components:

    node.STATE => the state to which the node corresponds. 
    node.PARENT => the node in the tree that generated this node.
    node.ACTION => the action that was applied to the parent's state to generate this node.
    
    """

    def __init__(self, state, parent,empty_cell_position):
        self.state = state 
        self.parent = parent
        self.empty_cell_position = empty_cell_position


def printMatrix(mat):
     print(mat)

def print_path(root):
    if root == None:
        return
     
    print_path(root.parent)
    printMatrix(root.state)
    print()


def Breadth_First_Search(initial_state, empty_cell_position, goal_state):

        node = Node(state = initial_state, parent = None,empty_cell_position = empty_cell_position)
        
        if node.state == goal_state:
             return node.state
        
        frontier =  Queue()
        frontier.put(node)
        explored = set()

        while not frontier.empty():
             
             node = frontier.get() #pop 
             explored.add(tuple(map(tuple,node.state))) 

             if node.state == goal_state:
                   print("GOAL REACHED !!!\n")
                   print("Path to goal: " )
                   print_path(node)

                   return node
             """
               Generate the possible children 
               we move left right down up 
               left right => change in column only
               ==>> when it moves left the column - 1
               ==>> when it moves right the column + 1 
               down up => change in row only 
               ==>> when it moves up the row - 1 
               ==>> when it moves down the row + 1  

               so we can generate like this row [-1,1,0,0] ----- col [0,0,-1,1] 
             """
             row = [-1,1,0,0]
             col = [0,0,-1,1]

             for i in range(4):
                  new_empty_cell_position = [
                              node.empty_cell_position[0] + row[i],
                              node.empty_cell_position[1] + col[i],]
                  
                  if(new_empty_cell_position[0] < 3 and new_empty_cell_position[1] < 3):
                       child = new_node(state = node.state, parent = node , 
                                        empty_cell_position= node.empty_cell_position, new_empty_cell_position=new_empty_cell_position)
                       
                       frontier.put(child)
                       
                  


             
          


def new_node(state,parent,empty_cell_position,new_empty_cell_position):
     """
     Generate the possible children 
     we move left right down up 
     left right => change in column only
     ==>> when it moves left the column - 1
     ==>> when it moves right the column + 1 
     down up => change in row only 
     ==>> when it moves up the row - 1 
     ==>> when it moves down the row + 1  

     so we can generate like this row [-1,1,0,0] ----- col [0,0,-1,1] 
     """
     new_state = copy.deepcopy(state)
     x1 = empty_cell_position[0]
     y1 = empty_cell_position[1]
     x2 = new_empty_cell_position[0]
     y2 = new_empty_cell_position[1]

     new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]

     newNode = Node(state = new_state, parent = parent,empty_cell_position = new_empty_cell_position)

     return newNode






                    
                    
             


def find_zeros(state):
     for i in range(0,3):
          for j in range(0,3):
               if state[i][j] == 0:
                    empty_cell_position = [i,j]
                    return empty_cell_position


if __name__ == "__main__":

     inital_state = [[1,2,5],[3,4,0],[6,7,8]]
     goal_state = [[0,1,2],[3,4,5],[6,7,8]]

     Breadth_First_Search(initial_state=inital_state,empty_cell_position = find_zeros(inital_state),goal_state=goal_state )

          


     







