#!/usr/bin/python3
def list_division(my_list_1 my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of element list_length containing all the the divisions
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list[i] / my_list_2[i]
        except TypeError:
            print("wrong Type")
            div = 0
        except ZeroDivisionError:
            print("division in 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)        
