def ft_reduce(function_to_apply, list_of_inputs):
    value = list_of_inputs[0]
    for element in list_of_inputs[1:]:
        value = function_to_apply(value, element)

    return value