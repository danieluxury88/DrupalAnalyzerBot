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
