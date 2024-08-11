def list_operations():
    # Initializing a sample list
    my_list = [1, 2, 3, 4, 5]

    # Displaying the original list
    print("Original List:", my_list)

    # Appending an element to the list
    my_list.append(6)
    print("List after appending 6:", my_list)

    # Inserting an element at a specific position
    my_list.insert(2, 10)
    print("List after inserting 10 at index 2:", my_list)

    # Removing an element by value
    my_list.remove(4)
    print("List after removing element 4:", my_list)

    # Removing an element by index
    popped_element = my_list.pop(1)
    print("List after popping element at index 1:", my_list)
    print("Popped element:", popped_element)

    # Checking if an element exists in the list
    if 3 in my_list:
        print("3 is present in the list.")
    else:
        print("3 is not present in the list.")

    # Sorting the list
    my_list.sort()
    print("Sorted List:", my_list)

    # Reversing the list
    my_list.reverse()
    print("Reversed List:", my_list)

# Calling the list_operations function
list_operations()
