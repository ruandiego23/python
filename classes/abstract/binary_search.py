"""
The same tactic can be used in many different contexts. One common problem is to find out whether
a number is to be found in a (sorted) sequence and even to find out where it is. Again, you follow the same
procedure: “Is the number to the right of the middle of the sequence?” If it isn’t, “Is it in the second quarter
(to the right of the middle of the left half )?” and so on. You keep an upper and a lower limit to where the
number may be and keep splitting that interval in two with every question.
"""


def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
    if number > sequence[middle]:
        return search(sequence, number, middle + 1, upper)
    else:
        return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(search(seq, 4))
