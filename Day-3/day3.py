from collections import Counter

def read_input():

	with open("input.txt") as f:
		binary_codes = [x.strip() for x in f]
	
	return binary_codes

#def process_codes(binary_codes):
#return [list(map(int, x)) for x in binary_codes]


def part1(binary_codes):
	
	most_common = least_common = ""
	for i in range(len(binary_codes[0])):
		frequent_binary = Counter((x[i] for x in binary_codes))
		most_common_bit , least_common_bit = frequent_binary.most_common()
		most_common += most_common_bit[0]
		least_common += least_common_bit[0]

	power_of_consumption = int(most_common,2) * int(least_common,2)
	
	return power_of_consumption


def part2(binary_codes):
	
	temp = binary_codes.copy()

	print(sorted(binary_codes))

	most_common = least_common = ""
	j = 0
	while len(temp) > 1:
		frequent_binary = Counter((x[i] for x in temp))
		most_common_bit , least_common_bit = frequent_binary.most_common()
		most_common += most_common_bit[0]
		least_common += least_common_bit[0]
		temp = 





def main():
	binary_codes = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
	#binary_codes = read_input()
	#binary_codes = process_codes(binary_codes)
	print(binary_codes)
	power_of_consumption = part1(binary_codes)
	print(f"Part 1  - power_of_consumption is {power_of_consumption}")
	power_of_consumption = part2(binary_codes)
	#print(f"Part 2  - num_of_3_sum_increase is {num_of_increase}")

if __name__ == '__main__':
	main()