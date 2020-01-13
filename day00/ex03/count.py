import fileinput
import string

def text_analyzer(text = None):
    try:
        a = 0
        b = 0
        c = 0
        d = 0

        if (text != None and type(text) != string):
            raise Exception()
        if (text is None):
            print('What is the text to analyse?')
            line = fileinput.input()
            for text in line:
                for i in text:
                    if i.isupper():
                        a += 1
                    elif i.islower():
                        b += 1
                    elif i == ' ':
                        d += 1
                    elif string.punctuation:
                        c += 1
                line.close()
            print("The text contains " + str(len(text)) + " characters:")
            print("- " + str(a) + " upper letters")
            print("- " + str(b) + " lower letters")
            print("- " + str(c) + " punctuation marks")
            print("- " + str(d) + " spaces")

    except Exception:
        print("ERROR")
