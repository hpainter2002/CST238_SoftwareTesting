import datetime
import math
import getpass

def get_date_time_string():
    curr_time = datetime.datetime.now()
    curr_time = curr_time.replace(second = 0, microsecond = 0)
    return str(curr_time)

def get_fibonacci(n = 'z'):
    if n == 'z':
        return "No parameter given in get_fibonacci function"

    if n < 0:
        return 'Invalid Number'

    n = math.floor(n)
    if n < 2:
        return n
    return get_fibonacci(n-2) + get_fibonacci(n-1)

def get_pi_digit(n):
    if n <= 0:
        return "Invalid Number"

    n = n - 1
    n = math.floor(n)
    n = math.floor(math.pi * pow(10, n))
    n = math.fmod(n, 10)
    return n

def open_the_door():
    return "I'm afraid I can't do that " + getpass.getuser()

def convert(num=0, unit1='cm', unit2='cm'):
    conversion_dic = {
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
        if not unit2 in list(['km', 'm', 'cm', 'mm']):
            return "invalid conversion"

    if unit1 in list(['lbs', 'kg', 'g', 'mg']):
        if not unit2 in list(['lbs', 'kg', 'g', 'mg']):
            return "invalid conversion"

    if unit1 in list(['gallon', 'quart', 'pint']):
        if not unit2 in list(['gallon', 'quart', 'pint']):
            return "invalid conversion"

    result = (num*conversion_dic[unit1])/conversion_dic[unit2]

    return result

def my_add(num1 = 0, num2 = 0):
    return num1 + num2

def my_subtract(num1 = 0, num2 = 0):
    # if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
    #     return "Invalid number"

    return num1 - num2

def my_divide(num1 = 0, num2 = 0):
    # if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
    #     return "Invalid number"

    return num1 / num2

def my_multiply(num1 = 0, num2 = 0):
    # if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
    #     return "Invalid number"

    return num1 * num2

def my_mod(num1 = 0, num2 = 0):
    # if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
    #     return "Invalid number"

    return num1 % num2

def always_happy():
    return "I'm always happy!"

def good_time():
    return "Club"

def best_restaurant():
    return "Use a search engine idiot!"

def get_name():
    return "Your name is " + getpass.getuser()

def weather():
    return "Check your weather app!"



