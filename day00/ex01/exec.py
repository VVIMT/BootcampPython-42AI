import sys

word = ' '.join(sys.argv[1:])
word = word.swapcase()

print(word[::-1])
