"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum_brute(nums, target):
    """
    The brute force approach, this is pretty simple. It loops through
    each combination to find a value equal to target - x.
    This fails on LeetCode.com due to python being a slower language
    Time Complexity: O(n^2)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i, number in enumerate(nums):
        for j, number_2 in enumerate(nums):
            if number == target - number_2 and i != j:
                return [i, j]
    return


def two_sum_efficient(numbers, target):
    """
    A more efficient solution to the problem, it will store values to
    a dictionary. You can subtract the current number from the target
    and then check to see if the answer has already been mapped to the
    dictionary.

    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    number_map = {}
    for i, number in enumerate(numbers):
        number_map[number] = i

    for i, number in enumerate(numbers):
        complement = target - numbers[i]
        if complement in number_map and number_map[complement] != i:
            return i, number_map[complement]
    return


def two_sum_most_efficient(numbers, target):
    """
    Similar to the solution done above but is done using one for loop
    instead of two

    :param numbers:
    :param target:
    :return:
    """

    number_map = {}
    for i, number in enumerate(numbers):
        number_map[number] = i
        complement = target - number

        if complement in number_map and number_map[complement] != i:
            return i, number_map[complement]
    return
