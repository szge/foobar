def solution(map):
    # try all the possible mazes with removing a wall
    min = 500 # h * w <= 400
    h = len(map)
    w = len(map[0])
    for i in range(h):
        for j in range(w):
            if map[i][j] == 1:
                # copy map
                new_map = [row[:] for row in map]
                new_map[i][j] = 0
                val = solve(new_map)
                if val > 0 and val < min: min = val

    return str(min)

# return the minimum path length to solve the maze otherwise return 0
def solve(map):
    h = len(map)
    w = len(map[0])
    # dfs
    # since the walls are 1s let's start counting distance at 2 then subtract 1 later
    map[0][0] = 2
    def make_step(k):
        free = False
        for i in range(h):
            for j in range(w):
                if map[i][j] == k:
                    if i > 0 and map[i - 1][j] == 0:
                        map[i - 1][j] = k + 1
                        free = True
                    if j > 0 and map[i][j - 1] == 0:
                        map[i][j - 1] = k + 1
                        free = True
                    if i < h - 1 and map[i + 1][j] == 0:
                        map[i + 1][j] = k + 1
                        free = True
                    if j < w - 1 and map[i][j + 1] == 0:
                        map[i][j + 1] = k + 1
                        free = True
        return free
    k = 2
    while map[h - 1][w - 1] == 0:
        if not make_step(k): return 0
        k += 1
    # print(map)
    # print(k - 1)
    return k - 1

if __name__ == "__main__":
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))