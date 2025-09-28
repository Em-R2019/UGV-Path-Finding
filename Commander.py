import os
import sys
import numpy as np
from Search import search
from Grid import Grid


if __name__ == "__main__":
    N = sys.argv[1]
    t = int(sys.argv[2])
    T = int(sys.argv[3])
    start_position = [int(sys.argv[4]), int(sys.argv[5])]
    increasing = bool(sys.argv[6] == 'True')

    mission_path = "grids"
    missions = os.listdir(mission_path)
    mission = [s for s in missions if N in s][0]
    N = int(N)

    with open(os.path.join(mission_path, mission), "r") as file:
        rows = np.array(file.read().splitlines())
        grid= np.empty((N, N), dtype=int)
        for i, row in enumerate(rows):
            grid[i, :] = [int(i) for i in row.split(" ")]

    grid = Grid(grid, increasing)
    path, cost, value, time = search(grid, start_position, t, T-1)

    print(f"Grid size:{N}, total steps: {cost}, time: {time:.1f}ms score: {value:.1f}, path: {path}")
