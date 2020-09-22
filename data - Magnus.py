'''Assignment 2, data.py by Magnus Sverdrup. The functions for each part of the assignment is defined here. Each of them are run in the main() function.'''

def read_file(filename):
	list_names = []
	file = open(filename, 'r')
	for data in file:
		data_name = data.split('\n')
		for i in range(len(data_name)):
			if data_name[i] != '':
				list_names.append(data_name[i])
	file.close() 

	return list_names

def parse_csv_lines(lines):
	list_lines = []
	for names in lines:
		list_lines.append(names.split(";"))

	return list_lines

def parse_delimited_lines(lines, delimiter):
	delimeter_list = []
	for line in lines:
		string = line[0]
		delimeter_list.append(string.split(delimiter))

	return delimeter_list

def age_difference(lines):
	list_ageChange = []
	for line in lines:
		mean_age2005 = float(line[1])
		mean_age2019 = float(line[-1])
		mean_difference = mean_age2019 - mean_age2005
		list_ageChange.append(mean_difference)

	return list_ageChange

def find_unisex_names(male_names, female_names):
	set_unisexNames = set()
	set_maleName = set()
	set_femaleName = set()
	for name in male_names:
		male_name = name[0]
		set_maleName.add(male_name)
	for name in female_names:
		female_name = name[0]
		set_femaleName.add(female_name)
	for name in set_maleName:
		if name in set_femaleName:
				set_unisexNames.add(name)

	return set_unisexNames

def build_name_dataset(female_names, male_names, unisex_names):
	file = open("all_names.csv", 'w', encoding="UTF-8")
	for name in male_names:
		name_column = name[0]+",M"
		file.write(name_column+"\n")
	for name in female_names:
		name_column = name[0]+",F"
		file.write(name_column+"\n")
	for name in unisex_names:
		name_column = name[0]+",U"
		file.write(name_column+"\n")
	file.close()

	return None

def write_sorted_names(names):
	set_firstletter = set()
	for name in names:
		set_firstletter.add(name[0][0])
	for fileName in set_firstletter:
		files = open(fileName+".csv", 'w')
		for name in names:
			if name[0][0] == fileName:
				files.write(name[0]+"\n")
		files.close()

	print("Done")
	return None

def main():
	# Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.
	filename = input("Enter the name of the file: ") + ".csv"
	read_file(filename)

	lines = read_file(filename)
	parse_csv_lines(lines)

	lines_list = parse_csv_lines(lines)
	delimiter = input("Enter the desired delimiter here: ")
	parse_delimited_lines(lines_list, delimiter)
	
	names = read_file("municipalities-2005-2019.csv")
	lines = parse_csv_lines(names)
	age_difference(lines)
	
	string_male = read_file("male_names.csv")
	male_names = parse_csv_lines(string_male)
	string_female = read_file("female_names.csv")
	female_names = parse_csv_lines(string_female)
	find_unisex_names(male_names, female_names)
	
	unisex_names = find_unisex_names(male_names, female_names)
	build_name_dataset(male_names, female_names, unisex_names)
	
	all_names = read_file("all_names.csv")
	names = parse_csv_lines(all_names)
	write_sorted_names(names)

if __name__ == "__main__":
	# Executes only if run as a script
	main()
