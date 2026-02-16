"""
    Module principal de l'application de calculatrice Flask

    Ce module configure le serveur Flask et gère le routage ainsi que
    la logique de calcul des expressions arithmétiques simples.
"""

from flask import Flask, request, render_template
from .operators import add, subtract, multiply, divide

# Initialisation de l'application Flask avec le dossier de templates personnalisé et le dossier de fichiers statiques
app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# Évalue une expression arithmétique simple avec un seul opérateur
def calculate(expr: str):
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Suppression des espaces pour simplifier le parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche l'opérateur dans l'expression
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Opérateur au début, à la fin ou non trouvé
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    # Conversion des opérandes en nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application
    Gère les requêtes GET et POST
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)