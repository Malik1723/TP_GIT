import re


def traiter_expression(expression):
    if ',' not in expression:
        return expression
    main_operator = identifier_operateur_principal(expression)
    sous_expression = extraire_expression_sans_operateur_principal(expression,main_operator)
    sous_expression_remplacee = remplacer_virgules(sous_expression, main_operator)
    parties = diviser_expression(sous_expression_remplacee, main_operator)
    parties_traitees = [traiter_expression(partie) for partie in parties]
    expression_finale = combiner_expressions(parties_traitees, main_operator)
    return expression_finale

def identifier_operateur_principal(expression):
    begin_expression = expression.find('(')
    main_operator = expression[:begin_expression]
    return main_operator
def extraire_expression_sans_operateur_principal(expression, main_operator):
    begin_expression = expression.find('(')

    return expression[begin_expression+1:-1]

def remplacer_virgules(expression, main_operator):
    niveau_parenthese = 0
    result = []
    for char in expression:
        if char == '(':
            niveau_parenthese += 1
        elif char == ')':
            niveau_parenthese -= 1
        if char == ',' and niveau_parenthese == 0:
            result.append(f' "{main_operator}" ')
        else:
            result.append(char)
    return ''.join(result)

def diviser_expression(expression, operateur):
    # Diviser l'expression en parties en utilisant l'opérateur donné comme séparateur

    return expression.split(f"\"{operateur}\"")


def combiner_expressions(parties, operateur):
    # Combiner les parties traitées en une seule expression avec l'opérateur
    expression =  f' {operateur} '.join(parties)

    #expression = expression.replace(' ', '')  # remove empty spaces
    expression = expression.replace('(', '')  # remove left parentheses
    expression = expression.replace(')', '')  # remove right parentheses
    return expression


# Exemple d'utilisation:
expression = "or(not(cHILD2_IN1), math::IntToBool(cHILD2_IN2)) "
expression_finale = traiter_expression(expression)
print(expression_finale)