triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

triangle = triangle.strip()
triangle = [[int(i) for i in k.split(' ')] for k in triangle.split('\n')]

[
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

[
        [75],
      [95, 64],
    [17, 47, 82],
  [18, 35, 87, 10]
]

pos = (
    ([0, 0], [1, 0], [2, 0], [3, 0]),
    ([0, 0], [1, 0], [2, 0], [3, 1]),
    ([0, 0], [1, 0], [2, 1], [3, 1]),
    ([0, 0], [1, 0], [2, 1], [3, 2]),

    ([0, 0], [1, 1], [2, 1], [3, 1]),
    ([0, 0], [1, 1], [2, 1], [3, 2]),
    ([0, 0], [1, 1], [2, 2], [3, 2]),
    ([0, 0], [1, 1], [2, 2], [3, 3])
)


def make_smaller_triangle(pos_of_start, height):
    y, x = pos_of_start[0], pos_of_start[1]

    length = len(triangle)
    if y + height > length:
        height = length - y

    return [[triangle[y+i][x+k] for k in range(i+1)] for i in range(height)]


def triangle_paths(triangle):
    triangle = triangle[::-1]
    height = len(triangle)
    half_paths = [[] for i in range(2**(height-1)//2)]
    for i in range(height-1):
        if i == 0:
            half_paths


def max_path(triangle):
    height = len(triangle)
    max_sum = 0
    for coords in pos:
        temp = []
        for y, x in coords:
            temp.append(triangle[y][x])

        s = sum(temp)
        if s > max_sum:
            max_sum = s

    return max_sum


small_triangle = make_smaller_triangle([0, 0], 4)
print(max_path(triangle))
# print(small_triangle)
# print(triangle_paths(small_triangle))
