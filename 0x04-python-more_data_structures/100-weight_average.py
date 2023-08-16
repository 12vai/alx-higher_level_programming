#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    weighted_avg = total_weighted_score / total_weight
    return weighted_avg

# Example usage
integers_tuple = [(85, 3), (90, 2), (78, 4)]
result = weight_average(integers_tuple)
print("Weighted Average:", result)
