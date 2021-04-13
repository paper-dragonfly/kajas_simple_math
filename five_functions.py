def kaja_plus(num):
    '''Adds 26 to the argument num (int, float).'''
    if not isinstance(num,(int, float)):
        print("Input must be number")
        return "non-num input"
    print(num+26)
    return num+26

def kaja_mult(num): 
    '''Multiples argument num (int, float) by 26.'''
    if not isinstance(num,(int, float)):
        print("Input must be number")
        return "non-num input"
    print(num*26)
    return num*26

def kaja_div(num):
    '''Divides num (int, float) by 26.'''
    if not isinstance(num,(int, float)):
        print("Input must be number")
        return "non-num input"
    print(num/26)
    return num/26

def kaja_multimult(num1, num2, num3):
    '''Multiplies the three arguments (int, float) together'''
    if (not isinstance(num1, (int,float))
    or not isinstance(num2, (int,float))
    or not isinstance(num2, (int,float))):
        print("values must be numbers")
        return "non-num input"
    print(num1*num2*num3)
    return num1*num2*num3 

def kaja_wordsum(word):
    '''Returns the sum of the inputed string where each letter holds the value of its position in the alphabet.
    Example: kaja_wordsum('abc') returns 6'''
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    num = 0
    word_sum = 0
    if not isinstance(word, str):
        print("input must be a string") 
        return "non-string input"
    for letter in word:
        for i in range(len(alphabet)):
            if alphabet[i] == letter:
                num = i
                word_sum += num
    print(word_sum)
    return word_sum