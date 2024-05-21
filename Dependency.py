from Backtracing_Generator import *
from Xscade_Parser import *






"""
def transform_expression(expression):
    # Définit les correspondances des opérateurs
    operator_mapping = {
        'or': 'or',
        'and': 'and',
        'not': 'not',
        '<=': '<=',
        '>=': '>=',
        '==': '==',
        '!=': '!=',
        '<': '<',
        '>': '>',
        '+': '+',
        '-': '-',
        '*': '*',
        '/': '/',
        'math::IntToBool': 'math::IntToBool',
        'math::BoolToFloat32': 'math::BoolToFloat32'
    }

    # Supprimer les espaces superflus
    expression = expression.replace(" ", "")

    # Fonction récursive pour transformer les sous-expressions
    def transform_recursive(expr):
        if not expr:
            return ""

        if expr.startswith('('):
            open_brackets = 0
            for i, char in enumerate(expr):
                if char == '(':
                    open_brackets += 1
                elif char == ')':
                    open_brackets -= 1
                if open_brackets == 0:
                    sub_expr = expr[1:i]
                    rest_expr = expr[i + 1:]
                    return transform_recursive(sub_expr) + transform_recursive(rest_expr)

        match = re.match(r'(\w+)\((.*)\)', expr)
        if match:
            operator = match.group(1)
            sub_expr = match.group(2)
            if operator in operator_mapping:
                if operator == 'not':
                    return f"not({transform_recursive(sub_expr)})"
                else:
                    arguments = split_arguments(sub_expr)
                    transformed_arguments = [transform_recursive(arg) for arg in arguments]
                    if operator == 'and' or operator == 'or':
                        return f"({' '.join([operator_mapping[operator]] * (len(transformed_arguments) - 1)).join(['('] + transformed_arguments + [')'])})"
                    else:
                        return f"{operator_mapping[operator]}({', '.join(transformed_arguments)})"

        return expr

    # Fonction pour diviser les arguments d'une fonction
    def split_arguments(args):
        arguments = []
        current_arg = []
        open_brackets = 0
        for char in args:
            if char == ',' and open_brackets == 0:
                arguments.append("".join(current_arg))
                current_arg = []
            else:
                current_arg.append(char)
                if char == '(':
                    open_brackets += 1
                elif char == ')':
                    open_brackets -= 1
        arguments.append("".join(current_arg))
        return arguments

    # Appliquer la transformation à l'expression initiale
    return transform_recursive(expression)

"""
# Exemple d'utilisation















