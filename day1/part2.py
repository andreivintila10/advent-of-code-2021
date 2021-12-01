def main():
	filename="data"

	lines = []
	with open(filename, "r") as file:
		for line in file:
			lines.append(int(line.strip()))

	count = 0
	sum1 = sum(lines[:3])
	for index in range(3, len(lines)):
		start = index - 2
		end = start + 3
		sum2 = sum(lines[start:end])

		if sum1 < sum2:
			count+=1

		sum1 = sum2

	print("Answer is %d" % count)

if __name__ == "__main__":
	main()
