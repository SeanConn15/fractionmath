import math

class Fraction:

    whole = 0
    numerator = 0
    denominator = 0

    # constructor takes whole number, numerator and denominator
    # TODO: automatically simplifies if possible
    def __init__(self, whole, numerator, denominator):
        # takes overloaded fractions and adds them to number
        # divides if possible
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator

    # parsing constructor
    # takes a string and constructs the object


    # internal simplify function
    # takes unneccessarily complex fractions and simplifies them
    def simplify(self):
        # check if the whole numbers can be taken off the fraction
        while (self.numerator >= self.denominator):
            self.whole = self.whole + 1
            self.numerator = self.numerator - self.denominator

        # check if the fraction can be simplified
        # TODO: divide by GCD
        print ("hello")
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 1:
            self.numerator = int(self.numerator / gcd)
            self.denominator = int(self.denominator / gcd)


    # add two fractions together
    def add(self, other):
        # find the common denominator of the two fractions
        cd = self.common_denominator(self.denominator, other.denominator)

        # find the difference between each
        diff_denominator_1 = cd / self.denominator
        diff_denominator_2 = cd / other.denominator
        # multiply both the numerators by what's needed
        # implicit conversion here is okay because the common denominator division above always returns an int
        n1 = int(self.numerator * diff_denominator_1)
        n2 = int(other.numerator * diff_denominator_2)
        print (cd)
        print (n1)
        print (n2)

        new_num_1 = self.numerator * n1
        new_num_2 = other.numerator * n2
        print()
        print (new_num_1)
        print (new_num_2)
        # add the numerators
        self.numerator = new_num_1 + new_num_2
        self.denominator = cd


        # see if we need to add to the whole number


        # modify member variables


        # simplify
        self.simplify()

    def common_denominator(self, a, b):
        # TODO: LCD algo
        return a * b

    #TODO: overload addition operator

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

