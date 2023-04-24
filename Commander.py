import os

if __name__ == "__main__":
    mission_path = "missions"
    missions = os.listdir(mission_path)
    missions.sort()
    for mission in missions:

        with open(os.path.join(mission_path, mission), "r") as file:
            # lines = file.readlines()
            # file.close()
            trav_grid = []
            cover_grid = []
            ea_grid = []

            for line in file:
                if line == "Trav":
                    ...
