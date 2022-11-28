def find_cycle(matrix: [[]]):
    """
    this function get matrix with the values that the players get for any object and returns if the Consumption Graph
    contain cycle.
    >>> [find_cycle([[1, 1, 0.07, 0.3], [0, 0, 0.93, 0.7]])]
    ['have cycles']
    >>> [find_cycle([[1, 1, 0.07, 0], [0, 0, 0.93, 1]])]
    ['dont have cycles']
    >>> [find_cycle([[1, 0.5], [0, 0.5]])]
    ['dont have cycles']
    >>> [find_cycle([[0.1, 0.5], [0.9, 0.5]])]
    ['have cycles']
    """
    common_objects = 0
    # pass over the columns= the objects
    for i in range(0, len(matrix[0])):
        have_object = 0
        # pass over the rows= the players
        for j in range(0, len(matrix)):
            if matrix[j][i] > 0:  # if the value>0 this player have this object
                have_object = have_object + 1
            if have_object >= 2:  # at least 2 player have this object
                common_objects = common_objects + 1
                break
        if common_objects >= len(matrix):  # at least n objects shared
            return "have cycles"
    return "dont have cycles"


if __name__ == '__main__':
    import doctest

    doctest.testmod()
