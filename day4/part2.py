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
				'win': 0,
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

		total_no_of_boards = len(boards)
		no_of_winner_boards = 0
		last_score = 0
		for number in numbers:
			for board in boards:
				if board['win']:
					continue

				score = checkBoard(board, number)
				if score:
					no_of_winner_boards += 1
					last_score = score

		print("Answer is %d" % last_score)

def checkBoard(board, number):
	for row in range(len(board['matrix'])):
		for column in range(len(board['matrix'][row])):
			if board['matrix'][row][column]['value'] == number and not board['matrix'][row][column]['set']:
				board['matrix'][row][column]['set'] = 1
				board['rows_set'][row] += 1
				board['cols_set'][column] += 1

	for index in range(5):
		if board['rows_set'][index] == 5:
			board['win'] = 1
			score = sum_unmarked(board)
			return score * number

	for index in range(5):
		if board['cols_set'][index] == 5:
			board['win'] = 1
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