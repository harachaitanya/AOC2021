

def read_input():

	with open("input.txt") as f:
		depth_list = [int(x.strip()) for x in f]

	return depth_list

def part1(depth_list):
	increased = i = 0

	for i in range(1,len(depth_list)):
		if depth_list[i] > depth_list[i-1]:
			increased += 1

	return increased

def part2(depth_list):
	prev_3_sum = sum(depth_list[:3])
	increased = 0

	for i in range(1,len(depth_list)-2):
		current_3_sum = sum(depth_list[i:i+3])
		#print(prev_3_sum, current_3_sum, i)
		if current_3_sum > prev_3_sum:
			increased += 1

		prev_3_sum = current_3_sum

	return increased

def main():
	depth_list = [199,200,208,210,200,207,240,269,260,263]
	depth_list = read_input()

	num_of_increase = part1(depth_list)
	print(f"Part 1  - num_of_increase is {num_of_increase}")
	num_of_increase = part2(depth_list)
	print(f"Part 2  - num_of_3_sum_increase is {num_of_increase}")

if __name__ == '__main__':
	main()