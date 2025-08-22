import random
from itertools import combinations

def pick_number_sets(numbers_list, set_size=5, num_sets=5):
    """
    Picks a specified number of unique random sets of a given size from a list of numbers.

    Args:
        numbers_list (list): The list of numbers to choose from.
        set_size (int): The size of each number set (e.g., 6).
        num_sets (int): The number of sets to generate (e.g., 10).

    Returns:
        list: A list of tuples, where each tuple is a unique set of numbers.
              Returns an empty list if there are not enough unique combinations possible.
    """
    # First, check if the list is large enough to form at least one set.
    if len(numbers_list) < set_size:
        print("Error: The input list is smaller than the required set size.")
        return []

    # Generate all possible unique combinations of the given size.
    # The result is an iterator, so we convert it to a list.
    all_possible_combinations = list(combinations(numbers_list, set_size))

    # Check if we can actually generate the number of unique sets requested.
    if len(all_possible_combinations) < num_sets:
        print(f"Warning: Cannot generate {num_sets} unique sets.")
        print(f"Only {len(all_possible_combinations)} unique combinations are possible with the given list.")
        # In this case, we'll just return all possible combinations.

    # Randomly select the desired number of unique sets from the list of all combinations.
    random_sets = random.sample(all_possible_combinations, num_sets)

    sorted_sets = [tuple(sorted(s)) for s in random_sets]

    return sorted_sets

# --- Example Usage ---

# Define your list of numbers here.
# You can change, add, or remove numbers from this list.
my_numbers = [44, 45, 12, 33, 40, 21, 36, 52, 28, 23, 68, 65, 66, 60, 67, 64, 63, 26, 62, 46]

# Call the function to get 5 sets of 5 numbers.
selected_sets = pick_number_sets(my_numbers, set_size=5, num_sets=5)

# Print the results in a readable format.
if selected_sets:
    print(f"Here are {len(selected_sets)} random sets of 5 numbers:")
    for i, number_set in enumerate(selected_sets, 1):
        print(f"Set {i}: {number_set}")



