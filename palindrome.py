
def is_palindrome(word):
    reverse = word[::-1]

    if word == reverse:
        return True

    return False
