from bisect import bisect_left, bisect_right

def get_num_of_elements_in_range(lst, left_value, right_value):
    right_index = bisect_right(lst, right_value)
    left_index = bisect_left(lst, left_value)
    return right_index - left_index