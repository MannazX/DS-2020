import os

def read_file(filename):
	# write your function here.
	return open(filename, 'r', encoding='utf8').read().splitlines()

def parse_csv_lines(lines):
	# write your function here. It might possibly call other functions you wrote.
	lists = []
	for l in lines:
		lists.append(l.split(','))
	return lists

def parse_delimited_lines(lines, delimiter):
	# write your function here. It might possibly call other functions you wrote.
	lists = []
	for l in lines:
		lists.append(l.split(delimiter))
	return lists

def age_difference(lines) -> [int]:
	# write your function here. It might possibly call other functions you wrote.
	diffs = []

	for ages in lines:
		diffs.append(float(ages[-1]) - float(ages[1]))

	return diffs

def find_unisex_names(male_names, female_names):
	# write your function here. It might possibly call other functions you wrote.
	uniq = []
	for name in male_names:
		if name in female_names:
			uniq.append(name)

	return (uniq)

def build_name_dataset(female_names, male_names, unisex_names):
	# write your function here. It might possibly call other functions you wrote.
	# Should not return anything.
	with open('all_names.csv', 'w', encoding='utf8') as fs:
		for name in female_names:
			gender = 'U' if name in unisex_names else 'F'
			fs.write(f'{name[0]},{gender}\n')

		for name in male_names:
			gender = 'U' if name in unisex_names else 'M'
			fs.write(f'{name[0]},{gender}\n')


def write_sorted_names(names: [[]]) -> None:
	# write your function here. It might possibly call other functions you wrote.

	# Delete all files in data folder to get clean slate.
	[os.remove(f'data/{f}') for f in os.listdir('data')]

	for name in names:
		first = name[0][0].upper()
		with open(f'data/{first}.csv', 'a+') as f:
			f.write(f'{name}\n')

	print("Done")
	return None


def run_tests():
	"""
	sign: string -> [string] - A string for each line.
	"""
	lines_male   = read_file('male_names.csv')
	lines_female = read_file('female_names.csv')
	lines_muni   = read_file('municipalities-2005-2019.csv')

	pretty('Requirement 1', lines_muni)

	"""
	sign: iterable -> [[string, string]]
	"""
	parsed_lines_male   = parse_csv_lines(lines_male)
	parsed_lines_female = parse_csv_lines(lines_female)
	parsed_lines_muni   = parse_csv_lines(lines_muni)

	pretty('Requirement 2', parsed_lines_muni)

	"""
	sign: iterable -> [[string, string]]
	"""
	dparsed_lines_male   = parse_delimited_lines(lines_male, ';')
	dparsed_lines_female = parse_delimited_lines(lines_female, ';')
	dparsed_lines_muni   = parse_delimited_lines(lines_muni, ';')

	pretty('Requirement 3', dparsed_lines_muni)

	"""
	sign: iterable -> [int]
	"""
	age_diff_list = age_difference(dparsed_lines_muni)

	pretty('Requirement 4', age_diff_list)

	"""
	sign: [[string]], [[string]] -> set
	"""
	unisex_names = find_unisex_names(parsed_lines_male, parsed_lines_female)

	pretty('Requirement 5', unisex_names)

	"""
	sign: [[string]], [[string]], (string) -> io
	"""
	build_name_dataset(parsed_lines_female, parsed_lines_male, unisex_names)

	pretty('Requirement 6', 'Build all_names.csv')

	"""
	sign: [[string]] -> io
	"""
	all_names = parse_csv_lines(read_file('all_names.csv'))
	write_sorted_names(all_names)

	pretty('Requirement 7', 'Build data/*')

def pretty(title, content):
	print(f'========================= {title.upper()} =========================')
	print(content)
	print(f'=========================={"*" * len(title)}==========================\n')

def main():
	run_tests()

if __name__ == "__main__":
	# Executes only if run as a script
	main()
