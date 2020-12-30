# Imports
import math
from scipy.special import comb
from fractions import Fraction
from scipy.stats import binom

# Main numbers
a = 48
x = 6
# Extra number
b = 8
y = 1

# probability function
def factorial(miss):
    firstp = Fraction(math.factorial(x)/math.factorial(miss)*math.factorial(x-miss))
    secondp= Fraction(math.factorial(a-x)/(math.factorial((a-x)-(x-miss))*math.factorial(x-miss)))
    answer = firstp * secondp
    return answer

# Total possible combinations
total = comb(a, x, exact=True)
print("Total combinations: {}" .format(total))

# Jackpot 6+1
jackpot = total * b
print("Jackpot: 1 / {}" .format(jackpot))

# Level II 6
lvl2 = (total * 8) / 7
print("Level II: 1 / {}" .format(lvl2))

# Level III 5+1
probability5 = binom.pmf(1, x, (1/a))
lvl3 = (total * b) * probability5
print("Level III: 1 / {}" .format(lvl3))

# Level IV 5
lvl4 = ((total * 8) / 7) * probability5
print("Level IV: 1 / {}" .format(lvl4))

# Level V 4+1
probability4 = binom.pmf(2, x, (1/a))
lvl5 = (total * b) * probability4
print("Level V: 1 / {}" .format(lvl5))

# Level VI 4
lvl6 = ((total * 8) / 7) * probability4
print("Level VI: 1 / {}" .format(lvl6))

# Level VII 3+1
probability3 = binom.pmf(3, x, (1/a))
lvl7 = (total * b) * probability3
print("Level VII: 1 / {}" .format(lvl7))

# Level VIII 3
lvl8 = ((total * 8) / 7) * probability3
print("Level VIII: 1 / {}" .format(lvl8))

## probability variables are used to calculate the possible outcomes for each correctly and incorrectly guessed numbers
## in levels 2, 4, 6 and 8, probability equation also accounts for the incorrectly guessed extra number
## Total combinations calculated using scipy.special.comb
## other calculations done by only calculating the denominator of fractures, for ease of use
## Probability mass function from SciPy helped calculate cases with incorrect numbers
