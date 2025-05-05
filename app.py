from flask import Flask, render_template, request,url_for
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        try:
            method_type = request.form['type']

            if method_type == 'type1':
                # Table input
                x_vals = list(map(float, request.form['x_vals'].split(',')))
                y_vals = list(map(float, request.form['y_vals'].split(',')))

                if len(x_vals) != len(y_vals):
                    result = "X and Y values must have the same length."
                else:
                    n = len(x_vals) - 1
                    h = (x_vals[-1] - x_vals[0]) / n
                    sum_y = sum(y_vals[1:-1])
                    result_value = (h / 2) * (y_vals[0] + y_vals[-1] + 2 * sum_y)
                    result = round(result_value, 6)

            elif method_type == 'type2':
                # Function input
                func_expr = request.form['function']
                a = float(request.form['a'])
                b = float(request.form['b'])
                n = int(request.form['n'])

                def f(x):
                    return eval(func_expr, {"x": x, "np": np, "__builtins__": {}})

                h = (b - a) / n
                x_vals = [a + i * h for i in range(n + 1)]
                y_vals = [f(x) for x in x_vals]
                sum_y = sum(y_vals[1:-1])
                result_value = (h / 2) * (y_vals[0] + y_vals[-1] + 2 * sum_y)
                result = round(result_value, 6)

        except Exception as e:
            result = f"Error: {e}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
