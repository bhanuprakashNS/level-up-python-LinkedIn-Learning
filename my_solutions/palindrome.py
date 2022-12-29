# Identifying a palindrome
import re
import math
check_word = input('Enter a word or sentence?').lower()
cleaned_word = re.sub('\W+','',check_word)
# print(cleaned_word) - check
# print(cleaned_word[2]) - check

# def check_palindrome(word):
#     word_length = len(word)
#     check_upto = math.ceil(word_length/2)
#     is_palindrome = ''
#     # print(word_length) - check
#     for i in range(0, check_upto):
#         first_half_letter = word[i]
#         second_half_letter = word[word_length-i-1]
#         # print(first_half_letter,second_half_letter ) - check
#         if first_half_letter != second_half_letter:
#             is_palindrome = False
#             break    
#         elif first_half_letter == second_half_letter:
#             if i == check_upto-1:
#                 is_palindrome = True
#             else:
#                 pass
#     return is_palindrome

def check_palindrome(word):
    forward = word
    backward = word[::-1]
    return forward == backward

print(check_palindrome(cleaned_word))
