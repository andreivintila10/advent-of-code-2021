import collections
import fileinput

def get_points_on_line(line):
    (x1, y1), (x2, y2) = line
    dx = x2 - x1
    dy = y2 - y1

    def get_sign(delta):
        if delta > 0: return 1
        elif delta < 0: return -1
        else: return 0
    x_sign = get_sign(dx)
    y_sign = get_sign(dy)

    delta = max(abs(dx), abs(dy))
    return [(x1 + (i * x_sign), y1 + (i * y_sign)) for i in range(delta+1)]

# Parse input
lines = []
with open("data", "r") as file:
	for l in file:
		line = l.split()
		p1 = tuple(map(int, line[0].split(',')))
		p2 = tuple(map(int, line[2].split(',')))
		lines.append((p1, p2))

# Part 1
tiles = collections.defaultdict(int)
is_straight = lambda l: l[0][0] == l[1][0] or l[0][1] == l[1][1]
for l in filter(is_straight, lines):
    for p in get_points_on_line(l):
        tiles[p] += 1

print('Part 1:', sum(count >= 2 for count in tiles.values()))

# Part 2
is_diagonal = lambda l: not is_straight(l)
for l in filter(is_diagonal, lines):
    for p in get_points_on_line(l):
        tiles[p] += 1

print('Part 2:', sum(count >= 2 for count in tiles.values()))