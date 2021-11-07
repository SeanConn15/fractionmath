from fraction import Fraction
import sys

# forever
def parse_forever():
    while (True):
        inputstr = input("?")
        if (inputstr == "stop"):
           sys.exit(0) 
        a = parse(inputstr)
        print ("=" + a.__str__())

def parse(inputstring):

    # parse out the fractions and the operators
    arguments = inputstring.split()

    # TODO: handle parsing failures

    # TODO: PEMDAS by parsing and creating an operations stack

    # create fraction objects
    a = Fraction(arguments[0])
    b = Fraction(arguments[2])
    a.operate(b, arguments[1])
    return a

if __name__ == "__main__":
    parse_forever()
