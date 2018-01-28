"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum_brute(numbers, target):
    """
    This fails on LeetCode.com due to python being a slower language
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    for index, number in enumerate(numbers):
        for index_2, number_2 in enumerate(numbers):
            total = number + number_2
            if total == target and index != index_2:
                return [index, index_2]
    return


def two_sum_efficient(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
