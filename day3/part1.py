def main():
	data = []
	with open("data", "r") as file:
		for line in file:
			data.append(line.strip())

	gamma = ""
	epsilon = ""
	length = len(data[0])
	for i in range(length):
		freq = [0, 0]
		for number in data:
			freq[int(number[i])] += 1

		if freq[1] > freq[0]:
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"

	gamma_number = int(gamma, 2)
	epsilon_number = int(epsilon, 2)

	answer = gamma_number * epsilon_number

	print("Answer is %d" % answer)
			

if __name__ == "__main__":
	main()