import os
import re

import numpy as np

from A_star import search
from Grid import Grid


def get_array(line_range, lines):
    array_list = []
    for k in line_range:
        line = re.findall("\d", lines[k])
        array_list.append(line)
    return np.array(array_list, dtype=float)


if __name__ == "__main__":
    mission_path = "missions"
    missions = os.listdir(mission_path)
    missions.sort()

    for mission in missions:
        with open(os.path.join(mission_path, mission), "r") as file:
            lines = file.readlines()

            trav_grid = get_array(range(1, 9), lines)  # 8x8
            cover_grid = get_array(range(11, 19), lines)
            ea_grid = get_array(range(21, 29), lines)

            start_position = lines[31].strip().split(", ")  # x,y
            start_position = [int(x) for x in start_position]
            OP_position = lines[34].strip().split(", ")
            OP_position = [int(x) for x in OP_position]

            intent = int(lines[37].strip())  # 0-5

        detection_grid = np.multiply(cover_grid, ea_grid)
        detection_grid = np.multiply(detection_grid, intent/5)  # normalize and implement intent
        trav_grid = np.multiply(trav_grid, 5 - intent)
        combined_grid = np.add(trav_grid, detection_grid)

        grid = Grid(combined_grid)
        path, cost = search(grid, start_position, OP_position)

        print(f"{mission[:-4]}, total costs: {cost}, path: {path}")
