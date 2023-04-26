import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, colors


def get_locations(node_list):
    location_list = []
    for node in node_list:
        location_list.append(node.location)
    return location_list


class Node:
    def __init__(self, location: [int, int], value: float, parent):
        self.location = location  # [x,y]
        self.value = value
        self.parent = parent

        if parent is not None:
            self.g = parent.g + value + 1
        else:
            self.g = value + 1

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

    def print_path(self, path: [], closed_list: [], open_list: []):
        print_grid = np.zeros_like(self.grid)

        path_color = 15
        closed_color = 10
        open_color = 5

        closed_list = get_locations(closed_list)
        open_list = get_locations(open_list)

        cmap = colors.ListedColormap(['white', 'darkgray', 'dimgray', 'black'])
        bounds = [0, 5, 10, 15, 20]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        # plot accessed nodes
        for i in range(self.height):
            for j in range(self.width):
                if [j, i] in path:
                    print_grid[i][j] = path_color
                elif [j, i] in closed_list:
                    print_grid[i][j] = closed_color
                elif [j, i] in open_list:
                    print_grid[i][j] = open_color

        plt.imshow(print_grid, cmap=cmap, norm=norm)

        # print grid values
        for i in range(self.width):
            for j in range(self.height):
                if [i, j] in path:
                    plt.text(i - 0.1, j + 0.1, str(round(self.grid[j][i], 2)), color='w')
                else:
                    plt.text(i - 0.1, j + 0.1, str(round(self.grid[j][i], 2)))

        # create a patch (proxy artist) for every color
        p = [patches.Patch(color='white', label="not accessed".format(l=0)),
             patches.Patch(color='darkgray', label="open list".format(l=5)),
             patches.Patch(color='dimgray', label="closed list".format(l=10)),
             patches.Patch(color='black', label="path".format(l=15)), ]

        plt.legend(handles=p, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
        plt.tight_layout()
        plt.show()
