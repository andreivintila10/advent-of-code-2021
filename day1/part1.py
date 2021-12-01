def main():
	filename="data"

	lines = []
	with open(filename, "r") as file:
		for line in file:
			lines.append(int(line.strip()))

	count = 0
	for index in range(1, len(lines)):
		if lines[index - 1] < lines[index]:
			count += 1

	print("Answer is %d" % count)

if __name__ == "__main__":
	main()
