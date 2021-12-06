from collections import Counter, defaultdict

def main():
	fish = []
	with open('data', 'r') as file:
		line = file.readline().strip()
		fish = dict(Counter(map(lambda timer: int(timer), line.split(','))))
		days = 256
		for day in range(1, days + 1):
			newValues = defaultdict(int)
			for current in fish:
				if current == 0:
					newValues[6] += fish[current]
					newValues[8] += fish[current]
				else:
					newValues[current - 1] += fish[current]

			fish = newValues

	count = sum(fish.values())
	print("Answer is %d" % count)


if __name__ == "__main__":
	main()