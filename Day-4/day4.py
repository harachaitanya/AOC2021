def read_input(filename):
	boards = []
	board_complete = False
	board_index = 0
	temp_board = []
	with open(filename) as f:
		
		for i, line in enumerate(f.readlines()):
			if i==0:
				random_numbers = list(map(int,line.strip().split(',')))
			elif line.strip() == "":
				continue
			else:
				if len(temp_board) != 5:
					temp_board.append(list(map(int, line.strip().split())))
				elif len(temp_board) == 5:
					boards.append(temp_board)
					temp_board = []
					temp_board.append(list(map(int, line.strip().split())))

	if len(temp_board) == 5:
		boards.append(temp_board)

	return random_numbers, boards

#def process_codes(binary_codes):
#return [list(map(int, x)) for x in binary_codes]

def check_bingo(boards_metadata):
	for idx, board_metadata in enumerate(boards_metadata):
		#Check row wise bingo
		for i in range(5):
			if all(board_metadata[1][(i,j)]==1 for j in range(5)):
				return idx

		#Check column wise bingo
		for j in range(5):
			if all(board_metadata[1][(i,j)]==1 for i in range(5)):
				return idx

	return -1

def check_bingo_2(boards_metadata, won_boards):
	idxs = []
	for idx, board_metadata in enumerate(boards_metadata):
		#Check row wise bingo
		for i in range(5):
			if all(board_metadata[1][(i,j)]==1 for j in range(5)) and idx not in won_boards:
				won_boards[idx] = 1
				idxs.append(idx)

		#Check column wise bingo
		for j in range(5):
			if all(board_metadata[1][(i,j)]==1 for i in range(5)) and idx not in won_boards:
				won_boards[idx] = 1
				idxs.append(idx)

	return idxs if len(idxs) > 0 else -1

def part1(random_numbers, boards):
	boards_metadata = []

	for board in boards:
		value_pos = {}
		pos_mark = {}

		for i, sub_board in enumerate(board):
			for j, value in enumerate(sub_board):
				pos_mark[(i,j)] = 0
				value_pos[value] = (i,j)

		boards_metadata.append([value_pos, pos_mark])

	#print(boards_metadata)

	for number in random_numbers[:5]:
		for i, _ in enumerate(boards_metadata):
			if number in boards_metadata[i][0]:
				pos = boards_metadata[i][0][number]
				boards_metadata[i][1][pos] = 1

	#print("meta###\n",boards_metadata)
	bingo_idx = check_bingo(boards_metadata)
	if bingo_idx != -1:
		final_score = number * sum(value for value, pos in boards_metadata[bingo_idx][0].items() if boards_metadata[bingo_idx][1][pos] == 0)
		return final_score

	for number in random_numbers[5:]:
		for i, _ in enumerate(boards_metadata):
			if number in boards_metadata[i][0]:
				pos = boards_metadata[i][0][number]
				boards_metadata[i][1][pos] = 1
		
		bingo_idx = check_bingo(boards_metadata)

		if bingo_idx != -1:
			final_score = number * sum(value for value, pos in boards_metadata[bingo_idx][0].items() if boards_metadata[bingo_idx][1][pos] == 0)
			return final_score

		
def part2(random_numbers, boards):
	boards_metadata = []
	won_boards = {}
	for board in boards:
		value_pos = {}
		pos_mark = {}

		for i, sub_board in enumerate(board):
			for j, value in enumerate(sub_board):
				pos_mark[(i,j)] = 0
				value_pos[value] = (i,j)

		boards_metadata.append([value_pos, pos_mark])

	#print(boards_metadata)

	for number in random_numbers[:5]:
		for i, _ in enumerate(boards_metadata):
			if number in boards_metadata[i][0]:
				pos = boards_metadata[i][0][number]
				boards_metadata[i][1][pos] = 1

	#print("meta###\n",boards_metadata)
	bingo_idx = check_bingo_2(boards_metadata, won_boards)
	if bingo_idx != -1:
		final_score = number * sum(value for value, pos in boards_metadata[bingo_idx][0].items() if boards_metadata[bingo_idx][1][pos] == 0)
		return final_score

	bingoed_boards = []
	for number in random_numbers[5:]:
		for i, _ in enumerate(boards_metadata):
			if number in boards_metadata[i][0]:
				pos = boards_metadata[i][0][number]
				boards_metadata[i][1][pos] = 1
		
		bingo_idx = check_bingo_2(boards_metadata, won_boards)

		if bingo_idx != -1:
			print(bingo_idx, number, len(won_boards), len(boards), won_boards)
			if len(won_boards) == len(boards):
				bingo_idx = bingo_idx[-1]
				final_score = number * sum(value for value, pos in boards_metadata[bingo_idx][0].items() if boards_metadata[bingo_idx][1][pos] == 0)
				return final_score
	
	


def main():
	#random_numbers, boards = read_input("sample_input.txt")
	random_numbers, boards = read_input("input.txt")
	#binary_codes = process_codes(binary_codes)
	print(random_numbers)
	print(boards)
	part1_final_score = part1(random_numbers, boards)
	print(f"Part 1  - part1_final_score is {part1_final_score}")
	part2_final_score = part2(random_numbers, boards)
	print(f"Part 2  - part2_final_score is {part2_final_score}")

if __name__ == '__main__':
	main()