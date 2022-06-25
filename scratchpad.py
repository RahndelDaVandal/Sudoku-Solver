import numpy as np

nums = [1, 2, 3]
line = []
board = []

for s in range(3):
    for _ in range(len(nums)):
        for n in nums:
            for i in range(3):
                line.append(n)
        board.append(line)
        line = []
    nums = [i+3 for i in nums]


arr = np.array(board)

# (rows, cols)
# (0:3,0:3),(0:3,3:6),(0:3,6:9)
# (3:6,0:3),(3:6,3:6),(3:6,6:9)
# (6:9,0:3),(6:9,3:6),(6:9,6:9)

base = 3
rows = range(base)
cols = range(base)

rx = 0
ry = base
cx = 0
cy = base

for row in rows:
    for col in cols:
        # print(arr[rx:ry, cx:cy])
        pass
        cx += base
        cy += base
    rx += base
    ry += base
    cx = 0
    cy = base

x = [0, 3, 6]
y = [3, 6, 9]
