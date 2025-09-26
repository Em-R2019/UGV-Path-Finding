import os
import sys
import numpy as np
from ast import literal_eval
from A_star import search
from Grid import Grid


if __name__ == "__main__":
    N = sys.argv[1]
    t = int(sys.argv[2])
    T = int(sys.argv[3])
    start_position = literal_eval(sys.argv[4])

    mission_path = "grids"
    missions = os.listdir(mission_path)
    mission = [s for s in missions if N in s][0]
    N = int(N)

    with open(os.path.join(mission_path, mission), "r") as file:
        rows = np.array(file.read().splitlines())
        grid= np.empty((N, N), dtype=int)
        for i, row in enumerate(rows):
            grid[i, :] = [int(i) for i in row.split(" ")]

    grid = Grid(grid)
    path, cost, value = search(grid, start_position, t, T)

    print(f"{mission[:-4]}, total steps: {cost}, value: {value}, path: {path}")
