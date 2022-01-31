# Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and
# spaces. Spaces will be included only when more than one word is present.
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") =>
# returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
# import sys
# sys.stdin = open('input.txt', 'r')
# # def spin_words(sentence):
# #     new_sent = []
# #     ls = sentence.split()
# #     for word in ls:
# #         if len(word) >= 5:
# #             word = word[::-1]
# #         new_sent.append(word)
# #     return ' '.join(new_sent)
#
# def spin_words(sentence):
#     return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])
#
# print(spin_words(input()))

#=============================
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

# import sys
# sys.stdin = open('input.txt', 'r')
#
# # def persistence(n):
#     # count = 0
#     # while len(str(n)) > 1:
#     #     mult = 1
#     #     for sym in str(n):
#     #         mult *= int(sym)
#     #     n = mult
#     #     count += 1
#     # return count
#
# from functools import reduce
# def persistence(n, count = 0):
#     return persistence(reduce(lambda a, b: int(a)*int(b), str(n)), count + 1) if len(str(n)) > 1 else count
#
# print(persistence(int(input())))

#=============================
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most
# secret question is still correct. However, since someone could look over your shoulder, you don't want that shown
# on your screen. Instead, we mask it.
# import sys
# sys.stdin = open('input.txt', 'r')

# def maskify(cc):
#     return (len(cc) - 4) * '#' + cc[-4:]
#
# print(maskify(input()))

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore
# letter case.

# import sys
# sys.stdin = open('input.txt')
#
# def is_isogram(string):
#     # flag = True
#     # string = string.lower()
#     # for sym in string:
#     #     if string.count(sym) > 1:
#     #         flag = False
#     #         break
#     # return flag
#     return len(string) == len(set(string.lower()))
#
# print(is_isogram(input()))

#=============================
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
# also often referred to as Pascal case).
#

# def to_camel_case(text):
#     if text != '':
#         ls = text.replace('_', ' ').replace('-', ' ').split()
#         ls_new = ls[0] + ''.join([word.capitalize() for word in ls[1:]])
#         return ls_new
#     else: return ''
#
# print(to_camel_case(input()))

#=============================
#  Define a function that takes one integer argument and returns logical value true or false depending on if the
# integer is a prime.
#
#  Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other
# than 1 and itself.
#
# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.\
# Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.

# # def is_prime(num):
# #     ls = 2
# #     if num <= 1: return False
# #     for n in range(2, int(abs(num)/2)+1):
# #         if abs(num) % n == 0:
# #             ls += 1
# #             if ls > 2: return False
# #     return True
#
# def is_prime(num):
#     if num <= 1: return False
#     if num % 2 == 0:
#         return num == 2
#     d = 3
#     while d * d <= num and num % d != 0:
#         d += 2
#     return d * d > num
#
# print(is_prime(int(input())))

#===========================================================================================
# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You
# don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
# starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and
# 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

def solution(roman):
    romanNumeralMap = (('M', 1000),
                       ('CM', 900),
                       ('D', 500),
                       ('CD', 400),
                       ('C', 100),
                       ('XC', 90),
                       ('L', 50),
                       ('XL', 40),
                       ('X', 10),
                       ('IX', 9),
                       ('V', 5),
                       ('IV', 4),
                       ('I', 1))
    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while roman[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
    # rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # result = []
    # roman = ','.join(roman).split(',')
    # if len(roman) == 1: return rom_dict[roman]
    # # result = [rom_dict[b] - rom_dict[a] if a == 'I' and b in ('VXLCDM') else rom_dict[a] + rom_dict[b] for a,b in roman]
    # # return result
    # for i in range(1, len(roman)):
    #     if roman[i-1] == 'I' and (roman[i] in ('VXLCDM')):
    #         result.append(rom_dict[roman[i]] - rom_dict[roman[i-1]])
    #         roman[i] = ''
    #         roman[i - 1] = ''
    #     else:
    #         result.append(rom_dict[roman[i-1]])
    #         result.append(rom_dict[roman[i]])
    # return sum(result)





print(solution('XII'))

