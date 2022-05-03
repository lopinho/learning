def isPalindrome(strng):
    if len(strng) <=1:
        return True
    first, *middle, last = strng
    if first != last:
        return False
    return isPalindrome(middle)