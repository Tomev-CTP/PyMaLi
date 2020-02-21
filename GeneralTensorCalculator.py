class GeneralTensorCalculator:

    def __init__(self, f):
        self.f = f

    def calculate_tensor(self, objects: list) -> dict:
        resultant_tensor = dict()

        self.f(self.__get_indices_combinations(objects))

        return resultant_tensor

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
