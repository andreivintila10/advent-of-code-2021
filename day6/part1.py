def main():
	fish = []
	with open('data', 'r') as file:
		line = file.readline().strip()
		fish = list(map(lambda timer: int(timer), line.split(',')))
		days = 80
		for day in range(1, days + 1):
			for index in range(len(fish)):
				if fish[index] == 0:
					fish[index] = 6
					fish.append(8)
				else:
					fish[index] -= 1

	count = len(fish)
	print("Answer is %d" % count)


if __name__ == "__main__":
	main()