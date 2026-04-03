def average_mean(lst):
    # Converts any numbers in string form to ints and checks for invalid inputs
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid integer in list.")
    
    num_sum = sum(lst)
    return num_sum / len(lst)

def average_median(lst):
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid integer in list.")
    
    sorted_list = sorted(lst)
    median_index = (len(sorted_list) - 1) // 2

    if len(sorted_list) % 2 == 0:
        return (sorted_list[median_index] + sorted_list[median_index + 1]) / 2
    return sorted_list[median_index]
    
    