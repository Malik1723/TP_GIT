import xml.etree.ElementTree as ET
import os


def get_inputs(root, namespace):
    try:
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
    except Exception as e :
        print("The probleme is in get inputs ")
def get_outputs(root, namespace):
    try:
        Outputs_Data = root.findall('./ns:outputs/ns:Variable', namespace)
        outputs = []
        for output in Outputs_Data:
            Outputs = {
                'name': output.attrib['name'],
                'data_type': output.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef', namespace).attrib['name'],
            }
            outputs.append(Outputs)
        return outputs
    except:
        print("The probleme is in get outputs  ")


def get_locals(root, namespace):
    try:
        Locals_Data = root.findall('./ns:locals/ns:Variable', namespace)
        locals_list = []
        for Local in Locals_Data:
            Locals = {
                'name': Local.attrib['name'],
                'data_type': Local.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef', namespace).attrib['name'],
            }
            locals_list.append(Locals)
        return locals_list
    except:
        print("The probleme is in get locals")

def process_equations(root, namespace):
   try :
       equations_list = []
       # globals(equations_list)
       Data_system_Equation = root.findall('./ns:data/ns:Equation', namespace)

       for equation in Data_system_Equation:

           lefts = equation.findall('./ns:lefts/ns:VariableRef', namespace)
           # globals(lefts)

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
                                      'arguments': []}
                   if (right[0][0].tag).split('}')[-1] == 'FlattenOp':
                       Call_Expression['operator_Called'] = \
                       right.find('./ns:operator/ns:FlattenOp/ns:type/ns:TypeRef', namespace).attrib['name']
                   else:
                       Call_Expression['Operator_Called'] = \
                       right.find('./ns:operator/ns:OpCall/ns:operator/*', namespace).attrib['name']
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
                   Variable_name_Binary_Op['operator'] = Operator
                   Operands = right.findall('./ns:operands/ns:IdExpression', namespace)
                   for operand in Operands:
                       operandName = operand.find('./ns:path/ns:ConstVarRef', namespace).attrib['name']
                       Variable_name_Binary_Op['operands'].append(operandName)
                   Equations1['inputs'].append(Variable_name_Binary_Op)
               elif sibling_tag == 'NAryOp':
                   NAry_Operations = {
                       'manipulation_name': 'Logical_Operator',

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
                   Activation_Condition = \
                   right.find('./ns:if/ns:IdExpression/ns:path/ns:ConstVarRef', namespace).attrib[
                       'name']
                   If_Else_condition['Activate_condition'] = Activation_Condition
                   If_Else_condition['Arguments'].append(Activation_Condition)
                   Default_Condition = \
                       right.find('ns:then/ns:ListExpression/ns:items/ns:IdExpression/ns:path/ns:ConstVarRef',
                                  namespace).attrib['name']
                   If_Else_condition['First_Condition'] = Default_Condition
                   If_Else_condition['Arguments'].append(Default_Condition)
                   Else_Condition = \
                   right.find('ns:else/ns:ListExpression/ns:items/ns:IdExpression/ns:path/ns:ConstVarRef',
                              namespace).attrib['name']
                   If_Else_condition['Second_Condition'] = Else_Condition
                   If_Else_condition['Arguments'].append(Else_Condition)
                   Equations1['inputs'].append(If_Else_condition)
               elif sibling_tag == 'FbyOp':
                   FBY_Implementation = {
                       'FbyOp': 'FBY',
                       'Inputs': "",
                       'Delay': "",
                       'Init': "",
                   }
                   FBY_Implementation['Inputs'] = (
                   right.find("ns:flows/ns:IdExpression/ns:path/ns:ConstVarRef", namespace).attrib['name'])

                   FBY_Implementation['Delay'] = right.find("ns:delay/ns:ConstValue", namespace).attrib['value']
                   FBY_Implementation['Init'] = right.find("ns:values/ns:ConstValue", namespace).attrib['value']
                   Equations1['inputs'].append(FBY_Implementation)
           equations_list.append(Equations1)

       return equations_list
   except:
       print("The problem is in The quations functions ")


def get_equations_by_operator_name(data, operator_name):
    try:
        equations_list = []
        for operator in data:
            if operator['name'] == operator_name:
                equations_list = operator['Equations']
                break
        return equations_list
    except:
        print("The probleme is in the get outputs by operator name ")