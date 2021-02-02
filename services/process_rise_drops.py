
class RiseDropProcessor:

    def __init__(self, input):
        self.input = input
        self.__result_set = list()

    @property
    def result_set(self):
        return self.__result_set

    @result_set.setter
    def result_set(self, result_set):
        self.__result_set = result_set

    def __set_intersecting_points(self):

        intersections = [(ele[1], k[2]) for idx, ele in enumerate(self.input) for _i, k in enumerate(self.input)
                         if _i != idx and ele[2] > k[2] and k[0] < ele[1] < k[1]]
        subsume_intersections = [ele for idx, ele in enumerate(intersections) for _i, k in enumerate(intersections)
                                 if _i != idx and ele[0] == k[0] and ele[1] < k[1]]
        self.result_set.extend([_l for _l in intersections if _l not in subsume_intersections])
        del subsume_intersections

    def __set_input_coordinates(self):

        coord_list = list()
        for i in self.input:
            coord_list.extend(list([(i[0], i[2]), (i[1], 0)]))
        self.result_set.extend(coord_list)

    def __remove_subsumed_points(self):
        self.result_set = sorted(sorted(set(self.result_set), key=lambda x: (x[1]), reverse=True), key=lambda x: x[0])

        subsumed_list = list()
        for idx, ele in enumerate(self.input):
            for _point in self.result_set:
                if ele[0] <= _point[0] < ele[1] and _point[1] < ele[2]:
                    subsumed_list.append(_point)

        self.result_set = [_p for _p in self.result_set if _p not in subsumed_list]

    def process_rise_and_drops(self):
        self.__set_input_coordinates()
        self.__set_intersecting_points()
        self.__remove_subsumed_points()
        return self.result_set
