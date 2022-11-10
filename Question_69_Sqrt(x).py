import math
class Solution:
    def mySqrt(self, x):
        if x != 0 and x != 1 and x != 2:
            old_guess_number = x / 2
            new_guess_number = x
            while math.trunc(new_guess_number) != math.trunc(old_guess_number):
                temp = new_guess_number
                new_guess_number = old_guess_number - (old_guess_number**2-x) /(2*old_guess_number-1)
                old_guess_number = temp

            return math.trunc(old_guess_number)
        elif x == 1:
            return 1
        elif x == 2:
            return 1
        else:
            return 0