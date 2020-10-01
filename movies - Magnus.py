'''Assignment 3, movies by Magnus Sverdrup. Each of the functions are written here and are executed in the main function.'''

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
	for item in nodes:
		map_dict[item[0]] = item[1]

	return map_dict

def name_edges(edges, name_map):
	list_edgeName = []
	for edge in edges:
		objects = name_map[edge[0]], name_map[edge[1]], edge[2]
		list_edgeName.append(objects)
	
	return list_edgeName

def generate_movie_dictionary(named_edges):
	
	movie_dict = {edge[1]: set() for edge in named_edges if edge[2] == "ACTS_IN"}
	for edge in named_edges:
		role = edge[2]
		if role == "ACTS_IN":
			movie_dict[edge[1]].add(edge[0])
	
	return movie_dict

def get_actor_friends(movie_dictionary):
	dict_friendsActor = {actor:set() for movie in movie_dictionary for actor in movie_dictionary[movie]}
	for movie in movie_dictionary:
		for key_actor in movie_dictionary[movie]: 
			for friend_actors in movie_dictionary[movie]:
				value_set = dict_friendsActor[key_actor]
				value_set.add(friend_actors)
				dict_friendsActor[key_actor] = value_set
			dict_friendsActor[key_actor].remove(key_actor)

	return dict_friendsActor
	

def main():
	read_csv('nodes')
	nodes = read_csv('nodes')
	generate_name_map(nodes)
	name_map = generate_name_map(nodes)
	edges = read_csv('edges')
	name_edges(edges, name_map)
	named_edges = name_edges(edges, name_map)
	generate_movie_dictionary(named_edges)
	movie_dict = generate_movie_dictionary(named_edges)
	print(len(movie_dict))
	get_actor_friends(movie_dict)
	actor_friends = get_actor_friends(movie_dict)
	print(len(actor_friends))
	print("DONE!")

if __name__ == "__main__":
	main()
