import sys

try:
    if (len(sys.argv) > 2):
        raise Exception()
    if (len(sys.argv) == 2):
        nb = int(sys.argv[1])
        if (nb == 0):
            print("I'm Zero.")
        elif (nb % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")

except Exception:
    print("ERROR")
