def kaja_plus(num):
    if not isinstance(num,(int, float)):
        print("Input must be number")
        return "non-num input"
    print(num+26)
    return num+26

def kaja_mult(num): 
    if not isinstance(num,(int, float)):
        print("Input must be number")
        return "non-num input"
    print(num*26)
    return num*26

def kaja_div(num):
    if not isinstance(num,(int, float)):
        print("Input must be number")
        return "non-num input"
    print(num/26)
    return num/26

def kaja_multimult(num1, num2, num3):
    if (not isinstance(num1, (int,float))
    or not isinstance(num2, (int,float))
    or not isinstance(num2, (int,float))):
        print("values must be numbers")
        return "non-num input"
    print(num1*num2*num3)
    return num1*num2*num3 

def kaja_wordsum(word):
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