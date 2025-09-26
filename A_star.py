from datetime import datetime
from math import inf


def get_path(node):
    path = []
    while node is not None:
        path.append(node.location)
        node = node.parent
    path.reverse()
    return path


def search(grid, start, t, T):
    start_time = datetime.now()
    t_step = 0

    open_list = []
    closed_list = []

    current_node = grid.node(start, None)
    open_list.append(current_node)

    while len(open_list) > 0:
        # find highest f in open list
        f = -inf
        for node in open_list:
            if node.f > f:
                current_node = node
                f = current_node.f

        # switch non-goal current node to closed list
        T_step = (datetime.now() - start_time).total_seconds() / 1000
        t_step += 1
        if t_step >= t or T_step >= T:
            print("Time limit reached")
            path = get_path(current_node)
            grid.print_path(path, closed_list, open_list)
            return path, current_node.g
        else:
            closed_list.append(current_node)
            open_list.remove(current_node)

        # evaluate neighbours of current node
        neighbours = grid.neighbors(current_node)
        for candidate in neighbours:
            if not candidate.is_in(closed_list):
                if not candidate.is_in(open_list):
                    open_list.append(candidate)
                else:
                    open_node = candidate.get_eq(open_list)
                    if open_node.g > candidate.g:
                        open_list.append(candidate)
                        open_list.remove(open_node)

    print("Path limit reached")
    path = get_path(current_node)
    grid.print_path(path, closed_list, open_list)
    return path, current_node.g, current_node.h
    # raise Exception("No path found")

