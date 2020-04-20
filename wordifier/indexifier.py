from collections import deque


# This class will generate division index to accomodate substring checks
# for e.g. [(0, 4)] => [(0, 1), (1, 4)], [(0, 2), (2, 4)], [(0, 3), (3, 4)]
# These are the possible on level division for [(0, 4)]
# This class uses graph based approach till possible division which is [(0, 1)]
# after which division cannot be possible. This class also optimize the calcualtion
# by creating the division array by the number of elements. For our example,
# the fixed number is 7 as we only care about the last 7 digits in the phone number.
class Indexifier:
    def __init__(self, number_length: int):
        self.number_length = number_length
        self.list_of_indexes = []

    def get_all_possible_indexes(self):
        if (len(self.list_of_indexes) > 0):
            return self.list_of_indexes
        else:
            self.generate_indexes()
            return self.list_of_indexes

    def divide_array(self, container: list, index_to_divide: int) -> list:
        return_list = []

        number_of_division = container[index_to_divide][1] - container[index_to_divide][0]
        if number_of_division == 1:
            return return_list

        list_of_division = [[[container[index_to_divide][0], index],
                            [index, container[index_to_divide][1]]]
                            for index in range(container[index_to_divide][0]+1,
                            container[index_to_divide][0]+number_of_division)]

        # TODO(shivaang12): Make it more efficient?
        for div in list_of_division:
            current_list = []
            for element in range(len(container)):
                if element == index_to_divide:
                    for ele in div:
                        current_list.append(ele)
                else:
                    current_list.append(container[element])
            return_list.append(current_list)

        return return_list

    def generate_indexes(self):
        final_queue = []
        queue = deque()
        queue.append([[0, self.number_length]])
        while queue:
            element = queue.popleft()
            final_queue.append(element)
            for i in range(len(element)):
                for array in self.divide_array(element, i):
                    if len(array) > 0 and not(array in queue):
                        queue.append(array)
        self.list_of_indexes = final_queue
        return
