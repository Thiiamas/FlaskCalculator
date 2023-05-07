from flask import render_template, request, current_app as app


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def operation_result():
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['Operation']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        if operation == "+":
            result = input1 + input2
        elif operation == "-":
            result = input1 - input2
        elif operation == "/":
            result = input1 / input2
        elif operation == "*":
            result = input1 * input2
        elif operation == "%":
            result = input1 % input2    

        return render_template (
            'index.html',
            input1 = input1,
            input2 = input2,
            operation = operation,
            result = result,
            calculation_success = True
        )
    except ZeroDivisionError:
        return render_template (
            'index.html',
            input1 = input1,
            input2 = input2,
            operation = operation,
            result = "Bad Input",
            calculation_success = False,
            error = "You cannot divide by zero"
        )

    except ValueError:
        return render_template (
            'index.html',
            input1 = input1,
            input2 = input2,
            operation = operation,
            result = "Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided inputs"
        )
    except UnboundLocalError:
        return render_template (
            'index.html',
            input1 = input1,
            input2 = input2,
            operation = operation,
            result = "Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided inputs"
        )
