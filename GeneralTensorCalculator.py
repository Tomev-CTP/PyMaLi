import multiprocessing


class GeneralTensorCalculator:

    def __init__(self, f):
        self.f = f
        self.objects = []
        self.tensor = dict()

    # Calculates tensor for given object using function f provided in the constructor.
    def calculate_tensor(self, objects: list) -> dict:
        self.tensor = dict()

        # Get indices combinations
        indices_combinations = self.__get_indices_combinations(objects.copy())

        # Initialize tensor with empty values
        self.__initialize_tensor(indices_combinations)

        # Fill tensor dict with values
        for combination in indices_combinations:
            self.__count_tensor_value_for_combination(combination, objects)

        return self.tensor

    def __count_tensor_value_for_combination(self, combination, objects):
        tensor = self.tensor
        f_arguments = []

        # Note that len of objects should be equal to len of current_combination as it contains index value
        # for each object.
        for i in range(len(objects) - 1):
            f_arguments += [objects[i][combination[0]]]
            tensor = tensor[combination.pop(0)]

        # After above loop only one element remains and tensor should be in place, therefore only thing to do
        # left is assigning it value of f
        f_arguments += [objects[-1][combination[0]]]

        tensor[combination.pop(0)] = self.f(f_arguments)

    # Get combinations of all possible indices variation. Eg.
    def __get_indices_combinations(self, objects: list) -> list:
        # Finish if objects list is empty. This should not happen.
        if len(objects) == 0:
            return None

        combinations = []

        # Termination condition
        # If it's the last element of the list of objects create and return list of it's possible indexes
        if len(objects) == 1:
            for i in range(len(objects[0])):
                combinations.append([i])
            return combinations

        # Recursive call
        # If there are still multiple objects take first and make recursive call
        first_object = objects.pop(0)
        other_objects_combination = self.__get_indices_combinations(objects.copy())

        # Then add to combinations sum of other_objects_combinations and popped object indices
        # Note that order is important here
        for i in range(len(first_object)):
            for combination in other_objects_combination:
                combinations.append([i] + combination)

        return combinations

    # Initializing tensor as dict of dict of dict ... with zeros. Initialization for each combination is performed
    # once at a time.
    def __initialize_tensor(self, indices_combination) -> None:
        # Error check.
        if len(indices_combination) == 0:
            return

        for combination in indices_combination:
            self.__initialize_combination_path(self.tensor, combination.copy())

    # Initializing tensor with 0 for given path
    def __initialize_combination_path(self, tensor, combination):
        # Error check
        if len(combination) == 0:
            return

        # Termination condition
        if len(combination) == 1:
            tensor[combination[0]] = 0
            return

        # Recursive call
        initialized_index = combination.pop(0)
        if not tensor.keys().__contains__(initialized_index):
            tensor[initialized_index] = dict()
        self.__initialize_combination_path(tensor[initialized_index], combination)



#### Examples #####

def my_test_f(arguments: list) -> float:
    result = 1

    for a in arguments:
        result *= a

    return result


def my_test_f_2(arguments: list):
    result = 1

    for a in arguments:
        result = np.kron(result, a)

    return result


gtc = GeneralTensorCalculator(my_test_f)
t = gtc.calculate_tensor([[1, 2, 3], [40, 50], [600, 700, 800]])

import numpy as np
sigma_z=np.array([[1,0],[0,-1]])

gtc2 = GeneralTensorCalculator(my_test_f_2)
t2 = gtc2.calculate_tensor([
    [1*sigma_z, 2*sigma_z],
    [2*np.eye(4), 3*np.eye(4), 4*np.eye(4),5*np.eye(5)],
    [10*sigma_z, 1000*sigma_z, 10e6*sigma_z]
])
