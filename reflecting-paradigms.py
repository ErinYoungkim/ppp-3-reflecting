def flatten_and_sort(nested_list):
    # This function will flatten the nested list
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result
    
    # First, flatten the list
    flat_list = flatten(nested_list)
    # Then, sort the flat list
    return sorted(flat_list)

# Example usage
example_list = [3, [2, 1], [4, [6, 5]], 7]
sorted_list = flatten_and_sort(example_list)
print(sorted_list)  # Output: [1, 2, 3, 4, 5, 6, 7]


# Flattening: We make one big list from nested lists.
# Sorting: We put the numbers in order from smallest to largest.
# Immutability: We do not change the original list.
# Pure Function: Always gives the same result for the same input and does not affect other things.
# Not Higher-Order: Does not use or return other functions.
# Functional Benefits: Makes the code clean, easy to understand, and less prone to errors.


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

# Example usage
pod1 = Podracer(500, "perfect", 10000)
pod2 = AnakinsPod(600, "trashed", 15000)
pod3 = SebulbasPod(550, "repaired", 12000)

# Repair pod2
pod2.repair()
print(pod2.condition)  # Output: repaired

# Boost pod2
pod2.boost()
print(pod2.max_speed)  # Output: 1200

# Use flame_jet on pod1
pod3.flame_jet(pod1)
print(pod1.condition)  # Output: trashed


# Podracer: Basic podracer with speed, condition, and price. Can be repaired.
# AnakinsPod: Special podracer that can boost its speed.
# SebulbasPod: Special podracer that can trash other podracers