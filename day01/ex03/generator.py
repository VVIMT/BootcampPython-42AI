import random

def generator(text, sep=" ", option=None):
    text = text.split(sep)

    if option == None:
        return text
    elif option == "shuffle":
        random.shuffle(text)
        return text
    elif option == "unique":
        pass
    elif option == "ordered":
        pass
    else:
        pass