# Function to demonstrate list methods
def list_operations():
 	# Initialize a list
 	my_list = [1, 2, 3, 4, 5]

 	# Display the original list
	print("Original List:", my_list)

 	# Add elements using the '+' operator
 	added_list = my_list + [6, 7]
 	print("List after adding elements using '+':", added_list)

 	# Append a single element
 	my_list.append(8)
 	print("List after appending 8:", my_list)

 	# Append multiple elements using extend
 	my_list.extend([9, 10])
 	print("List after extending with [9, 10]:", my_list)

 	# Delete elements using pop
 	popped_element = my_list.pop(1)
 	print("List after popping element at index 1:", my_list)
 	print("Popped element:", popped_element)

 	# Remove an element by value
 	my_list.remove(4)

 print("List after removing element 4:", my_list)