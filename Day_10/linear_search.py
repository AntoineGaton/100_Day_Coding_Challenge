def linear_search(arr, target):
    """
    Perform a linear search to find the target element in the given list.

    :param arr: The list to search within.
    :param target: The element to find.
    :return: The index of the target element if found, -1 if not found.
    """
    for i in range(len(arr)):
        # Iterate through each element of the list.
        if arr[i] == target:
            # If the current element matches the target element, return its index.
            return i
    # If the target element is not found in the list, return -1.
    return -1

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_element = 9

# Perform a linear search to find the target_element in the list.
result = linear_search(my_list, target_element)

if result != -1:
    print(f"{target_element} found at index {result}")
else:
    print(f"{target_element} not found in the list.")