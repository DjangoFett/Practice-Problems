
def maximum_ones(digits):
    """
    Given binary array, find count of maximum number of consecutive 1’s present in the array.
    :param digits:
    :type digits: List[int]
    :rtype:  int
    Complexity: O(n)
    """

    maximum_sequence = 0
    current_sequence = 0

    for digit in digits:

        # validate that the digit is 0 or 1
        if digit not in [0, 1]:
            return "Invalid input"

        if digit == 1:
            current_sequence += 1
            if current_sequence > maximum_sequence:
                maximum_sequence = current_sequence
        else:
            current_sequence = 0
    return maximum_sequence
