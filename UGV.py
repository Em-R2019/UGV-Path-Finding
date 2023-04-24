from operator import attrgetter

import Grid


def get_path(node):
    path = []

    while node is not None:
        path.append(node)
        node = node.parent

    return path.reverse()


class A_star:
    def __init__(self, grid):
        self.grid = Grid.Grid(grid)
        # self.start = start
        # self.goal = goal
        # self.path = self.search(start, goal)

    def search(self, start, goal):
        open_list = []
        closed_list = []
        start = self.grid.node(start, None)
        open_list.append(start)

        while len(open_list) > 0:
            current_node = min(open_list, key=attrgetter('f.()'))

            if current_node.location == goal:
                return get_path(current_node)
            else:
                closed_list.append(current_node)
                open_list.remove(current_node)

            neighbours = self.grid.neighbors(current_node)
            for candidate in neighbours:
                if not candidate.is_in(open_list):
                    open_list.append(candidate)
                else:
                    open_node = candidate.get_eq(open_list)
                    if open_node.g > candidate:
                        open_node.g = candidate.g
                        open_node.parent = candidate.parent
                        
        raise Exception("No path found")

