def sort_data(data, column_index=0, descending=False):
    """Sort a list of tuples based on the specified column index and order.

    Args:
        data (list of tuple): Data to sort.
        column_index (int): Index of the tuple to sort by.
        descending (bool): Set to True for descending order, False for ascending order.

    Returns:
        list of tuple: Sorted data.
    """
    return sorted(data, key=lambda x: x[column_index], reverse=descending)

def sort_list_alphabetically(input_list, descending=False):
    """
    Sort a list of strings alphabetically.

    Args:
        input_list (list of str): The list to be sorted.
        descending (bool): Set to True for descending order, False for ascending order (default).

    Returns:
        list of str: The sorted list.
    """
    return sorted(input_list, reverse=descending)

def filter_list_by_string(elements, search_string):
    """
    Filters a list of strings, returning only those that contain a specific substring.

    Args:
        elements (list of str): The list of strings to filter.
        search_string (str): The substring to search for within the elements.

    Returns:
        list of str: A list containing only the elements that include the search string.
    """
    # Normalize the search string to lowercase to perform a case-insensitive match
    search_string = search_string.lower()

    # Use a list comprehension to filter elements
    filtered_list = [element for element in elements if search_string in element.lower()]

    return filtered_list
