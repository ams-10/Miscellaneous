# Nested list 
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Length of the nested list 
print("Length of the nested list:", len(nested_list)) 

# Concatenation of nested lists 
concatenated_list = nested_list + [[10, 11, 12]] 
print("Concatenated List:", concatenated_list) 

# Membership check 
if [4, 5, 6] in nested_list: 
	print("[4, 5, 6] is present in the nested list.") 
else: 
	print("[4, 5, 6] is not present in the nested list.") 

# Iterating through the elements of the nested list 
print("Iterating through the elements:") 

for sublist in nested_list: for element in sublist: 
	print(element, end=" ") print() 

# Indexing 
print("Element at index [1][2]:", nested_list[1][2]) 

# Slicing 
sliced_list = nested_list[0:2] 
print("Sliced List:", sliced_list)