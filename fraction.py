import math
import re

class Fraction:

    whole = 0
    numerator = 0
    denominator = 0
    parser = re.compile('(?P<whole>-{0,1}\d+)_(?P<numerator>-{0,1}\d+)/(?P<denominator>\d+)')

    # constructor takes whole number, numerator and denominator
    # TODO: type checking
    def __init__(self, *args):
        if (len(args) == 3):
            self.construct_from_ints(args[0], args[1], args[2])
        elif (len(args) == 1):
            self.construct_from_string(args[0])
        else:
            raise Exception("Invalid arguments, need either three integers or a string")

    def construct_from_ints(self, whole, numerator, denominator):
        # takes overloaded fractions and adds them to number
        # divides if possible
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    # parsing constructor
    # takes a string and constructs the object
    def construct_from_string(self, string):
        res = self.parser.search(string)
        if not res:
            raise Exception("Inavlid Arugments")
        # TODO: check conversion to int
        self.whole = int(res.group("whole"))
        self.numerator = int(res.group("numerator"))
        self.denominator = int(res.group("denominator"))
        self.simplify()


    # internal simplify function
    # takes unneccessarily complex fractions and simplifies them
    def simplify(self):
        # check if the whole numbers can be taken off the fraction
        while (self.numerator >= self.denominator):
            self.whole = self.whole + 1
            self.numerator = self.numerator - self.denominator

        # TODO:: check if the fraction is negative and take off from the whole
        while (self.numerator < 0):
            self.whole = self.whole - 1
            self.numerator = self.numerator + self.denominator

        # check if the fraction can be simplified
        # TODO: divide by GCD
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 1:
            self.numerator = int(self.numerator / gcd)
            self.denominator = int(self.denominator / gcd)

    def add(self, other):
        self.operate(other, "+")

    def subtract(self, other):
        self.operate(other, "-")

    def multiply(self, other):
        self.operate(other, "*")

    def divide(self, other):
        self.operate(other, "/")

    # add two fractions together
    def operate(self, other, operator):


        if (operator == "*"):
            self.numerator = self.numerator * other.numerator;
            self.denominator = self.denominator * other.denominator;
        elif (operator == "/"):
            self.numerator = self.numerator * other.denominator;
            self.denominator = self.denominator * other.numerator;
        elif operator == "+" or operator == "-":

            # find the common denominator of the two fractions
            cd = self.common_denominator(self.denominator, other.denominator)

            # find the difference between each
            diff_denominator_1 = cd / self.denominator
            diff_denominator_2 = cd / other.denominator
            # multiply both the numerators by what's needed
            # implicit conversion here is okay because the common denominator division above always returns an int
            n1 = int(self.numerator * diff_denominator_1)
            n2 = int(other.numerator * diff_denominator_2)

            new_num_1 = self.numerator * n1
            new_num_2 = other.numerator * n2

            if(operator == "+"):
                self.numerator = new_num_1 + new_num_2
            elif (operator == "-"):
                self.numerator = new_num_1 - new_num_2
            self.denominator = cd

        else:
            raise Exception("not givien a valid operator")

        # simplify
        self.simplify()


    def common_denominator(self, a, b):
        # TODO: LCD algo
        return a * b

    #TODO: overload addition operator?

    def __eq__(self, other):
        if (self.numerator == other.numerator and
            self.denominator == other.denominator and
            self.whole == self.whole):
            return True
        else:
            return False

    # printing function
    def __str__(self):
        return str(self.whole) + "_" + str(self.numerator) + "/" + str(self.denominator)


if __name__ == "__main__":
    a = Fraction(0, 1, 2)
    b = Fraction(0, 1, 2)
    a.add(b)
    print (a)

