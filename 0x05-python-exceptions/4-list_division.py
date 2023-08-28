#!/usr/bin/python3

def list_division(list_1, list_2, length):
    """
    Takes two lists and creates a new list with the results of division operations.
    Handles errors and prints corresponding messages to stdout.
    """
    new_list = []

    for i in range(length):
        try:
            result = list_1[i] / list_2[i]
        except TypeError:
            result = 0
            print("Error: Wrong type")
        except ZeroDivisionError:
            result = 0
            print("Error: Division by zero")
        except IndexError:
            result = 0
            print("Error: Index out of range")
        finally:
            new_list.append(result)

    return new_list
