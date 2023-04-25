from math import inf


def get_path(node):
    path = []
    while node is not None:
        path.append(node.location)
        node = node.parent
    path.reverse()
    return path


def search(grid, start, goal):
    open_list = []
    closed_list = []
    current_node = grid.node(start, None)
    open_list.append(current_node)

    while len(open_list) > 0:
        f = inf
        for node in open_list:
            if node.f(goal) < f:
                current_node = node
                f = current_node.f(goal)

        if current_node.location == goal:
            # path, cost = get_path(current_node)
            return get_path(current_node), current_node.g
        else:
            closed_list.append(current_node)
            open_list.remove(current_node)

        neighbours = grid.neighbors(current_node)
        for candidate in neighbours:
            if not candidate.is_in(closed_list):
                if not candidate.is_in(open_list):
                    open_list.append(candidate)
                else:
                    open_node = candidate.get_eq(open_list)
                    if open_node.g > candidate.g:
                        # open_node.g = candidate.g
                        # open_node.parent = candidate.parent
                        open_list.append(candidate)
                        open_list.remove(open_node)

    raise Exception("No path found")

