import numpy as np
import copy
import matplotlib.pyplot as plt


class Node:
    def __init__(self, location: [int, int], value: float, parent):
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
    def __init__(self, grid: np.array([])):
        self.grid = grid
        self.width = grid.shape[0]
        self.height = grid.shape[1]

    def in_bounds(self, location) -> bool:
        x, y = location
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, node: Node):
        x, y = node.location

        neighbours = []
        neighbour_locations = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]  # N S W E

        for location in neighbour_locations:
            if self.in_bounds(location):
                neighbours.append(self.node(location, node))

        return neighbours

    def node(self, location: [int, int], parent):
        if self.in_bounds(location):
            x, y = location
            return Node(location, self.grid[y][x], parent)

    def print_path(self, path: []):
        print_grid = copy.deepcopy(self.grid)

        path_color = np.max(print_grid) * 1.2
        for location in path:
            x, y = location
            print_grid[y][x] = path_color

        plt.pcolormesh(print_grid, cmap='gist_yarg')
        plt.show()
