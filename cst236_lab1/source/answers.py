"""
    This file holds all the helper functions that do the caluculations
     or holds the logic to test files
"""

import datetime
import math
import getpass



def get_date_time_string():
    """
    Get date and time

    :returns: script filename, SHA1 hash, date, and author of last time path was modified
    :returns: current time
    :rtype: string
    """

    curr_time = datetime.datetime.now()
    curr_time = curr_time.replace(second=0, microsecond=0)
    return str(curr_time)


def get_fibonacci(nth_digit='z'):
    """
    Get file revision for the file in path

    :param nth_digit: Digit of the fibonacci sequence
    :type path: float

    :returns: The nth digit of the fibonacci sequence
    :rtype: float
    """

    if nth_digit == 'z':
        return "No parameter given in get_fibonacci function"

    if nth_digit < 0:
        return 'Invalid Number'

    nth_digit = math.floor(nth_digit)
    if nth_digit < 2:
        return nth_digit
    return get_fibonacci(nth_digit-2) + get_fibonacci(nth_digit-1)


def get_pi_digit(nth_digit):
    """
    Get the nth digit of pi

    :param nth_digit: Digit of the pi that you want
    :return: returns the nth digit of the pi
    """
    if nth_digit <= 0:
        return "Invalid Number"

    nth_digit = nth_digit - 1
    nth_digit = math.floor(nth_digit)
    nth_digit = math.floor(math.pi * pow(10, nth_digit))
    nth_digit = math.fmod(nth_digit, 10)
    return nth_digit


def open_the_door():
    """

    :return: returns a string with the username of the current user
    """

    return "I'm afraid I can't do that " + getpass.getuser()


def convert(num=0, unit1='cm', unit2='cm'):
    """

    :param num: pass in the number that you want to convert the units of
    :param unit1: unit you want to convert from
    :param unit2: unit you want to convert to
    :return: returns the result of the conversion
    """
    conversion_dic = \
        {
            'km': 1000,
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'lbs': .454545454545454545454545,
            'kg': 1,
            'g': 0.001,
            'mg': 0.0001,
            'gallon': 1,
            'quart': 0.25,
            'pint': 0.125
        }

    if unit1 in list(['km', 'm', 'cm', 'mm']):
        if unit2 not in list(['km', 'm', 'cm', 'mm']):
            return "invalid conversion"

    if unit1 in list(['lbs', 'kg', 'g', 'mg']):
        if unit2 not in list(['lbs', 'kg', 'g', 'mg']):
            return "invalid conversion"

    if unit1 in list(['gallon', 'quart', 'pint']):
        if unit2 not in list(['gallon', 'quart', 'pint']):
            return "invalid conversion"

    result = (num * conversion_dic[unit1]) / conversion_dic[unit2]

    return result


def my_add(num1=0, num2=0):
    """

    :param num1: first number to add
    :param num2: second number to add
    :return: return the added result
    """
    return num1 + num2


def my_subtract(num1=0, num2=0):
    """

    :param num1: number to subtract from
    :param num2: number to subtract
    :return: returns subtracted result
    """

    return num1 - num2


def my_divide(num1=0, num2=0):
    """

    :param num1: number to divide from
    :param num2: number to divide to
    :return: returns divided result of the two numbers
    """

    return num1 / num2


def my_multiply(num1=0, num2=0):
    """

    :param num1: First number to multiply
    :param num2: second number to multiply
    :return: returns the result of the two numbers multiplied together
    """

    return num1 * num2


def my_mod(num1=0, num2=0):
    """

    :param num1: number to mod
    :param num2: number to mod from
    :return: returns the modded result of the two numbers passed in
    """

    return num1 % num2


def always_happy():
    """

    :return: returns a string
    """
    return "I'm always happy!"


def good_time():
    """

    :return: returns a string
    """
    return "Club"


def best_restaurant():
    """

    :return: returns a string
    """
    return "Use a search engine idiot!"


def get_name():
    """

    :return: returns your username
    """
    return "Your name is " + getpass.getuser()


def weather():
    """

    :return: returns a string
    """
    return "Check your weather app!"
