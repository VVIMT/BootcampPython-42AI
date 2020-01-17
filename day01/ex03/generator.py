import random

def ordered_set(seq):
  seen = set()
  return [x for x in seq if x not in seen and not seen.add(x)]

def generator(text, sep=" ", option=None):
    text = text.split(sep)

    if option == None:
        return text
    elif option == "shuffle":
        random.shuffle(text)
        return text
    elif option == "unique":
        print(text)
        return list(ordered_set(text))
    elif option == "ordered":
        return sorted(text, key=lambda x:(not x.islower(), x))
    else:
        pass