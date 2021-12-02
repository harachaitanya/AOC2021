from itertools import groupby

def read_input():

	with open("input.txt") as f:
		instructions = [x.strip() for x in f]

	return instructions

def process_instructions(instructions):
	return [(x.split()[0],int(x.split()[1])) for x in instructions]

def part1(instructions):
	forward = depth = 0

	for op, val in instructions:
		if op == 'forward':
			forward += val
		elif op == 'down':
			depth += val
		elif op == 'up':
			depth -= val

	return forward * depth

	

def part2(instructions):
	forward = aim = depth = 0

	for op, val in instructions:
		if op == 'forward':
			forward += val
			depth += aim * val
		elif op == 'down':
			aim += val
		elif op == 'up':
			aim -= val


	return forward * depth

def main():
	#instructions = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']
	instructions = read_input()

	instructions = process_instructions(instructions)
	#print(instructions)
	final_position_product = part1(instructions)
	print(f"Part 1  - final_position_product is {final_position_product}")
	final_position_depth_product = part2(instructions)
	print(f"Part 2  - final_position_depth_product is {final_position_depth_product}")


if __name__ == '__main__':
	main()