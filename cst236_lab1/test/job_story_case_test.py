from unittest import TestCase
from test.plugins.ReqTracer import JobStory
from test.plugins.ReqTracer import requirements
from source.main import Interface
import datetime
import getpass
import time

class TestJobStories(TestCase):

# Datetime Test
    @requirements(['#0050', '#0051', '#0052'])
    @JobStory("When I ask \"What time is it?\" I want to be given the current date/time so I can stay up to date")
    def test_ask_date_time(self):
        new_interface = Interface()
        dateandtime = datetime.datetime.now()
        dateandtime = dateandtime.replace(second=0, microsecond=0)
        start_time = time.clock()
        result = new_interface.ask("What time is it?")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, str(dateandtime))

# Fibonacci Tests
    @JobStory("When I ask \"What is the n digit of fibonacci?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_fibbonacci_n_int(self):
        new_interface = Interface()
        result = new_interface.ask("What is the 5 digit of fibonacci?")
        self.assertEqual(result, 5)

    @JobStory("When I ask \"What is the n digit of fibonacci?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_fibbonacci_n_float(self):
        new_interface = Interface()
        result = new_interface.ask("What is the 5.3 digit of fibonacci?")
        self.assertEqual(result, 5)

    @JobStory("When I ask \"What is the n digit of fibonacci?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_fibbonacci_n_negative(self):
        new_interface = Interface()
        result = new_interface.ask("What is the -5 digit of fibonacci?")
        self.assertEqual(result, "Invalid Number")

    @JobStory("When I ask \"What is the n digit of fibonacci?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_fibbonacci_n_zero(self):
        new_interface = Interface()
        result = new_interface.ask("What is the 0 digit of fibonacci?")
        self.assertEqual(result, 0)

    @JobStory("When I ask \"What is the n digit of fibonacci?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_fibbonacci_n_no_parameter(self):
        new_interface = Interface()
        result = new_interface.ask("What is the r digit of fibonacci?")
        self.assertEqual(result, "No parameter given in get_fibonacci function")

# Pi Tests
    @JobStory("When I ask \"What is the n digit of pi?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_pi_int(self):
        new_interface = Interface()
        result = new_interface.ask("What is the 5 digit of pi?")
        self.assertEqual(result, 5)

    @JobStory("When I ask \"What is the n digit of pi?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_pi_float(self):
        new_interface = Interface()
        result = new_interface.ask("What is the 5.0 digit of pi?")
        self.assertEqual(result, 5)

    @JobStory("When I ask \"What is the n digit of pi?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_pi_negative(self):
        new_interface = Interface()
        result = new_interface.ask("What is the -5 digit of pi?")
        self.assertEqual(result, "Invalid Number")

    @JobStory("When I ask \"What is the n digit of pi?\" I want to receive the answer so I don't have to figure it out myself")
    def test_ask_pi_zero(self):
        new_interface = Interface()
        result = new_interface.ask("What is the 0 digit of pi?")
        self.assertEqual(result, "Invalid Number")

# Clear Memory Test
    @requirements(['#0050', '#0051', '#0052'])
    @JobStory("When I ask \"Please clear memory.\" I was the application to clear user set questions and answers so I can reset the application")
    def test_ask_clear_memory(self):
        new_interface = Interface()
        new_interface.ask("How crappy are you?")
        new_interface.teach("I am very crappy")
        clear_mem_return = new_interface.ask("Please clear memory.")
        self.assertEqual(clear_mem_return, "Memory cleared!")
        start_time = time.clock()
        result = new_interface.ask("How crappy are you?")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, "I don't know, please provide the answer")

# Open The Door Test
    @requirements(['#0050', '#0051', '#0052'])
    @JobStory("When I say \"Open the door hal!\", I want the application to say \"I'm afraid I can't do that <user name> so I know that is not an option")
    def test_ask_open_door(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Open the door hal!")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, "I'm afraid I can't do that " + getpass.getuser())

# Coversion Tests
    @requirements(['#0050', '#0051', '#0052'])
    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_cm_m_int(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Convert 500 cm to m.")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, 5)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_cm_m_float(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 25 cm to m.")
        self.assertEqual(result, .25)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_m_km(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 5000 m to km.")
        self.assertEqual(result, 5)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_km_m(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 23 km to m.")
        self.assertEqual(result, 23000)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_mm_km(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 100 mm to km.")
        self.assertEqual(result, 0.0001)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_lbs_kg(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 100 kg to lbs.")
        self.assertAlmostEqual(result, 220)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_kg_lbs(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 220 lbs to kg.")
        self.assertAlmostEqual(result, 100)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_kg_g(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 1 kg to g.")
        self.assertEqual(result, 1000)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_kg_mg(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 1 kg to mg.")
        self.assertEqual(result, 10000)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_gallon_pint(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 15 gallon to pint.")
        self.assertEqual(result, 120)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_gallon_quart(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 20 gallon to quart.")
        self.assertEqual(result, 80)

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_invalid_input(self):
        new_interface = Interface()
        result = new_interface.ask("Convert P gallon to quart.")
        self.assertEqual(result, "invalid input")

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_invalid_km_lbs(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 10 km to lbs.")
        self.assertEqual(result, "invalid conversion")

    @JobStory("When I ask \"Convert <number> <units> to <units>.\" I want to receive the converted value and units so I can know the answer.")
    def test_convert_invalid_lbs_quart(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 10 lbs to quart.")
        self.assertEqual(result, "invalid conversion")

    @JobStory("When I ask for a numberic conversion I want at least 10 different units I can convert from/to")
    def test_convert_invalid_gallon_km(self):
        new_interface = Interface()
        result = new_interface.ask("Convert 10 gallon to km.")
        self.assertEqual(result, "invalid conversion")

# Add Tests
    @requirements(['#0050', '#0051', '#0052'])
    @JobStory("When I say \"Please add num1 and num2.\" I want to receive the added result of two numbers.")
    def test_my_add_int(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Please add 1 and 2.")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, 3)

    @JobStory("When I say \"Please add num1 and num2.\" I want to receive the added result of two numbers.")
    def test_my_add_float(self):
        new_interface = Interface()
        result = new_interface.ask("Please add 1.0 and 2.0.")
        self.assertEqual(result, 3.0)

    @JobStory("When I say \"Please add num1 and num2.\" I want to receive the added result of two numbers.")
    def test_my_add_invalid_number(self):
        new_interface = Interface()
        result = new_interface.ask("Please add something with something.")
        self.assertEqual(result, "I don't know, please provide the answer")

# Subtract Tests
    @requirements(['#0053'])
    @JobStory("When I say \"Please subtract num1 and num2.\" I want to receive the subtracted result of two numbers.")
    def test_my_subtract_int(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Please subtract 1 and 2.")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, -1)

    @requirements(['#0053'])
    @JobStory("When I say \"Please subtract num1 and num2.\" I want to receive the subtracted result of two numbers.")
    def test_my_subtract_float(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Please subtract 1.0 and 2.0.")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, -1.0)

    @requirements(['#0053'])
    @JobStory("When I say \"Please subtract num1 and num2.\" I want to receive the subtracted result of two numbers.")
    def test_my_subtract_invalid_number(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Please subtract something with something.")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .05)
        self.assertEqual(result, "I don't know, please provide the answer")

# Divide Tests
    @requirements(['#0055'])
    @JobStory("When I say \"Please divide num1 and num2.\" I want to receive the divided result of two numbers.")
    def test_my_divide_int(self):
        new_interface = Interface()
        result = new_interface.ask("Please divide 10 and 2.")
        self.assertEqual(result, 5)

    @requirements(['#0055'])
    @JobStory("When I say \"Please divide num1 and num2.\" I want to receive the divided result of two numbers.")
    def test_my_divide_float(self):
        new_interface = Interface()
        result = new_interface.ask("Please divide 10.0 and 2.0.")
        self.assertEqual(result, 5.0)

    @requirements(['#0055'])
    @JobStory("When I say \"Please divide num1 and num2.\" I want to receive the divided result of two numbers.")
    def test_my_divide_invalid_number(self):
        new_interface = Interface()
        result = new_interface.ask("Please divide something with something.")
        self.assertEqual(result, "I don't know, please provide the answer")

# Multiply Tests
    @requirements(['#0054'])
    @JobStory("When I say \"Please multiply num1 and num2.\" I want to receive the multiplied result of two numbers.")
    def test_my_multiply_int(self):
        new_interface = Interface()
        result = new_interface.ask("Please multiply 10 and 2.")
        self.assertEqual(result, 20)

    @requirements(['#0054'])
    @JobStory("When I say \"Please multiply num1 and num2.\" I want to receive the multiplied result of two numbers.")
    def test_my_multiply_float(self):
        new_interface = Interface()
        result = new_interface.ask("Please multiply 10.0 and 2.0.")
        self.assertEqual(result, 20.0)

    @requirements(['#0054'])
    @JobStory("When I say \"Please multiply num1 and num2.\" I want to receive the multiplied result of two numbers.")
    def test_my_multiply_invalid_number(self):
        new_interface = Interface()
        result = new_interface.ask("Please multiply something with something.")
        self.assertEqual(result, "I don't know, please provide the answer")

# Mod Tests
    @requirements(['#0056'])
    @JobStory("When I say \"Please mod num1 and num2.\" I want to receive the moded result of two numbers.")
    def test_my_mod_int(self):
        new_interface = Interface()
        result = new_interface.ask("Please mod 43 and 5.")
        self.assertEqual(result, 3)

    @requirements(['#0056'])
    @JobStory("When I say \"Please mod num1 and num2.\" I want to receive the moded result of two numbers.")
    def test_my_mod_float(self):
        new_interface = Interface()
        result = new_interface.ask("Please mod 43.0 and 5.0.")
        self.assertEqual(result, 3.0)

    @requirements(['#0056'])
    @JobStory("When I say \"Please mod num1 and num2.\" I want to receive the moded result of two numbers.")
    def test_my_mod_invalid_number(self):
        new_interface = Interface()
        result = new_interface.ask("Please mod something with something.")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0057'])
    @JobStory("When I ask \"Are you happy?\" I want to receive the answer \"I'm always happy!\"")
    def test_always_happy(self):
        new_interface = Interface()
        start_time = time.clock()
        result = new_interface.ask("Are you happy?")
        end_time = time.clock()
        self.assertLess(end_time - start_time, .02)
        self.assertEqual(result, "I'm always happy!")

    @JobStory("When I ask \"Where can I go to have a good time?\" I want to receive the answer \"Club\".")
    def test_good_time(self):
        new_interface = Interface()
        result = new_interface.ask("Where can I go to have a good time?")
        self.assertEqual(result, "Club")

    @JobStory("When I ask \"Which is the best restaurant around here?\" I want to receive the answer \"Use a search engine idiot!\".")
    def test_best_restaurant(self):
        new_interface = Interface()
        result = new_interface.ask("Which is the best restaurant around here?")
        self.assertEqual(result, "Use a search engine idiot!")

    @JobStory("When I ask \"What is my name?\" I want to receive the answer \"Your name is <username>\".")
    def test_your_name(self):
        new_interface = Interface()
        result = new_interface.ask("What is my name?")
        self.assertEqual(result, "Your name is " + getpass.getuser())

    @JobStory("When I ask \"How is the weather going to be tomorrow?\" I want to receive the answer \"Check your weather app!\"")
    def test_weather(self):
        new_interface = Interface()
        result = new_interface.ask("How is the weather going to be tomorrow?")
        self.assertEqual(result, "Check your weather app!")