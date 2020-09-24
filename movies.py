def read_csv(filename):
	file = open(filename+'.csv', 'r', encoding="UTF-8")
	list_tuples = []
	for data in file:
		split_rows = data.split("\n")
		data_split = split_rows[0].split(",")
		data_tuples = tuple(data_split)
		list_tuples.append(data_tuples)

	return list_tuples

def generate_name_map(nodes):
	map_dict = {}
	for i in range(len(nodes)):
		map_dict[str(i)] = nodes[i][1]

	return map_dict

def name_edges(edges, name_map):
	list_edgeName = []
	for i in range(len(edges)):
		first_element = ""
		second_element = ""
		for indx in name_map:
			if edges[i][0] == indx:
				first_element = name_map[indx]
			elif edges[i][1] == indx:
				second_element = name_map[indx]
		name_tuple = (first_element, second_element, edges[i][2])
		list_edgeName.append(name_tuple)

	return list_edgeName #The list has a length of 208912 and will take long to return 

def generate_movie_dictionary():

	return

def get_actor_friends():

	return

def main():
	read_csv('nodes')
	nodes = read_csv('nodes')
	generate_name_map(nodes)
	name_map = generate_name_map(nodes)
	edges = read_csv('edges')
	name_edges(edges, name_map)
	

	


if __name__ == "__main__":
	main()
