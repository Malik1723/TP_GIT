import os
from Xscade_Parser import get_equations_by_operator_name
def Is_Direct_Settable(Input_Signal,Path_DS_File):
    with open(Path_DS_File, "r") as file:
        Lines =file.readlines()
        for line in Lines:
            if Input_Signal in line:
                return True
    return False






def Is_Connected_To_Direct_Settable(Input,path_ds ):
    with open(path_ds, "r") as file:
        DS_File_Lines = file.readlines()
        for line in DS_File_Lines:
            if Input in line:
                return True
    return False
def Turn_The_final_Equation(Equ_Substutued):
    pass


def Check_Is_connected_To_Input(argument , Operator):
    Input_Implementations = turn_Input_Implementation_For_All_Operators()
    for key , value in Input_Implementations.items():
        if key == Operator and argument in Input_Implementations[key]:
            return True

    return False
def Backtracing_Generation(All_operators,Operator_Name_Selected , Desired_Signal,path_ds):
        BackTracing_Data= ""
        # Input_List_Tracked = [] # To Stock the signal
        Dependency = Extract_Dependecies_Between_Operators(All_operators)
        Signal_Depndecies = Extracting_Signal_Connexions(Dependency, All_operators)
        locale_Implementation = turn_Local_Implementation_For_All_Operators(All_operators)
        print(locale_Implementation)# 1
        Inputs_Implemntation = turn_Input_Implementation_For_All_Operators(All_operators)  # 2
        Output_Implementation = turn_Output_Implementation_for_All_Operators(All_operators)
        Input_Lists_for_the_Operator_Name_Selected = get_inputs_by_operator_name(All_operators,
                                                                                 Operator_Name_Selected)  # 3


        Output_Lists_for_the_Operator_Name_Selected = get_outputs_by_operator_name(All_operators,
                                                                                   Operator_Name_Selected)
        if Is_Connected_To_Direct_Settable(Desired_Signal,path_ds):  # Should Have True

            Ds_Name = Signal_Depndecies[Desired_Signal][0][1]#Here when i will increment the system it should be changed
            #print(Ds_Name)   #print(f"{Ds_Name} i moved until the signal " )
            BackTracing_Data+=f"\t\t\t\t\t;#Set: {Desired_Signal}:\n \t\t\t\t\t\t;#SetInput: {Ds_Name}\n"
            #print(f"\t\t\t\tThe '{Desired_Signal}' is directly_connected to : \n \t\t\t\t\t ==>The Direct_Settable signal_Named : {Ds_Name}\n")
            #file.write(f"The - {Desired_Signal}-  is directly_connected to : \n \t\t ==>The Direct_Settable signal_Named : {Ds_Name}")
            # add it to the rapport
        elif Desired_Signal in Input_Lists_for_the_Operator_Name_Selected:
            Previous_Operator = Signal_Depndecies[Desired_Signal][0][0]  # Previous_Operator
            # print(Previous_Operator)
            Out_Signal_For_Previous_Operator = Signal_Depndecies[Desired_Signal][0][1]  # The output connected to it
            Lcl_variable_associated_to_the_out_signal =Output_Implementation[Previous_Operator][Out_Signal_For_Previous_Operator][0]
            Local_Equation_for_the_current_operator = locale_Implementation[Previous_Operator]
            Input_Equation_for_the_current_operator = Inputs_Implemntation[Previous_Operator]
            Equation_substututed, Input_List_Tracked = Turn_substuated_equation(
                Lcl_variable_associated_to_the_out_signal, Local_Equation_for_the_current_operator,
                Input_Equation_for_the_current_operator)
            #print(Equation_substututed)
            BackTracing_Data+=f"The Signal : '{Desired_Signal}'  in '{Operator_Name_Selected}' :\n \t -Move to'{Previous_Operator}'\n \t\t ;#Set :{Out_Signal_For_Previous_Operator} \n \t\t\t -Equation:{Equation_substututed} \n \t\t\t\t  - ;#Set:{Input_List_Tracked}\n"
            #print(f"The signal {Desired_Signal}  u want to set it is  Localised in the Operator {Operator_Name_Selected} and to track it : \n \t -U should to move until the operator {Previous_Operator} and  Set : \n \t\t -Firstly the output : {Out_Signal_For_Previous_Operator} \n \t\t -The equation of this output is : {Equation_substututed} \n \t\t -In The same Operator , the inputs u should to track also are : {Input_List_Tracked}")
            if Input_List_Tracked:
                for inputa in Input_List_Tracked:
                    BackTracing_Data += Backtracing_Generation(All_operators,Previous_Operator, inputa, path_ds)
        elif Desired_Signal in Output_Lists_for_the_Operator_Name_Selected:
            Lcl_variable_associated_to_the_desired_signal = \
            Output_Implementation[Operator_Name_Selected][Desired_Signal][0]
            print(Lcl_variable_associated_to_the_desired_signal)
            lcl_Implemntation_for_this_op = locale_Implementation[Operator_Name_Selected]

            print(lcl_Implemntation_for_this_op)
            Inp_Implemntation_for_this_op = Inputs_Implemntation[Operator_Name_Selected]
            print(Inp_Implemntation_for_this_op)
            Equ_Impl, Input_List_Tracked = Turn_substuated_equation(Lcl_variable_associated_to_the_desired_signal,
                                                                    lcl_Implemntation_for_this_op,
                                                                    Inp_Implemntation_for_this_op)
            BackTracing_Data += f"Signal : {Desired_Signal}  in '{Operator_Name_Selected}' :\n \t - Equation : {Equ_Impl}\n \t\t ;#Set :{Input_List_Tracked} \t\t\t \n"
            print(BackTracing_Data)
            if Input_List_Tracked:
                for inp in Input_List_Tracked:
                    BackTracing_Data += Backtracing_Generation(All_operators, Operator_Name_Selected, inp, path_ds)

        return BackTracing_Data






def Turn_substuated_equation(lcl, lcl_Implementation, Input_Implementation):
    Inputs_Tracked = []
    # Étape 1 : Récupération des substitutions pour la clé donnée
    if lcl in lcl_Implementation:
        substitutions = lcl_Implementation[lcl]
        #print(substitutions)
        # Étape 2 : Substitution récursive des arguments
        arguments = []
        for (op, args) in substitutions:
            for arg in args:
                argument_substituted, inputs_tracked = Turn_substuated_equation(arg, lcl_Implementation, Input_Implementation)
                arguments.append(argument_substituted)
                Inputs_Tracked.extend(inputs_tracked)
        # Étape 3 : Construction de l'expression substituée
        expression = f"{op}({', '.join(arguments)})"
        #print(expression)
        #print(expression)
        # Étape 4 : Vérification et substitution finale
        for arg in Input_Implementation:
            if arg in expression:
                    input_value = Input_Implementation[arg][0]
                    expression = expression.replace(arg, input_value)
                    #print(expression)
                    Inputs_Tracked.append(input_value)

        # Étape 5 : Retour de l'expression substituée et des inputs trackés
        return expression, Inputs_Tracked
    else:
        # Si la clé n'est pas trouvée, retourner la clé elle-même
        return lcl, Inputs_Tracked

def turn_the_Bt_Report(All_operators, path_of_BT_Report_file, opt, Signal_Name, path_of_ds_file):
       file_path = os.path.join(path_of_BT_Report_file,'Backtracing_Report.txt')
       #print(file_path)
       with open(file_path , 'w') as file :
           file.write(Backtracing_Generation(All_operators,opt,Signal_Name,path_of_ds_file))
           #print(Backtracing_Generation(opt,Signal_Name,path_of_ds_file))

       return file_path


def get_inputs_by_operator_name(data, operator_name):
    inputs_list = []
    for operator in data:
        if operator['name'] == operator_name:
            inputs_list = [input['name'] for input in operator['inputs']]
            break
    return inputs_list
def get_outputs_by_operator_name(data, operator_name):
    outputs_list = []
    for operator in data:
        if operator['name'] == operator_name:
            outputs_list = [output['name'] for output in operator['outputs']]
            break
    return outputs_list

def get_locals_by_operator_name(data, operator_name):
    locals_list = []
    for operator in data:
        if operator['name'] == operator_name:
            locals_list = [local['name'] for local in operator['locals']]
            break
    return locals_list






def clear_the_content_of_the_Report_File(file):
     open (file , 'w').close()




def turn_Output_Implementation_for_All_Operators(All_Operators):
    Output_Implementation = {}
    for opt in All_Operators:
        Op_name = opt['name']
        Op_Equation = opt['Equations']
        Lis_Out_for_this_Op = get_outputs_by_operator_name(All_Operators,Op_name)
        for out in Lis_Out_for_this_Op:
            for equ_out in Op_Equation:
                Out_side_Equ = equ_out['output']
                Inp_Side_Equ = equ_out['inputs']
                if out in Out_side_Equ and  isinstance(Inp_Side_Equ , list) and "Simple_Assignement" in Inp_Side_Equ:
                    Local_Variable = Inp_Side_Equ[0]
                    Output_Implementation.setdefault(Op_name , {}).setdefault(out , []).append((Local_Variable))

    return Output_Implementation


def Choose_Operator(All_operators):
    List_of_Operators = []
    for op in All_operators:
        op_name = op['name']
        List_of_Operators.append(op_name)
    return List_of_Operators


def turn_Local_Implementation_For_All_Operators(All_Operators):
    Locale_Implementation = {}
    for opt in All_Operators:
        Op_Name_lcl = opt['name']
        Op_Equation_lcl = opt['Equations']
        List_Lcl_For_This_Op = get_locals_by_operator_name(All_Operators , Op_Name_lcl)
        for lcl in List_Lcl_For_This_Op:
            for equ in Op_Equation_lcl:
                Out_Lcl_Equation = equ['output']
                Inp_lcl_Equation = equ['inputs']
                if lcl in Out_Lcl_Equation and  isinstance(Inp_lcl_Equation , list) and  "Simple_Assignement" not in  Inp_lcl_Equation:
                    for inp in Inp_lcl_Equation:
                        if "manipulation_name" in inp:
                            operand = inp['operator']
                            arguments = inp['operands']
                            Locale_Implementation.setdefault(Op_Name_lcl, {}).setdefault(lcl , []).append((operand ,arguments))
                        elif "Operator_Called" in inp:
                            operator_called = inp['Operator_Called']
                            arguments_call_expression = inp['arguments']
                            Locale_Implementation.setdefault(Op_Name_lcl, {}).setdefault(lcl, []).append((operator_called,
                                                                                                      arguments_call_expression))
                        elif "Unary_Process" in inp :
                            operand_implemented = inp[1]
                            arguments = inp[2]
                            Locale_Implementation.setdefault(Op_Name_lcl , {}).setdefault(lcl , []).append((operand_implemented ,arguments))
    return Locale_Implementation


def turn_Input_Implementation_For_All_Operators(All_Operators):
    Inputs_Implemntation = {}
    for opt in All_Operators:

        Op_name = opt['name']
        Op_Equation = opt['Equations']
        List_Inp_for_this_Op = get_inputs_by_operator_name(All_Operators, Op_name)
        for inp in List_Inp_for_this_Op:
            for equ in Op_Equation:
                Out_equ_Side = equ['output']
                Inp_equ_Side = equ['inputs']
                if isinstance(Inp_equ_Side, list) and "Simple_Assignement" in Inp_equ_Side:
                    if inp in Inp_equ_Side:
                        Locale_Associated = Out_equ_Side[0]
                        Inputs_Implemntation.setdefault(Op_name, {}).setdefault(Locale_Associated , []).append((inp))
    return Inputs_Implemntation

Dependecies= {}
Signal_Depndecies ={}
def Extract_Dependecies_Between_Operators(All_Operators):

    for operator in All_Operators:
        Operator_Name = operator['name']

        Dependecies[Operator_Name] = {"calls" : {} , "Called_By" : {}}
        Operator_Equations = operator['Equations']
        for eq in Operator_Equations:
            for Input_Item in eq['inputs']:
                if isinstance(Input_Item,dict) and 'Operator_Called' in Input_Item:
                    Inclued_Operator = Input_Item['Operator_Called']
                    #print(Inclued_Operator)
                    Arguments = Input_Item['arguments']
                    #print(Arguments)
                    if Inclued_Operator.startswith(('math::' , 'lib::')):
                        continue
                    Dependecies[Operator_Name]['calls'].setdefault(Inclued_Operator ,[] ).append(Arguments)
        for other_operator in All_Operators:
            other_operator_name = other_operator['name']
            if other_operator_name!= Operator_Name:
                other_operator_equations= other_operator['Equations']
                for equations in other_operator_equations:
                    for input_equation_side in equations['inputs']:
                        if isinstance(input_equation_side , dict) and 'Operator_Called' in input_equation_side:
                            Caller_Operator = input_equation_side['Operator_Called']
                            Arguments_Gived = input_equation_side['arguments']
                            if Caller_Operator ==Operator_Name:
                                Dependecies[Operator_Name]['Called_By'].setdefault(other_operator_name, []).extend(
                                    Arguments_Gived)

    return Dependecies


def Is_Input_Signal(Operator_Name ,Local_Signal_from_argument , Data):  #Second function to test the signal is input or not

        for operator in Data:
            if Operator_Name == operator['name']:
                for equ in operator['Equations']:
                    for output_equation in equ['output']:
                        if output_equation == Local_Signal_from_argument:
                            for input_side_equation in equ['inputs']:
                                if isinstance(equ['inputs'] , list) and equ['inputs'][-1] == "Simple_Assignement":
                                    input_assignement = equ['inputs'][0]
                                    return input_assignement


def Extracting_Signal_Connexions(Dependecies ,All_Operators):

        for operator in All_Operators: # loop in all the operator
            Operator_name = operator['name'] # extraire le nom d l operateur
            Operator_Inputs = get_inputs_by_operator_name(All_Operators , Operator_name) # les inputs de cet operater
            Operator_Outputs = get_outputs_by_operator_name(All_Operators , Operator_name) # les outputs de cet operateur
            Dependecies_Dictionnary = Dependecies[Operator_name]['Called_By'] #Le dictionnaire qui contient les operateur appelllant
            for operator , argument in Dependecies_Dictionnary.items(): #Dans cette operateur je veux voir l operateur appellant et les arguments (key , value )
                Operator_Caller = operator  #clé c'est l operateur
                Arguments_Passed = argument # la liste des arguments
                for index , argument  in enumerate(Arguments_Passed):  # Je veux parcouri l'argument
                    Input_Tracked = get_inputs_by_operator_name(All_Operators , Operator_name)[index]  # extraire l inout adéquat
                    for other_operator in All_Operators: #Parcourir une autre fois les operateurs
                        if other_operator['name'] == Operator_Caller: # localise l operateur adéquat
                            Equations_Operator_Called = other_operator['Equations'] # extraire ces équations
                            for equ in Equations_Operator_Called: #Parcouir ces équations
                                Input_side_equations = equ['inputs'] #Extraire ce inputs
                                Output_side_equations = equ['output'] #extraire ces outputs
                                if argument in Output_side_equations and isinstance(Input_side_equations , list) and "Simple_Assignement" in Input_side_equations: # si l argument est dans la partie output et simple assignment est dans la partie input
                                    Signal_Name = Input_side_equations[0]
                                    Signal_Depndecies.setdefault(Input_Tracked , []).append((Operator_Caller,Signal_Name))

                                elif argument in Output_side_equations :
                                    if isinstance(Input_side_equations ,list):
                                        for item in Input_side_equations:
                                            if "Operator_Called" in item:
                                                Successor_Operator = item["Operator_Called"]
                                                Signal_Name_for_successor = get_outputs_by_operator_name(All_Operators , Successor_Operator)[0]
                                                Signal_Depndecies.setdefault(Input_Tracked, []).append((Successor_Operator,Signal_Name_for_successor))


        return Signal_Depndecies






















