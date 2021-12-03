import copy

def main():
	data = []
	with open("data", "r") as file:
		for line in file:
			data.append(line.strip())

	data_generator = copy.copy(data)
	data_scrubber = copy.copy(data)
	pos_generator = pos_scrubber = 0
	while len(data_generator) > 1 and pos_generator < len(data_generator[0]):
		data_generator = find_generator_rating(pos_generator, data_generator)
		pos_generator += 1

	while len(data_scrubber) > 1 and pos_scrubber < len(data_scrubber[0]):
		data_scrubber = find_scrubber_rating(pos_scrubber, data_scrubber)
		pos_scrubber += 1

	generator_rating = int(data_generator[0], 2)
	scrubber_rating = int(data_scrubber[0], 2)

	answer = generator_rating * scrubber_rating
	print("Answer is %d" % answer)


def find_generator_rating(pos, data):
	first_pos_zeros = []
	first_pos_ones = []
	for number in data:
		if number[pos] == "1":
			first_pos_ones.append(number)
		else:
			first_pos_zeros.append(number)

	length_ones = len(first_pos_ones)
	length_zeros = len(first_pos_zeros)
	if length_ones > length_zeros:
		return first_pos_ones
	elif length_ones < length_zeros:
		return first_pos_zeros
	else:
		return first_pos_ones

def find_scrubber_rating(pos, data):
	first_pos_zeros = []
	first_pos_ones = []
	for number in data:
		if number[pos] == "1":
			first_pos_ones.append(number)
		else:
			first_pos_zeros.append(number)

	length_ones = len(first_pos_ones)
	length_zeros = len(first_pos_zeros)
	if length_ones < length_zeros:
		return first_pos_ones
	elif length_ones > length_zeros:
		return first_pos_zeros
	else:
		return first_pos_zeros


if __name__ == "__main__":
	main()