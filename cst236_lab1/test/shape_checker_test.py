"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from unittest import TestCase
from source.shape_checker import get_quadrilateral_type
from test.plugins.ReqTracer import requirements
from source.main import Interface

def return_a_string():
    str1 = "My favorite color is black."
    return str1

class TestGetTriangleType(TestCase):

# Int test
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(4, 4, 5)
        self.assertEqual(result, 'isosceles')

# Float test
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(2.0, 2.0, 2.0)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(1.0, 2.0, 3.0)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_float(self):
        result = get_triangle_type(2.0, 2.0, 5.0)
        self.assertEqual(result, 'isosceles')

# Char test
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_char(self):
        result = get_triangle_type('a', 'd', 'v')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_char(self):
        result = get_triangle_type('r', 'g', 'h')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_char(self):
        result = get_triangle_type('q', 'r', 'n')
        self.assertEqual(result, 'invalid')

# Float/Int combination test
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_float_int_combo(self):
        result = get_triangle_type(2, 2.0, 2.0)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_float_int_combo(self):
        result = get_triangle_type(1.0, 2, 3.0)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_float_int_combo(self):
        result = get_triangle_type(2.0, 2, 5)
        self.assertEqual(result, 'isosceles')

# Tuples test
    @requirements(['#0001'])
    def test_get_triangle_equilateral_tuple(self):
        tup1 = (2, 2, 2)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_get_triangle_scalene_all_tuple(self):
        tup1 = (1.0, 2, 3)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0001'])
    def test_get_triangle_isosceles_all_tuple(self):
        tup1 = (2, 2.0, 5)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_get_triangle_invalid_tuple(self):
        tup1 = (1, 2.0, 5, 43)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'invalid')

# List test
    @requirements(['#0001'])
    def test_get_triangle_equilateral_list(self):
        tup1 = [2, 2, 2]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_get_triangle_scalene_all_list(self):
        tup1 = [1.0, 2, 3]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_get_triangle_isosceles_all_list(self):
        tup1 = [2, 2.0, 5]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_get_triangle_invalid_list(self):
        tup1 = [1, 2.0, 5, 43]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'invalid')

# Dicionary test
    @requirements(['#0001'])
    def test_get_triangle_equilateral_dic(self):
        dic1 = {'one' : 1, 'two' : 1, 'three' : 1}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_get_triangle_scalene_all_dic(self):
        dic1 = {'one' : 1, 'two' : 2, 'three' : 3}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_get_triangle_isosceles_all_dic(self):
        dic1 = {'one' : 1, 'two' : 1, 'three' : 4}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_get_triangle_invalid_dic(self):
        dic1 = {'one' : 1, 'two' : 1, 'three' : 1, 'four' : 5}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'invalid')

# Zero and negative test
    @requirements(['#0001', '#0001'])
    def test_get_triangle_zero_neg(self):
        result = get_triangle_type(0, -5, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0001'])
    def test_get_triangle_two_zero(self):
        result = get_triangle_type(0, 4, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0001'])
    def test_get_triangle_all_zero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0001'])
    def test_get_triangle_all_neg(self):
        result = get_triangle_type(-6, -4, -3)
        self.assertEqual(result, 'invalid')


class TestGetQuadrilateralType(TestCase):

# Int test
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_type_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rect_type_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 2, 270, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 4, 180, 45, 45, 90)
        self.assertEqual(result, 'rhombus')

# Float test
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_type_all_float(self):
        result = get_quadrilateral_type(2.0, 2.0, 2.0, 2.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 3.0, 4.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rect_type_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 2.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 2.0, 270.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 4.0, 180.0, 45.0, 45.0, 90.0)
        self.assertEqual(result, 'rhombus')

# Char test
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_type_all_char(self):
        result = get_quadrilateral_type('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_some_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 3.0, 'f', 90.0, 90.0, 'b', 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rect_type_some_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 'k', 2.0, 90.0, 90.0, 'b', 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_some_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 'k', 2.0, 'f', 'v', 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_all_char(self):
        result = get_quadrilateral_type('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        self.assertEqual(result, 'invalid')

# Float/Int combination test
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_type_int_float_combo(self):
        result = get_quadrilateral_type(2, 2.0, 2, 2.0, 90, 90.0, 90, 90.0)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_int_float_combo(self):
        result = get_quadrilateral_type(1, 2.0, 3.0, 4, 90.0, 90, 90.0, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rect_type_int_float_combo(self):
        result = get_quadrilateral_type(1.0, 2, 1, 2.0, 90, 90.0, 90, 90.0)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_int_float_combo(self):
        result = get_quadrilateral_type(1.0, 2, 1, 2.0, 270, 90.0, 90, 90.0)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_int_float_combo(self):
        result = get_quadrilateral_type(1.0, 2.0, 1, 4, 180, 45, 45.0, 90.0)
        self.assertEqual(result, 'rhombus')

# Zero and negative test
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_type_neg_zero_combo(self):
        result = get_quadrilateral_type(0, 2.0, 2, -90, 90, -90.0, 0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_all_zeros(self):
        result = get_quadrilateral_type(0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rect_type_all_neg(self):
        result = get_quadrilateral_type(-2.0, -7, -9, -89, -65, -90.0, -180, -90.0)
        self.assertEqual(result, 'invalid')

class QuestionAnswerTest(TestCase):

    @requirements(['#0001', '#0006', '#0007', '#0012', '#0013'])
    def test_ask_question_equilateral(self):
        new_interface = Interface()
        result = new_interface.ask("What type of triangle is 2 2 2?")
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0006', '#0007', '#0012', '#0013'])
    def test_ask_question_scalene(self):
        new_interface = Interface()
        result = new_interface.ask("What type of triangle is 1 2 3?")
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0006', '#0007', '#0012', '#0013'])
    def test_ask_question_isosceles(self):
        new_interface = Interface()
        result = new_interface.ask("What type of triangle is 1 1 2?")
        self.assertEqual(result, 'isosceles')

    @requirements(['#0006', '#0007', '#0008'])
    def test_ask_question_invalid_question(self):
        new_interface = Interface()
        result = new_interface.ask("Hey are you?")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_question_no_question_mark(self):
        new_interface = Interface()
        result = new_interface.ask("What type of triangle is 4 5 2")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_question_with_ASCII_ques_mark(self):
        new_interface = Interface()
        result = new_interface.ask("What type of triangle is 4 5 2 0x3F")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0007', '#0010'])
    def test_ask_question_with_no_spaces(self):
        new_interface = Interface()
        result = new_interface.ask("Whatareyoudoing?")
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0007', '#0011'])
    def test_ask_question_90_percent_keyword(self):
        new_interface = Interface()
        result = new_interface.ask("What type of ryp triangle is 1 2 2?")
        self.assertEqual(result, "isosceles")

    @requirements(['#0006', '#0007', '#0012'])
    def test_ask_question_multiple_keywords(self):
        new_interface = Interface()
        result = new_interface.ask("What type of 1 triangle is 1 2?")
        self.assertEqual(result, "isosceles")

    @requirements(['#0006', '#0007', '#0014'])
    def test_ask_question_no_valid_match(self):
        new_interface = Interface()
        result = new_interface.ask("What kind of triangle is this?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0015'])
    def test_ask_teach(self):
        new_interface = Interface()
        new_interface.ask("How is the day today?")
        new_interface.teach("It's rainy today.")
        result = new_interface.ask("How is the day today?")
        self.assertEqual(result, "It's rainy today.")

    @requirements(['#0006', '#0007', '#0016', '#0020'])
    def test_ask_accept_function_pointer(self):
        new_interface = Interface()
        new_interface.ask("What is your favorite color?")
        new_interface.teach(return_a_string)
        result = new_interface.ask("What is your favorite color?")
        self.assertEqual(result, "My favorite color is black.")

    @requirements(['#0006', '#0007', '#0017', '#0021'])
    def test_teach_with_no_ask(self):
        new_interface = Interface()
        result = new_interface.teach("Help me create a dinasaur")
        self.assertEqual(result, "Please ask a question first")

    @requirements(['#0006', '#0007', '#0018'])
    def test_ask_teach_teach(self):
        new_interface = Interface()
        new_interface.ask("What is your favorite color?")
        new_interface.teach(return_a_string)
        result = new_interface.teach("Something important")
        self.assertEqual(result, "I don\'t know about that. I was taught differently")

    @requirements(['#0006', '#0007', '#0019'])
    def test_ask_correct(self):
        new_interface = Interface()
        new_interface.ask("What is your favorite color?")
        new_interface.correct("My new favorite color is red")
        result = new_interface.ask("What is your favorite color?")
        self.assertEqual(result, "My new favorite color is red")

