# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    return sorted(array, key=lambda x: (x == 0) and x is not False)


# Here, sorted function is sorting by lambda function, which turns not 0 into false and - into true, and then sort by keys
# where all false comes before the trues... Python uses stable sort so all values in false and true remain in their
# original order in output.
