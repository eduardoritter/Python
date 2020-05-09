import operator
from functools import reduce


"""  Map Function """

list_one = [1, 4, 9, 16, 25]

list_two = map(str, list_one)

print(list_two) # In Python 3+, many processes that iterate over iterables return iterators themselves.
print(list(list_two))


""" Filter Function """

def positive(v):
    return v > 0

values = [10, 4, -1, 3, 5, -9, -11]
print(list(filter(positive, values)))


""" Lambda """

values = [1, -2, 17, 10, 4, -1, 3, 5, -9, -11]
print(list(filter(lambda v: v > 0, values)))


""" Reduce Function """

numbers = [1, 2, 3, 4, 5]
multiplication = reduce(operator.mul, numbers)
print(multiplication)
