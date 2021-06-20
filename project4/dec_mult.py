import palindrometest

def decrement_multiply(static_num, index_num):
    while index_num > 1:
        product = static_num * index_num
        if palindrometest.is_palindrome(product):
            return product
        index_num -= 1
    return 0
