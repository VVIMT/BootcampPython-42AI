def ft_map(function_to_apply, list_of_inputs):
    l = []
    for elem in list_of_inputs:
        l.append(function_to_apply(elem))
    return l