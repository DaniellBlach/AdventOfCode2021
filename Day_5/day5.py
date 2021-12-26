lines = open('input.txt').read().splitlines()
points = {}


def put_horizontal_to_point(x1, x2, y1):
    start = min(x1, x2)
    end = max(x1, x2) + 1
    for i in range(start, end):
        points[(y1, i)] = points.get((y1, i), 0) + 1


def put_vertical_to_point(x1, y1, y2):
    start = min(y1, y2)
    end = max(y1, y2) + 1
    for i in range(start, end):
        points[(i, x1)] = points.get((i, x1), 0) + 1


def get_points(lines, points):
    for index, line in enumerate(lines):
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        if y1 == y2:
            put_horizontal_to_point(x1, x2, y1)
        if x1 == x2:
            put_vertical_to_point(x1, y1, y2)

    return points


def overlap_lines(points):
    overlap = 0
    for i in points.items():
        if i[1] >= 2:
            overlap += 1
    return overlap


print("Output of the first   part: ", overlap_lines(get_points(lines, points)))
