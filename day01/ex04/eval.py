class Evaluator:
    def __init__(self):
        pass

    def zip_evaluate(param1, param2):
        if (isinstance(param1, list) and isinstance(param2, list)) and (len(param1) == len(param2)):
            pass
        else:
            return (-1)

        zipped = zip(param1, param2)
        l_zipped = list(zipped)
        sum = 0
        for i in l_zipped:
            print(i)

            if isinstance(i[0], str) and isinstance(i[1], float):
                sum = sum + (len(i[0]) * i[1])
            elif isinstance(i[1], str) and isinstance(i[0], float):
                sum = sum + (len(i[1]) * i[0])
            else:
                raise TypeError
        print("\nsum = " + str(sum))
        return sum

    def enumerate_evaluate(param1, param2):
        if (isinstance(param1, list) and isinstance(param2, list)) and (len(param1) == len(param2)):
            pass
        else:
            return (-1)

        sum = 0
        for i, (key1, key2) in enumerate(zip(param1, param2)):
            print(key1)

            if isinstance(key1, str) and isinstance(key2, float):
                sum = sum + (len(key1) * key2)
            elif isinstance(key2, str) and isinstance(key1, float):
                sum = sum + (key1 * len(key2))
            else:
                raise TypeError
        print("\nsum = " + str(sum))
        return sum