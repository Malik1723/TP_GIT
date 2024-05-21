import re


def turn_the_final_equation(expression):
    begin_of_expression = expression.find('(')
    print(begin_of_expression)
    main_operator =expression[:begin_of_expression]
    print(main_operator)
    sub_exprssion=expression[begin_of_expression+1:-2]
    print(sub_exprssion)
    pattern = r",(?![^()]*\))"
    sub_exprssion = re.sub(pattern, main_operator, sub_exprssion)
    #print(sub_exprssion)
    return sub_exprssion










    #return sub_exprssion






equation =  " and(>=(math::Abs(cHILD3_IN1), *(cHILD3_IN2, -(cHILD3_IN3))), not(<=(math::Abs(cHILD3_IN4), math::Sign(cHILD3_IN5))))"
final_equ = turn_the_final_equation(equation)
print(final_equ)

