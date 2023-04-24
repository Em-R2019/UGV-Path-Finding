import numpy as np


class Node:
    def __init__(self, location: [int, int], value: int, parent):
        self.location = location
        self.value = value
        self.parent = parent

        if parent is not None:
            self.g = parent.g + value
        else:
            self.g = value

    def h(self, goal):
        x, y = self.location
        dx = goal[0] - x
        dy = goal[1] - y
        return dx ** 2 + dy ** 2

    def f(self, goal):
        h = self.h(goal)
        return self.g + h

    def is_in(self, node_list):
        for node in node_list:
            if node.location == self.location:
                return True
        return False

    def get_eq(self, node_list):
        for node in node_list:
            if node.location == self.location:
                return node
        return None

    def is_eq(self, node):
        if node.location == self.location:
            return True
        else:
            return False


class Grid:
    def __init__(self, grid: np.Array(int)):
        self.grid = grid
        self.width = grid.width
        self.height = grid.height

    def in_bounds(self, node: Node) -> bool:
        x, y = node.location
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, node: Node):
        x, y = node.location
        neighbours = [self.node([x, y - 1], node), self.node([x, y + 1], node), self.node([x - 1, y], node),
                      self.node([x + 1, y], node)]  # N S W E
        return filter(self.in_bounds, neighbours)

    def node(self, location: [int, int], parent):
        return Node(location, self.grid(location), parent)

    def print_path(self, path: []):
        print_grid = self.grid.hardcopy()
        for node in path:
            x, y = node.location
            print_grid[x][y] = "X"

        # First row
        print(f"x>", end='')
        for j in range(self.width):
            print(f"| {j + 1} ", end='')
        print("| ")
        print((self.width * 4 + 4) * "-")

        # Other rows
        for i in range(self.height):
            print(f"{i} ", end='')
            for j in range(self.width):
                print(f"| {print_grid[i][j]} ", end='')
            print("| ")
            print((self.width * 4 + 4) * "-")
        print("y^")
