import json
from tracking import Tracking
import numpy


class BaseClass:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class FormulaRequest(BaseClass):
    def __init__(self, variables, formula):
        self.variables = variables
        self.formula = formula


class FormulaResponse(BaseClass):
    def __init__(self, variables, tracking):
        self.variables = variables
        self.tracking = tracking

    def __init__(self, request, exec_response, tracking):
        self.variables_formula = {}
        self.tracking = {}
        for key, value in exec_response.items():
            if key.startswith("s_"):
                self.variables_formula[key] = value
            if key.startswith("if_"):
                self.tracking[key] = value
            if key.startswith("else_"):
                self.tracking[key] = value

        self.tracking = {**tracking.map_conditionals, **self.tracking}

        self.variables = request.variables


def print_algo(algo):
    print(algo)


def avg(numbers):
    return numpy.mean(numbers)


def calculate_formula(request):
    variables_code = ''

    for key, value in request.variables.items():
        if isinstance(value, list):
            variables_code += key + '=' + '[' + ', '.join(value) + ']' + '\n'
        else:
            variables_code += key + '=' + value + '\n'

    exec_response = {}
    formula_with_variables = variables_code + request.formula
    tracking = Tracking(formula_with_variables)
    tracking.transform()

    exec(tracking.modified_code, globals(), exec_response)

    formula_response = FormulaResponse(request, exec_response, tracking)
    return formula_response
