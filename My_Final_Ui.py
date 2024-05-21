import sys
from ressources import *
from Menu import Ui_MainWindow

from Xscade_Parser import *
from Backtracing_Generator import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QSpacerItem,QTextEdit , QGridLayout,QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QHBoxLayout ,QFormLayout ,QPushButton ,QComboBox , QFileDialog
from PyQt5.QtGui import QPixmap ,QFont ,QIcon
from PyQt5.QtCore import Qt

class My_Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Backtracing_Generator")

        pixmap = QPixmap(r"Logo-menu-actia (1).png")
        pixmap = pixmap.scaled(600, 600)  # Ajuster la taille à 30x30 pixels
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)


        self.Clear_Btn.clicked.connect(self.clear_report_file)

        self.Icon_Name.setHidden(True)
        self.Menu_Icon.clicked.connect(self.view_menu)
        self.Menu_buuton_name.clicked.connect(self.view_menu)
        self.add_project_icon.clicked.connect(self.view_project_management)
        self.Prj_Mng_button.clicked.connect(self.view_project_management)
        self.generate_icon.clicked.connect(self.view_report_generation)
        self.Generate_Nmae_btn.clicked.connect(self.view_report_generation)
        current_widget = self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget.removeWidget(current_widget)
        self.stackedWidget.setCurrentWidget(self.Welcome_window)

        self.Project_added = False
        self.DS_File = False
        self.report_folder_path = ""
        self.file = ""
        self.report_file = ""

        self.Clear8project_Button.clicked.connect(self.clear_project)
        self.Load_Project_Button.clicked.connect(self.upload_project_folder)
        self.Upload_DS_File_Button.clicked.connect(self.add_direct_settable_file)
        self.ADD_Project_Button.clicked.connect(self.Adding_Project)

        self.Generate_Btn.clicked.connect(self.on_generate_report_clicked)
        self.Choose_Report_Folder_Btn.clicked.connect(self.choose_report_folder)
    def on_generate_report_clicked(self):
        try:
            operator_selected = self.comboBox_operator.currentText()
            desired_signal_input = self.comboBox_Signal.currentText()
            report_folder_path = self.report_folder_path
            ds_file = self.file

            if not operator_selected or not desired_signal_input or not report_folder_path or not ds_file:
                QMessageBox.warning(self, "Missing Information",
                                    "Please ensure all fields are selected and files are uploaded.")
                return

            self.Generate_Backtracing_Report(report_folder_path, operator_selected, desired_signal_input, ds_file)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.Console_Prjt_BT_Gener.append(f"Error: {str(e)}")
            print(f"Error: {str(e)}")

    def clear_project(self):
        self.Project_added = False
        self.DS_File = False
        self.report_folder_path = ""
        self.file = ""

        self.Load_Project_Button.setEnabled(True)
        self.Upload_DS_File_Button.setStyleSheet("")
        self.Generate_Btn.setEnabled(False)

        self.comboBox_operator.clear()
        self.comboBox_Signal.clear()

        self.Console_Prjt_BT_Gener.clear()
        self.Console_Project_Management.clear()
        self.Choose_Report_Folder_Btn.setStyleSheet("background-color:#f0f0f0;;")








    def clear_report_file(self):
        try:
            with open(self.report_file, "w") as file:
                    file.write("")  # Efface le contenu du fichier en le remplaçant par une chaîne vide
            QMessageBox.information(self, "Report File Cleared", "The report file has been cleared.")
            self.Console_Prjt_BT_Gener.insertPlainText("Report File Cleared : The report file has been cleared \n")
            self.Choose_Report_Folder_Btn.setStyleSheet("background-color: #f0f0f0;")
        except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while clearing the report file: {str(e)}")









    def view_menu(self):
        self.stackedWidget.setCurrentIndex(0)
        self.Project_Manageent_Title.setHidden(True)
        self.Backtracing_generator.setHidden(False)



    def view_project_management(self):
        self.stackedWidget.setCurrentIndex(1)
        self.Project_Manageent_Title.setHidden(True)
        self.Backtracing_generator.setHidden(True)


    def view_report_generation(self):
        self.stackedWidget.setCurrentIndex(2)
        self.BT_Genr_Title.setHidden(True)
        self.Backtracing_generator.setHidden(True)

    def handle_project_folder(self):
        if self.Project_added:
            QMessageBox.warning(self, "The Project was added " "The project has already been successfully added")
            self.Load_Project_Button.setEnabled(False)
            return
        self.upload_project_folder()

    def upload_project_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier", "/path/par/défaut")
        if not self.folder_path:
            QMessageBox.warning(self, "Inappropriate Folder", " Please add the appropriate folder .")
            self.Console_Project_Management.insertPlainText("The Folder is Empty ")
            return

        if self.folder_path:
            Files = os.listdir(self.folder_path)
            has_etp = False
            has_xscade = False
            for file in Files:
                if file.endswith(".etp"):
                    has_etp = True
                elif file.endswith(".xscade"):
                        has_xscade = True
            if not has_etp:
                self.Console_Project_Management.insertPlainText("Please add the appropritate folder ")
                QMessageBox.warning(self, "Inappropriate folder", "Please add the appropriate folder.")
                self.Project_added = False
            if not has_xscade:
                self.Console_Project_Management.insertPlainText("The folder does not contain any xSCADE files")
                QMessageBox.warning(self, "Inappropriate folder", "The folder does not contain any xSCADE files")
                self.Project_added = False
            elif has_etp and has_xscade:
                #self.Console_Project_Management.insertPlainText("Project successfully added")
                QMessageBox.information(self, "Folder added", "Project Folder successfully added")
                self.Console_Project_Management.insertPlainText("Project Folder is added successfully \n")
                self.Project_added = True
                self.Load_Project_Button.setEnabled(False)

    def add_direct_settable_file(self):
            if self.DS_File:
                QMessageBox.information(self, "Project already added", "Project has already been successfully added")
                return

            self.file, _ = QFileDialog.getOpenFileName(self)
            print(self.file)
            if not self.file:
                QMessageBox.warning(self, "File not added", "Please add the file")
                self.Console_Project_Management.insertPlainText("File is empty")
                return

            if not self.file.endswith(".txt"):
                QMessageBox.warning(self, "Wrong file type", "Please add a file with the .txt extension")
                self.Console_Project_Management.insertPlainText("The extension is not appropriate")
                return

            QMessageBox.information(self, "Direct Settable File  successfully added", "Direct Settable File successfully added")
            self.Console_Project_Management.insertPlainText("Direct Settable File successfully added \n")
            self.DS_File = True

    def Adding_Project(self):
        if not self.Project_added and not self.DS_File:
            QMessageBox.warning(self, "Project Not Added",
                                "Please upload the project folder and the direct settable file before continuing.")
            return
        if not self.Project_added and self.DS_File:
            QMessageBox.warning(self, "Project Not Added ",
                                "Please upload the project folder ")
            return
        if not self.DS_File and self.Project_added:
            QMessageBox.warning(self, "Project Not Added ",
                                "Please upload the Direct Settable file ")

        self.comboBox_operator.clear()
        self.comboBox_Signal.clear()

        if not self.folder_path:
            QMessageBox.warning(self, "Folder Path Not Selected", "Please select a folder path.")
            return

        Files = os.listdir(self.folder_path)
        path = [os.path.join(self.folder_path, File) for File in Files]
        print(path)

        all_operators = []

        for p in path:
            p = os.path.normpath(p)
            if p.endswith((".etp", ".vsw", ".err", ".htm", ".ewo")):
                continue
            namespace = {
                'ns': 'http://www.esterel-technologies.com/ns/scade/6',
                'ed': 'http://www.esterel-technologies.com/ns/scade/pragmas/editor/7'
            }
            tree = ET.parse(p)
            root = tree.getroot()

            inputs = get_inputs(root, namespace)
            locals_list = get_locals(root, namespace)
            outputs = get_outputs(root, namespace)
            equations = process_equations(root, namespace)
            operator_dict = {
                'name': root.get('name'),
                'kind': root.get('kind'),
                'inputs': inputs,
                'outputs': outputs,
                'locals': locals_list,
                'Equations': equations,
            }

            all_operators.append(operator_dict)

        self.all_operators = all_operators

        QMessageBox.information(self , "Project added successfully" , "Project is added successfully ")
        self.Console_Project_Management.insertPlainText("Project is added successfully \n")
        for op in self.all_operators:
            op_name = op['name']
            self.comboBox_operator.addItem(op_name)

        self.comboBox_operator.currentTextChanged.connect(self.fill_input_output_signals)



    def fill_input_output_signals(self, operator_selected):
            operator_inputs = get_inputs_by_operator_name(self.all_operators, operator_selected)
            operators_output = get_outputs_by_operator_name(self.all_operators, operator_selected)
            self.comboBox_Signal.clear()

            for inp in operator_inputs:
                self.comboBox_Signal.addItem(inp)
            for out in operators_output:
                self.comboBox_Signal.addItem(out)

    def choose_report_folder(self):
            self.report_folder_path = QFileDialog.getExistingDirectory(self)
            if not self.report_folder_path:
                QMessageBox.warning(self, "Report Path not chosen", "Please choose the report path.")
                self.Choose_Report_Folder_Btn.setEnabled(True)
            else:
                self.Choose_Report_Folder_Btn.setStyleSheet("background-color: green;")
                self.Generate_Btn.setEnabled(True)

    def Generate_Backtracing_Report(self, report_folder_path,operator_selected ,desired_signal_input , ds_file):
        # Votre logique pour générer le rapport de backtracing ici
        print(Backtracing_Generation(self.all_operators , operator_selected,desired_signal_input,ds_file))
        self.report_file= turn_the_Bt_Report(self.all_operators, report_folder_path, operator_selected, desired_signal_input, ds_file)
        print(self.report_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_Window()
    window.show()
    app.exec_()
