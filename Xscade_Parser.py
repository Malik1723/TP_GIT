import xml.etree.ElementTree as ET
import os


def get_inputs(root, namespace):
    Inputs_Data = root.findall('./ns:inputs/ns:Variable', namespace)
    inputs = []

    #globals(inputs)
    for input in Inputs_Data:
        Inputs = {
            'name': input.attrib['name'],
            'data_type': input.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef', namespace).attrib['name']

        }
        inputs.append(Inputs)
    return inputs
def get_outputs(root, namespace):
    Outputs_Data = root.findall('./ns:outputs/ns:Variable', namespace)
    outputs = []
    for output in Outputs_Data:
        Outputs = {
            'name': output.attrib['name'],
            'data_type': output.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef', namespace).attrib['name'],
        }
        outputs.append(Outputs)
    return outputs

def get_locals(root, namespace):
    Locals_Data = root.findall('./ns:locals/ns:Variable', namespace)
    locals_list = []
    for Local in Locals_Data:
        Locals = {
            'name': Local.attrib['name'],
            'data_type': Local.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef', namespace).attrib['name'],
        }
        locals_list.append(Locals)
    return locals_list


def get_outputs(root, namespace):
    Outputs_Data = root.findall('./ns:outputs/ns:Variable', namespace)
    outputs = []
    #globals(outputs)
    for output in Outputs_Data:
        Outputs = {
            'name': output.attrib['name'],
            'data_type': output.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef', namespace).attrib['name'],

        }
        outputs.append(Outputs)
    return outputs


def process_equations(root, namespace):
    equations_list = []
    #globals(equations_list)
    Data_system_Equation = root.findall('./ns:data/ns:Equation', namespace)

    for equation in Data_system_Equation:

        lefts = equation.findall('./ns:lefts/ns:VariableRef', namespace)
        #globals(lefts)



        rights_element = equation.findall('./ns:right/', namespace)
        rights_element_tag = equation.find('./ns:right', namespace)
        Equations1 = {

            'output': [left.attrib['name'] for left in lefts],
            'inputs': []

        }
        sibling_tag = rights_element_tag[0].tag.split('}')[-1]

        for right in rights_element:
            if sibling_tag == 'CallExpression':
                Call_Expression = {'Operator_Called': '',
                                   'arguments':[]}
                if (right[0][0].tag).split('}')[-1] == 'FlattenOp':
                    Call_Expression['operator_Called'] = right.find('./ns:operator/ns:FlattenOp/ns:type/ns:TypeRef', namespace).attrib['name']
                else:
                    Call_Expression['Operator_Called'] = right.find('./ns:operator/ns:OpCall/ns:operator/*', namespace).attrib['name']
                Call_Parameters = right.findall('./ns:callParameters/', namespace)
                for Call in Call_Parameters:
                    variable = Call.find('./ns:path/*', namespace).attrib['name']
                    Call_Expression['arguments'].append(variable)
                Equations1['inputs'].append(Call_Expression)
            elif sibling_tag == 'IdExpression':
                VariableName = right.find('./ns:path/ns:ConstVarRef', namespace).attrib['name']
                Manipulation_name = 'Simple_Assignement'
                Equations1['inputs'].append(VariableName)
                Equations1['inputs'].append(Manipulation_name)
            elif sibling_tag == 'BinaryOp':
                manipulation_name = 'Binary_Operation'
                Variable_name_Binary_Op = {'manipulation_name': 'Binary_Operation',
                                           'operator': [],
                                           'operands': []}
                Operator = right.attrib['operator']
                Variable_name_Binary_Op['operator']=Operator
                Operands = right.findall('./ns:operands/ns:IdExpression', namespace)
                for operand in Operands:
                    operandName = operand.find('./ns:path/ns:ConstVarRef', namespace).attrib['name']
                    Variable_name_Binary_Op['operands'].append(operandName)
                Equations1['inputs'].append(Variable_name_Binary_Op)
            elif sibling_tag == 'NAryOp':
                NAry_Operations = {
                'manipulation_name' : 'Logical_Operator',

                'operator': right.attrib['operator'],
                'operands': []
                }
                Operator = right.attrib['operator']
                NAry_Operations['operator'] = Operator
                arguments = right.findall('./ns:operands/', namespace)
                for argument in arguments:
                    Passed_Parametre = argument.find('./ns:path/ns:ConstVarRef', namespace).attrib['name']
                    NAry_Operations['operands'].append(Passed_Parametre)
                Equations1['inputs'].append(NAry_Operations)
            elif sibling_tag == 'ConstValue':
                Constant_Value = right.attrib['value']
                Equations1['inputs'].append(Constant_Value)
            elif sibling_tag == 'UnaryOp':
                Un = []
                Un_Process_Name = "Unary_Process"
                UnaryOp = right.attrib['operator']
                Unary_Operand = [right.find('./ns:operand/ns:IdExpression/ns:path/ns:ConstVarRef', namespace).attrib[
                    'name']]
                Un.append(Un_Process_Name)
                Un.append(UnaryOp)
                Un.append(Unary_Operand)
                Equations1['inputs'].append(Un)
            elif sibling_tag == 'IfThenElseOp':
                If_Else_condition = {
                    'Manipulation_Name': " ",
                    'Activate_condition': None,
                    'First_Condition': None,
                    'Second_Condition': None,
                    'Arguments': []
                }
                Activation_Condition = right.find('./ns:if/ns:IdExpression/ns:path/ns:ConstVarRef', namespace).attrib[
                    'name']
                If_Else_condition['Activate_condition'] = Activation_Condition
                If_Else_condition['Arguments'].append(Activation_Condition)
                Default_Condition = \
                right.find('ns:then/ns:ListExpression/ns:items/ns:IdExpression/ns:path/ns:ConstVarRef',
                           namespace).attrib['name']
                If_Else_condition['First_Condition'] = Default_Condition
                If_Else_condition['Arguments'].append(Default_Condition)
                Else_Condition = right.find('ns:else/ns:ListExpression/ns:items/ns:IdExpression/ns:path/ns:ConstVarRef',
                                            namespace).attrib['name']
                If_Else_condition['Second_Condition'] = Else_Condition
                If_Else_condition['Arguments'].append(Else_Condition)
                Equations1['inputs'].append(If_Else_condition)
            elif sibling_tag == 'FbyOp':
                FBY_Implementation = {
                    'Inputs': None,
                    'Delay': None,
                    'Init': None,
                    'Arguments': []
                }
                Input = right.find("ns:flows/ns:IdExpression/ns:path/ns:ConstVarRef", namespace).attrib['name']
                FBY_Implementation['Arguments'].append(Input)
                Delay = right.find("ns:delay/ns:ConstValue", namespace).attrib['value']
                FBY_Implementation['Arguments'].append(Delay)
                Init_Value = right.find("ns:values/ns:ConstValue", namespace).attrib['value']
                FBY_Implementation['Arguments'].append(Init_Value)
                Equations1['inputs'].append(FBY_Implementation)
        equations_list.append(Equations1)

    return equations_list














def get_equations_by_operator_name(data, operator_name):
    equations_list = []
    for operator in data:
        if operator['name'] == operator_name:
            equations_list = operator['Equations']
            break
    return equations_list


def transform_equations(equations_list):
    transformed_equations = []
    for equation in equations_list:
        output = equation['output'][0]
        inputs = equation['inputs']
        input_str = ""
        for input_item in inputs:
            if isinstance(input_item, dict) and 'Operator_Called' in input_item:
                operator_called = input_item['Operator_Called']
                arguments = ", ".join(input_item['arguments'])
                input_str += f"{operator_called}({arguments}), "
            elif isinstance(input_item, dict) and 'inputs' in input_item:
                input_str += ", ".join(input_item['inputs'])
            else:
                input_str += str(input_item)
            input_str += ", "
        input_str = input_str.rstrip(', ')
        transformed_equation = f"{output} = {input_str}"
        transformed_equations.append(transformed_equation)
    return transformed_equations
def process_equations_list(equations):
    for idx, equation in enumerate(equations, start=1):
        parts = equation.split(" = ")
        output_variable = parts[0]
        input_expression = parts[1]
        print(f"Equation {idx}:")
        print(f"Output: {output_variable}")
        print(f"Input: {input_expression}")
        print()

# Exemple d'utilisation :









#extraction the dictionnaire of output in fucntion of locales





#extraction the dictionnaire of inputs in functipon of locales





#extraction the other dictionnaire that have the implémentation