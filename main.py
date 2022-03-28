from flask import Flask, request, make_response
from motor_calculo import FormulaRequest, calculate_formula

app = Flask("rules-engine")

@app.route('/formula', methods=['POST'])
def formula():
    body = request.get_json()
    formula_request = FormulaRequest(body['variables'], body['formula'])

    calculated = calculate_formula(formula_request)
    response = make_response(calculated.to_json(), 200)
    response.headers["Content-Type"] = "application/json"
    return response


app.run()
