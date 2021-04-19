class Console:
    conversions = {
        "int": int,
        "str": str
    }

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
            self.parse_function(command)

    def parse_function(self, command):
        function_tuple = self.keywords.get(command[0], None)
        if not function_tuple:
            raise KeyError("Invalid function! Try: ", self.keywords.keys())

    def check_parameter_count(self, command, function_tuple):
        parameters_expected = len(function_tuple)
        parameters_given = len(command)
        if parameters_given == parameters_expected:
            self.convert_parameters(command, function_tuple)
        elif parameters_given > parameters_expected:
            print("Too many parameters!")
        else:
            print("Not enough parameters!")

    def convert_parameters(self, command, function_tuple):
        parameter_values = []
        for i in range(1, len(command)):
            next_paramater = self.convert_parameter(command[i], function_tuple[i])
            if next_paramater

    def convert_parameter(self, value, conversion_type):
        try:
            return Console.conversions[conversion_type](value)
        except ValueError:
