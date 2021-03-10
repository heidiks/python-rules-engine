import json

class FormulaRequest:
    def __init__(self, variables, formula):
        self.variables = variables
        self.formula = formula

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class FormulaResponse:
    def __init__(self, variables, tracking):
        self.variables = variables
        self.tracking = tracking

    def __init__(self, request, exec_response):
        self.variables_formula = {}
        for key, value in exec_response.items():
            if key.startswith("s_"):
                self.variables_formula[key] = value

        self.variables = request.variables
        self.tracking = 'to implement'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def calculate_formula(request):
    variables_code = ''

    for key, value in request.variables.items():
        variables_code += key + '=' + value + ';'

    exec_response = {}
    exec(variables_code + request.formula, globals(), exec_response)

    formula_response = FormulaResponse(request, exec_response)
    return formula_response


