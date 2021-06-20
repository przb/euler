def is_palindrome(number):
    
    number = str(number)
    index = 0
    lastIndex = len(number) - 1
    if not (number[index] == number[lastIndex - index]):
        return False
    else:
        palindromeStatus = True
        
        while (lastIndex - index > 1):
            if not (number[index] == number[lastIndex - index]):
                palindromeStatus = False
                return palindromeStatus
            else:
                index += 1
    
        return palindromeStatus