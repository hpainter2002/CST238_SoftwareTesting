from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answers import get_date_time_string, get_fibonacci, get_pi_digit, open_the_door, convert, my_add, \
    my_subtract, my_divide, my_multiply, my_mod, always_happy, good_time, best_restaurant, get_name, weather
import difflib

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", 'Please', 'Open', 'Are', 'Which']
        self.question_mark = chr(0x3F)
        self.exclamation_point = chr(0x21)
        self.period = chr(0x2E)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type, True),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What time is it ' : QA('What time is it', get_date_time_string),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', get_fibonacci),
            'What is the n digit of pi ': QA('What is the n digit of pi ', get_pi_digit),
            'Please clear memory ': QA('Please clear memory ', self.clear_memory),
            'Open the door hal ': QA('Open the door hal ', open_the_door),
            'Convert <number> <units> to <units>': QA('convert <number> to ', convert),
            'Please add and ': QA('Please add and ', my_add),
            'Please subtract and ': QA('Please subtract and ', my_subtract),
            'Please divide and ': QA('Please divide and ', my_divide),
            'Please multiply and ': QA('Please multiply and ', my_multiply),
            'Please mod and ': QA('Please mod and ', my_mod),
            'Are you happy ': QA('Are you happy ', always_happy),
            'Where can I go to have a good time ': QA('Where can I go to have a good time ', good_time),
            'Which is the best restaurant around here ':QA('Which is the best restaurant around here ', best_restaurant),
            'What is my name ': QA('What is my name ', get_name),
            'How is the weather going to be tomorrow ': QA('How is the weather going to be tomorrow ', weather)
        }

        self.default_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type, True),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What time is it ' : QA('What time is it', get_date_time_string),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', get_fibonacci),
            'What is the n digit of pi ': QA('What is the n digit of pi ', get_pi_digit),
            'Please clear memory ': QA('Please clear memory ', self.clear_memory),
            'Open the door hal ': QA('Open the door hal ', open_the_door),
            'Convert <number> <units> to <units>': QA('convert <number> to ', convert),
            'Please add and ': QA('Please add and ', my_add),
            'Please subtract and ': QA('Please subtract and ', my_subtract),
            'Please divide and ': QA('Please divide and ', my_divide),
            'Please multiply and ': QA('Please multiply and ', my_multiply),
            'Please mod and ': QA('Please mod and ', my_mod),
            'Are you happy ': QA('Are you happy ', always_happy),
            'Where can I go to have a good time ': QA('Where can I go to have a good time ', good_time),
            'Which is the best restaurant around here ':QA('Which is the best restaurant around here ', best_restaurant),
            'What is my name ': QA('What is my name ', get_name),
            'How is the weather going to be tomorrow ': QA('How is the weather going to be tomorrow ', weather)
        }

        self.last_question = None

    def clear_memory(self):
        self.question_answers.clear()
        self.question_answers = self.default_answers
        return "Memory cleared!"

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark and question[-1] != self.exclamation_point and \
                        question[-1] != self.period or question.split(' ')[0] not in self.keywords:
            self.last_question = None

            if question.startswith("Convert"):
                question = question.rstrip('.')
                question = question.lstrip('Convert')
                question = question.lstrip(' ')
                number, unit1, delimiter, unit2 = question.split(' ', 4)

                try:
                    number = float(number)

                except ValueError:
                    return "invalid input"

                return convert(number, unit1, unit2)

            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except Exception as ex:
                            print(ex)
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)