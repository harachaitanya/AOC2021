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
	i = 0
	while len(temp) > 1:
		frequent_binary = Counter((x[i] for x in temp))
		most_common_bit , least_common_bit = frequent_binary.most_common()
		most_common_bit, most_common_bit_value = most_common_bit
		least_common_bit, least_common_bit_value = least_common_bit
		if most_common_bit_value == least_common_bit_value:
			most_common_bit = '1'
		temp = [x for x in temp if x[i] == most_common_bit]

		i += 1

	oxygen_generator_value = int(temp[0],2)

	temp = binary_codes.copy()
	i = 0
	while len(temp) > 1:
		frequent_binary = Counter((x[i] for x in temp))
		most_common_bit , least_common_bit = frequent_binary.most_common()
		most_common_bit, most_common_bit_value = most_common_bit
		least_common_bit, least_common_bit_value = least_common_bit
		if most_common_bit_value == least_common_bit_value:
			least_common_bit = '0'
		temp = [x for x in temp if x[i] == least_common_bit]

		i +=1 

	co2_scrubbing_value = int(temp[0],2)

	return oxygen_generator_value * co2_scrubbing_value





def main():
	binary_codes = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
	binary_codes = read_input()
	#binary_codes = process_codes(binary_codes)
	print(binary_codes)
	power_of_consumption = part1(binary_codes)
	print(f"Part 1  - power_of_consumption is {power_of_consumption}")
	power_of_consumption = part2(binary_codes)
	print(f"Part 2  - power_of_consumption_rating_value is {power_of_consumption}")

if __name__ == '__main__':
	main()