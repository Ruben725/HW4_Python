def sort_dictionary(input_dict):

    sorted_keys = sorted(input_dict.keys(), key = lambda x: input_dict[x][1])

    result = []

    for i in sorted_keys:

        _tuple = (i, input_dict[i][0])

        result.append(_tuple)

    return result
