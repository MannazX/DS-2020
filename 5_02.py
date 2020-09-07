# ex 4 lec 1

n_list = (1,2,10,4,5,6,9,8)
#print(n_list)

def list_length(n_list):
	length = 0
	print("first line: ", n_list)
	# print("length in the first line is :", length)
	for i in n_list:
		length += 1
		# print("second line: ", n_list)
		# print("length here is :", length)
		# print("i is :", i)
	return length

#list_length(n_list)
#print("Length of the list is: ", list_length())
    #print("Length of the list is: ", list_length(n_list))

#txt = "The list has {price:.0f} elements!"
#print(txt.format(price = list_length(n_list)))

max_item = n_list[0]
print("max item is: ", max_item)
def showMax(n_list):
        max_item = n_list[0]
        for i in n_list:
                print("i in for is : ", i)
                if i > max_item:
                        print("i is: ", i)
                        max_item = i
        return max_item
txt = "The biggest number is the {price:.0f} in the list!"
print(txt.format(price = showMax(n_list)))

