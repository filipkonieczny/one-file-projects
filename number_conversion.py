#!/usr/bin/env python
# encoding: utf-8
 
 
# this program allows you to quickly convert numbers of different
# numeral base systems(2-10) and vice versa
# gotta be careful though, I couldn't be bothered to make
# all the neccessary tests and warnings such as "base out of range".
 
 
 
def convert_from_decimal(base, number, output="", output_list=[]):
    '''
   Converts a number from decimal system to any other system,
   With x base, where 2 < x < 10.
   
   
   (int, int, str, list) -> str
   
   output, output_list are set to default and should not be changed.
   Basically all you should give is the target base and number.
   
   
   >>> convert_from_decimal(2, 13)
   
   1101
 
   '''
   
 
    # make sure it's within range
    if base >= 2 and base <= 10:
        # what's left of the number when trying to convert it
        rest = number % base
        #number = number/base
       
        # extending output with the outcome
        output += str(rest)
        output_list.append(output[::-1])
       
        # continue converting if it's not over
        if number > 1:
            convert_from_decimal(base, number/base, output, output_list)
   
    # if it's not within range, inform the user
    else:
        print("Sorry, can't convert using %d as a base!" % base)
   
 
    # return the value of the number as an int
    return int(output_list[-1])
 
 
def convert_to_decimal(base, number):
    '''
   This function takes a base number and converts it to decimal.
   
   (int, int) -> str
   
   
   >>> convert_to_decimal(2, 1101)
   13
   
   >>> convert_to_decimal(4, 2002)
   130
   
   '''
   
    number = str(number)
    outcome = 0
    foo = 0
   
    # make sure it's within range
    if base >= 2 and base <= 10:
        for i, n in enumerate(number[::-1]):
            foo = int(n)
            outcome += pow(base, i) * foo
   
   
    # if it's not within range
    else:
        print("Sorry, can't convert using %d as a base!" % base)
   
   
    return outcome
 
 
input_text = "Would you like to convert from or to decimal?(0/1): "
number_input = "What is the number you want to convert?: "
 
 
# main loop
while True:
    # ask to choose a mode
    mode = raw_input(input_text)
   
    # convertion from decimal to something
    if mode == "0":
        base_input = "What is your target base?(2-10): "
       
        base = input(base_input)
        number = input(number_input)
       
        print convert_from_decimal(base, number)
   
   
    # convertion from something to decimal
    elif mode == "1":
        base_input = "What is your starting base?(2-10): "
       
        base = input(base_input)
        number = input(number_input)
       
        print convert_to_decimal(base, number)
       
   
    # if mode was chosen improperly
    else:
        print("Wrong input, unable to proceed.")
   
   
    # ask the user if he wants to repeat the fun
    repeat = raw_input("Would you like to continue?(y/n): ")
   
    while repeat != "y" and repeat != "n":
        repeat = raw_input("Would you like to continue?(y/n): ")
   
   
    if repeat == "n":
        break



# smarter way(@narfdotpl)
from __future__ import absolute_import, division
 
 
def convert(n, base1, base2):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
 
    # convert n (string) to decimal (int)
    # going through digits from right to left
    decimal = 0
    for index, digit in enumerate(reversed(n)):
        decimal += digits.index(digit) * base1 ** index
 
    # deal with zero
    if decimal == 0:
        return '0'
 
    # compute length of n2 (string) -- a number in base2
    len_n2 = 0
    while base2 ** len_n2 <= decimal:
        len_n2 += 1
 
    # set n2 digits from left to right (using right to left index)
    n2_digits = []
    for index in reversed(range(len_n2)):
        for digit_value, digit in reversed(list(enumerate(digits[:base2]))):
            value = digit_value * base2 ** index
            if value <= decimal:
                decimal -= value
                n2_digits.append(digit)
                break
 
    return ''.join(n2_digits)
 
 
def _main():
    for number, b1, b2, expected_result in [
        ('ff', 16, 10, '255'),
        ('15', 10, 16, 'f'),
        ('101', 2, 10, '5'),
        ('21', 10, 2, '10101'),
        ('8', 10, 16, '8'),
        ('0', 10, 16, '0'),
    ]:
        result = convert(number, b1, b2)
        if result != expected_result:
            print '%s != %s' % (result, expected_result)
 
#if __name__ == '__main__':
#    _main()