import random
from datetime import datetime
from math import inf


def get_path(node):
    path = []
    while node is not None:
        path.append(node.location)
        node = node.parent
    path.reverse()
    return path

def get_max_steps(node_list):
    max_steps = 0
    max_node = None
    for node in node_list:
        if node.path_steps > max_steps:
            max_node = node
    return max_node

def end_sequence(current_node, closed_list, open_list, grid, T_step):
    path = get_path(current_node)
    grid.update_working_grid(current_node)
    grid.print_path(path, closed_list, open_list)
    return path, current_node.path_steps, current_node.path_value, T_step

def add_to_open_list(candidate, open_list):
    if not candidate.is_in(open_list):
        open_list.append(candidate)
    else:
        open_node = get_max_steps(candidate.get_eq(open_list))
        if candidate.f > open_node.f and candidate.path_steps > open_node.path_steps + 2:
            open_list.append(candidate)
            open_list.remove(open_node)

def search(grid, start, t, T):
    start_time = datetime.now()

    open_list = []
    closed_list = []

    current_node = grid.node(start, None)
    open_list.append(current_node)

    while len(open_list) > 0:
        # find highest f in open list
        f = -inf
        # random.shuffle(open_list) # to introduce some randomness in case of ties
        for node in open_list:
            if node.f > f:
                current_node = node
                f = current_node.f

        # switch non-goal current node to closed list
        T_step = (datetime.now() - start_time).total_seconds() * 1000
        t_step = len(get_path(current_node))
        if t_step >= t:
            print("Time step limit reached")
            return end_sequence(current_node, closed_list, open_list, grid, T_step)
        elif T_step >= T:
            print("Time limit reached")
            return end_sequence(current_node, closed_list, open_list, grid, T_step)
        else:
            closed_list.append(current_node)
            open_list.remove(current_node)

        # updating the grid to reflect visited nodes
        grid.update_working_grid(current_node)

        open_list = [node for node in open_list if node.path_steps > current_node.path_steps - 10]
        closed_list = [node for node in closed_list if node.path_steps > current_node.path_steps - 10]

        # evaluate neighbours of current node
        neighbours = grid.neighbors(current_node)
        for candidate in neighbours:
            if not candidate.is_in(closed_list):
                add_to_open_list(candidate, open_list)
            else:
                closed_node = get_max_steps(candidate.get_eq(closed_list))
                if candidate.path_steps > closed_node.path_steps + 2:
                    add_to_open_list(candidate, open_list)

    raise Exception("No path found")

