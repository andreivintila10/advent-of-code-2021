def main():
	boards = []
	numbers = []
	with open("data", "r") as file:
		first_line = file.readline().strip()
		numbers = list(map(lambda number: int(number), first_line.split(',')))
		skip = file.readline()
		ok = 1
		while True:
			board = {
				'matrix': [],
				'cols_set': [0] * 5,
				'rows_set': [0] * 5
			}
			for row in range(5):
				line = file.readline()
				if line == '':
					ok = 0
					break
				board_row = list(map(lambda cols: { 'value': int(cols), 'set': 0 }, line.split()))
				board['matrix'].append(board_row)
			if ok == 0:
				break
			boards.append(board)
			skip = file.readline()

		for number in numbers:
			ok = 0
			for board in boards:
				score = checkBoard(board, number)
				if score:
					print("Answer is %d" % score)
					ok = 1
					break
			if ok:
				break

def checkBoard(board, number):
	for row in range(len(board['matrix'])):
		for column in range(len(board['matrix'][row])):
			if board['matrix'][row][column]['value'] == number and not board['matrix'][row][column]['set']:
				board['matrix'][row][column]['set'] = 1
				board['rows_set'][row] += 1
				board['cols_set'][column] += 1

	for index in range(5):
		if board['rows_set'][index] == 5:
			score = sum_unmarked(board)
			return score * number

	for index in range(5):
		if board['cols_set'][index] == 5:
			score = sum_unmarked(board)
			return score * number

	return 0

def sum_unmarked(board):
	sum = 0
	for row in range(len(board['matrix'])):
		for column in range(len(board['matrix'][row])):
			if not board['matrix'][row][column]['set']:
				sum += board['matrix'][row][column]['value']

	return sum

if __name__ == "__main__":
	main()