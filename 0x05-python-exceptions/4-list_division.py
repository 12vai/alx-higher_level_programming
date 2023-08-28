#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Takes two lists and creates a new list with the results of division operations.
    Handles errors and prints corresponding messages to stdout.
    """
    new_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("Wrong type")
        except ZeroDivisionError:
            result = 0
            print("Division by zero")
        except IndexError:
            result = 0
            print("Index out of range")
        finally:
            new_list.append(result)
    
    return new_list
