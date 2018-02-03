
def is_anagram(s, t):
    """
    Given two strings s and t, write a function to determine if t is an
    anagram of s
    :type s: str
    :type t: str
    :rtype: bool
    """

    if sorted(s) == sorted(t):
        return True

    return False

