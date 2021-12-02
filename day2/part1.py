def main():
	instructions = []
	with open("data", "r") as file:
		for line in file:
			tokens = line.split()
			instruction = {
				"direction": tokens[0],
				"steps": int(tokens[1])
			}
			instructions.append(instruction)

	horizPos = 0
	depth = 0
	for instruction in instructions:
		match instruction["direction"]:
			case 'forward':
				horizPos += instruction["steps"]
			case 'up':
				depth -= instruction["steps"]
			case 'down':
				depth += instruction["steps"]
			case '_':
				print("Unknown case")

	answer = horizPos * depth
	print("Answer is %d" % answer)


if __name__ == "__main__":
	main()