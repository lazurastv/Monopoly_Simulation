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
                parameters = convert_parameters(command, function_tuple)
                run_function(function_tuple, parameters)
            except KeyError:
                print("Invalid function! Try: ", self.keywords.keys())
            except NotEnoughParameters:
                print("Not enough parameters!")
            except TooManyParameters:
                print("Too many parameters!")
            except ValueError:
                print(ValueError)

    def get_function(self, command):
        function_tuple = self.keywords.get(command[0], None)
        if function_tuple:
            return function_tuple
        else:
            raise KeyError


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


def convert_parameter(value, conversion_type):
    return conversion_type(value)


def convert_parameters(command, function_tuple):
    check_parameter_count(command, function_tuple)
    parameter_values = []
    for i in range(1, len(function_tuple)):
        try:
            parameter_values.append(convert_parameter(command[i], function_tuple[i]))
        except ValueError:
            raise ValueError("Parameter ", i, " of type ", function_tuple[i])
    return parameter_values


def run_function(function_tuple, pars):
    function_tuple[0](*pars)
