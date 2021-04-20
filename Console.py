class Console:

    def __init__(self, keywords: dict, max_parameters):
        self.keywords = keywords
        self.max_parameters = max_parameters

    def parse_text(self, command: str):
        command = command.split()
        n = len(command)
        if n < 1:
            print("No command given!")
        elif n > self.max_parameters:
            print("Command has too many parameters!")
        else:
            try:
                function_tuple = self.get_function(command)
                check_parameter_count(command, function_tuple)
                self.convert_parameters(command, function_tuple)
            except KeyError:
                print("Invalid function! Try: ", self.keywords.keys())
            except NotEnoughParameters:
                print("Not enough parameters!")
            except TooManyParameters:
                print("Too many parameters!")
            except ValueError:
                print()

    def get_function(self, command):
        return self.keywords.get(command[0])

    def convert_parameters(self, command, function_tuple):
        parameter_values = []
        for i in range(1, len(command)):
            parameter_values.append(self.convert_parameter(command[i], function_tuple[i]))

    def convert_parameter(self, value, conversion_type):
        try:
            return Console.conversions[conversion_type](value)
        except ValueError:
            pass


class TooManyParameters(Exception):
    pass

class NotEnoughParameters(Exception):
    pass

def check_parameter_count(command, function_tuple):
    parameters_expected = len(function_tuple)
    parameters_given = len(command)
    if parameters_given > parameters_expected:
        raise TooManyParameters
    else:
        raise NotEnoughParameters