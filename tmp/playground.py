# def kaja_wordsum(word):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     num = 0
#     word_sum = 0 
#     for letter in word:
#         for i in range(len(alphabet)):
#             if alphabet[i] == letter:
#                 num = i + 1
#                 word_sum += num
#     print(word_sum)
#     return word_sum

# kaja_wordsum("yyyy")

def test_type(num1, num2):
    if not isinstance(num1,[int,float]):
        print("not number")
    else:
        print(num1*2)
    return 
# test_type(5)

word = "a thingz"
alphabet = " abcdefghijklmnopqrstuvwxyz"
num = 0
word_sum = 0
for letter in word:
        for i in range(len(alphabet)):
            if alphabet[i] == letter:
                num = i
                print(letter, num)
                word_sum += num
            



