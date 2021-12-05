def main():
	segments = []
	max_x = max_y = 0
	with open("data", "r") as file:
		for line in file:
			line = line.split()
			p1 = line[0].split(',')
			p2 = line[2].split(',')
			segment = [{'x': int(p1[0]), 'y': int(p1[1])}, {'x': int(p2[0]), 'y': int(p2[1])}]
			segments.append(segment)

			max_x = max(max_x, maxAxis('x', segment))
			max_y = max(max_y, maxAxis('y', segment))

	diagram = []
	for row in range(max_y + 1):
		diagram.append([0] * (max_x + 1))

	for segment in segments:
		upateDiagram(diagram, segment)

	score = calculateScore(diagram)
	print("Answer is %d" % score)

def upateDiagram(diagram, segment):
	fixed_axis = points_axis = ''
	if segment[0]['x'] == segment[1]['x']:
		fixed_axis = 'x'
		points_axis = 'y'
	elif segment[0]['y'] == segment[1]['y']:
		fixed_axis = 'y'
		points_axis = 'x'
	else:
		return

	for point in range(minAxis(points_axis, segment), maxAxis(points_axis, segment) + 1):
		if fixed_axis == 'x':
			diagram[point][segment[0]['x']] += 1
		else:
			diagram[segment[0]['y']][point] += 1

def calculateScore(diagram):
	count = 0
	for y in range(len(diagram)):
		for x in range(len(diagram[y])):
			if diagram[y][x] > 1:
				count += 1

	return count

def minAxis(axis, segment):
	return min(segment[0][axis], segment[1][axis])

def maxAxis(axis, segment):
	return max(segment[0][axis], segment[1][axis])


if __name__ == "__main__":
	main()