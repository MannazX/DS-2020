# ex 4 lec 1

n_list = list(range(1, 7))
#print(n_list)

def list_length(n_list):
	length = 0
	print("first line: ", n_list)
	# print("length in the first line is :", length)
	for i in n_list:
		length += 1
		print("second line: ", n_list)
		# print("length here is :", length)
		print("i is :", i)
	return length

#list_length(n_list)
#print("Length of the list is: ", list_length())
    #print("Length of the list is: ", list_length(n_list))

txt = "The list has {price:.0f} elements!"
print(txt.format(price = list_length(n_list)))

