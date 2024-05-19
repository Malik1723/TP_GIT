# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import ressources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(867, 493)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Icon_only = QWidget(self.centralwidget)
        self.Icon_only.setObjectName(u"Icon_only")
        self.Icon_only.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"QPushButton {\n"
" color : white;\n"
"\n"
"height : 30px;\n"
"border :none;\n"
"\n"
"}\n"
"QPushButton:checked {\n"
"    /* Styles lorsque le bouton est coch\u00e9 */\n"
"    background-color: white;\n"
"    color: green;\n"
"    border: 2px solid white; /* Changez la couleur et l'\u00e9paisseur de la bordure si n\u00e9cessaire */\n"
"    border-radius: 10px; /* Changez la valeur pour ajuster le radius des coins */\n"
"	 font-size: 12px;\n"
" font-weight: bold;\n"
"\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.Icon_only)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_icon = QLabel(self.Icon_only)
        self.logo_icon.setObjectName(u"logo_icon")
        self.logo_icon.setMinimumSize(QSize(50, 50))
        self.logo_icon.setMaximumSize(QSize(50, 50))
        self.logo_icon.setPixmap(QPixmap(u":/rsr/image.png"))
        self.logo_icon.setScaledContents(True)
        self.logo_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.logo_icon)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 100, -1, -1)
        self.Menu_Icon = QPushButton(self.Icon_only)
        self.Menu_Icon.setObjectName(u"Menu_Icon")
        self.Menu_Icon.setMinimumSize(QSize(20, 20))
        self.Menu_Icon.setMaximumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Menu_Icon.setFont(font)
        icon = QIcon()
        icon.addFile(u":/rsr/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_Icon.setIcon(icon)
        self.Menu_Icon.setIconSize(QSize(20, 20))
        self.Menu_Icon.setCheckable(True)
        self.Menu_Icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Menu_Icon)

        self.add_project_icon = QPushButton(self.Icon_only)
        self.add_project_icon.setObjectName(u"add_project_icon")
        self.add_project_icon.setMinimumSize(QSize(20, 20))
        self.add_project_icon.setMaximumSize(QSize(40, 40))
        self.add_project_icon.setBaseSize(QSize(20, 20))
        self.add_project_icon.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/rsr/th (5).jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_project_icon.setIcon(icon1)
        self.add_project_icon.setIconSize(QSize(20, 20))
        self.add_project_icon.setCheckable(True)
        self.add_project_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_project_icon)

        self.generate_icon = QPushButton(self.Icon_only)
        self.generate_icon.setObjectName(u"generate_icon")
        self.generate_icon.setMinimumSize(QSize(20, 20))
        self.generate_icon.setMaximumSize(QSize(40, 40))
        self.generate_icon.setBaseSize(QSize(40, 40))
        self.generate_icon.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/rsr/OIP.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.generate_icon.setIcon(icon2)
        self.generate_icon.setIconSize(QSize(20, 20))
        self.generate_icon.setCheckable(True)
        self.generate_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.generate_icon)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 132, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.log_outicon = QPushButton(self.Icon_only)
        self.log_outicon.setObjectName(u"log_outicon")
        icon3 = QIcon()
        icon3.addFile(u":/rsr/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.log_outicon.setIcon(icon3)
        self.log_outicon.setCheckable(True)
        self.log_outicon.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.log_outicon)


        self.gridLayout_6.addWidget(self.Icon_only, 0, 0, 1, 1)

        self.Icon_Name = QWidget(self.centralwidget)
        self.Icon_Name.setObjectName(u"Icon_Name")
        self.Icon_Name.setStyleSheet(u"QWidget {\n"
"\n"
"	\n"
"	color : white;\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"QPushButton {\n"
" color : white;\n"
"text-align : left;\n"
"height : 30px;\n"
"border: none;\n"
"padding-left : 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    /* Styles lorsque le bouton est coch\u00e9 */\n"
"    background-color: white;\n"
"    color: green;\n"
"    border: 2px solid white; /* Changez la couleur et l'\u00e9paisseur de la bordure si n\u00e9cessaire */\n"
"    border-radius: 10px; /* Changez la valeur pour ajuster le radius des coins */\n"
"	 font-size: 12px;\n"
" font-weight: bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Icon_Name)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 30, -1)
        self.name = QLabel(self.Icon_Name)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(50, 50))
        self.name.setMaximumSize(QSize(50, 50))
        self.name.setPixmap(QPixmap(u":/rsr/image.png"))
        self.name.setScaledContents(True)
        self.name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.name)

        self.Side_Menu_Bar = QLabel(self.Icon_Name)
        self.Side_Menu_Bar.setObjectName(u"Side_Menu_Bar")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.Side_Menu_Bar.setFont(font1)

        self.horizontalLayout_3.addWidget(self.Side_Menu_Bar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 100, -1, -1)
        self.Menu_buuton_name = QPushButton(self.Icon_Name)
        self.Menu_buuton_name.setObjectName(u"Menu_buuton_name")
        self.Menu_buuton_name.setMinimumSize(QSize(20, 20))
        self.Menu_buuton_name.setFont(font)
        self.Menu_buuton_name.setIcon(icon)
        self.Menu_buuton_name.setIconSize(QSize(20, 20))
        self.Menu_buuton_name.setCheckable(True)
        self.Menu_buuton_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Menu_buuton_name)

        self.Prj_Mng_button = QPushButton(self.Icon_Name)
        self.Prj_Mng_button.setObjectName(u"Prj_Mng_button")
        self.Prj_Mng_button.setFont(font)
        self.Prj_Mng_button.setIcon(icon1)
        self.Prj_Mng_button.setIconSize(QSize(20, 20))
        self.Prj_Mng_button.setCheckable(True)
        self.Prj_Mng_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Prj_Mng_button)

        self.Generate_Nmae_btn = QPushButton(self.Icon_Name)
        self.Generate_Nmae_btn.setObjectName(u"Generate_Nmae_btn")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.Generate_Nmae_btn.setFont(font2)
        self.Generate_Nmae_btn.setMouseTracking(True)
        self.Generate_Nmae_btn.setIcon(icon2)
        self.Generate_Nmae_btn.setIconSize(QSize(20, 20))
        self.Generate_Nmae_btn.setCheckable(True)
        self.Generate_Nmae_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Generate_Nmae_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 134, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.logout_name = QPushButton(self.Icon_Name)
        self.logout_name.setObjectName(u"logout_name")
        font3 = QFont()
        font3.setPointSize(11)
        self.logout_name.setFont(font3)
        self.logout_name.setIcon(icon3)
        self.logout_name.setCheckable(True)
        self.logout_name.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.logout_name)


        self.gridLayout_6.addWidget(self.Icon_Name, 0, 1, 1, 1)

        self.Main = QWidget(self.centralwidget)
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.verticalLayout_6 = QVBoxLayout(self.Main)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.window_Fixed = QWidget(self.Main)
        self.window_Fixed.setObjectName(u"window_Fixed")
        self.gridLayout_2 = QGridLayout(self.window_Fixed)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_bar_icon = QPushButton(self.window_Fixed)
        self.side_bar_icon.setObjectName(u"side_bar_icon")
        self.side_bar_icon.setStyleSheet(u"border: none ; ")
        icon4 = QIcon()
        icon4.addFile(u":/rsr/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_bar_icon.setIcon(icon4)
        self.side_bar_icon.setIconSize(QSize(20, 20))
        self.side_bar_icon.setCheckable(True)
        self.side_bar_icon.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.side_bar_icon)

        self.horizontalSpacer_2 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Backtracing_generator = QLabel(self.window_Fixed)
        self.Backtracing_generator.setObjectName(u"Backtracing_generator")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.Backtracing_generator.setFont(font4)
        self.Backtracing_generator.setStyleSheet(u"color: rgb(0, 170, 255);")

        self.horizontalLayout.addWidget(self.Backtracing_generator)

        self.horizontalSpacer_4 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.window_Fixed)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.stackedWidget = QStackedWidget(self.Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(245, 250, 254);\n"
"      border-radius: 10px;\n"
"\n"
"\n"
"QPushButton {\n"
"    pointer-events: auto;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Welcome_window = QWidget()
        self.Welcome_window.setObjectName(u"Welcome_window")
        self.gridLayout_9 = QGridLayout(self.Welcome_window)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_5 = QLabel(self.Welcome_window)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Welcome_window)
        self.Project_Management_Window = QWidget()
        self.Project_Management_Window.setObjectName(u"Project_Management_Window")
        self.formLayout = QFormLayout(self.Project_Management_Window)
        self.formLayout.setObjectName(u"formLayout")
        self.lay_for_prj_management_title = QHBoxLayout()
        self.lay_for_prj_management_title.setObjectName(u"lay_for_prj_management_title")
        self.horizontalSpacer_7 = QSpacerItem(158, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lay_for_prj_management_title.addItem(self.horizontalSpacer_7)

        self.Project_Manageent_Title = QLabel(self.Project_Management_Window)
        self.Project_Manageent_Title.setObjectName(u"Project_Manageent_Title")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.Project_Manageent_Title.setFont(font5)
        self.Project_Manageent_Title.setStyleSheet(u"color: rgb(46, 255, 70);")
        self.Project_Manageent_Title.setAlignment(Qt.AlignCenter)

        self.lay_for_prj_management_title.addWidget(self.Project_Manageent_Title)

        self.horizontalSpacer_8 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lay_for_prj_management_title.addItem(self.horizontalSpacer_8)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.lay_for_prj_management_title)

        self.Lay_For_upload_nd_dsQVBox = QVBoxLayout()
        self.Lay_For_upload_nd_dsQVBox.setObjectName(u"Lay_For_upload_nd_dsQVBox")
        self.Load_Project_Button = QPushButton(self.Project_Management_Window)
        self.Load_Project_Button.setObjectName(u"Load_Project_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load_Project_Button.sizePolicy().hasHeightForWidth())
        self.Load_Project_Button.setSizePolicy(sizePolicy)
        self.Load_Project_Button.setMinimumSize(QSize(300, 40))
        self.Load_Project_Button.setMaximumSize(QSize(300, 25))
        self.Load_Project_Button.setStyleSheet(u"background-color: #f0f0f0;\n"
"color: rgb(51, 10, 255);")
        self.Load_Project_Button.setCheckable(False)
        self.Load_Project_Button.setAutoExclusive(False)

        self.Lay_For_upload_nd_dsQVBox.addWidget(self.Load_Project_Button)

        self.Upload_DS_File_Button = QPushButton(self.Project_Management_Window)
        self.Upload_DS_File_Button.setObjectName(u"Upload_DS_File_Button")
        sizePolicy.setHeightForWidth(self.Upload_DS_File_Button.sizePolicy().hasHeightForWidth())
        self.Upload_DS_File_Button.setSizePolicy(sizePolicy)
        self.Upload_DS_File_Button.setMinimumSize(QSize(300, 40))
        self.Upload_DS_File_Button.setMaximumSize(QSize(300, 25))
        self.Upload_DS_File_Button.setStyleSheet(u"background-color: #f0f0f0;\n"
"color: rgb(51, 10, 255);")
        self.Upload_DS_File_Button.setCheckable(False)
        self.Upload_DS_File_Button.setAutoExclusive(False)

        self.Lay_For_upload_nd_dsQVBox.addWidget(self.Upload_DS_File_Button)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.Lay_For_upload_nd_dsQVBox)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ADD_Project_Button = QPushButton(self.Project_Management_Window)
        self.ADD_Project_Button.setObjectName(u"ADD_Project_Button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ADD_Project_Button.sizePolicy().hasHeightForWidth())
        self.ADD_Project_Button.setSizePolicy(sizePolicy1)
        self.ADD_Project_Button.setMinimumSize(QSize(50, 40))
        self.ADD_Project_Button.setMaximumSize(QSize(60, 40))
        self.ADD_Project_Button.setStyleSheet(u"background-color: rgb(32, 170, 17);\n"
"color: rgb(245, 245, 245);")
        self.ADD_Project_Button.setCheckable(False)
        self.ADD_Project_Button.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.ADD_Project_Button, 0, 0, 1, 1)

        self.Clear8project_Button = QPushButton(self.Project_Management_Window)
        self.Clear8project_Button.setObjectName(u"Clear8project_Button")
        sizePolicy1.setHeightForWidth(self.Clear8project_Button.sizePolicy().hasHeightForWidth())
        self.Clear8project_Button.setSizePolicy(sizePolicy1)
        self.Clear8project_Button.setMinimumSize(QSize(40, 40))
        self.Clear8project_Button.setMaximumSize(QSize(60, 40))
        self.Clear8project_Button.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Clear8project_Button.setCheckable(False)
        self.Clear8project_Button.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.Clear8project_Button, 0, 1, 1, 1)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.gridLayout_3)

        self.Console_Project_Management = QTextEdit(self.Project_Management_Window)
        self.Console_Project_Management.setObjectName(u"Console_Project_Management")
        self.Console_Project_Management.setStyleSheet(u"background-color: #f0f0f0;")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.Console_Project_Management)

        self.Copyright_window = QWidget(self.Project_Management_Window)
        self.Copyright_window.setObjectName(u"Copyright_window")
        self.Copyright_window.setMinimumSize(QSize(0, 50))
        self.Copyright_window.setMaximumSize(QSize(16777215, 16777215))
        self.Copyright_window.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.Grid_for_Copyright_actia = QGridLayout(self.Copyright_window)
        self.Grid_for_Copyright_actia.setObjectName(u"Grid_for_Copyright_actia")
        self.layout_for_actia_copyright_for_prj_management = QHBoxLayout()
        self.layout_for_actia_copyright_for_prj_management.setObjectName(u"layout_for_actia_copyright_for_prj_management")
        self.Actia_In_Copy_Right_Window = QLabel(self.Copyright_window)
        self.Actia_In_Copy_Right_Window.setObjectName(u"Actia_In_Copy_Right_Window")
        sizePolicy.setHeightForWidth(self.Actia_In_Copy_Right_Window.sizePolicy().hasHeightForWidth())
        self.Actia_In_Copy_Right_Window.setSizePolicy(sizePolicy)
        self.Actia_In_Copy_Right_Window.setMinimumSize(QSize(60, 25))
        self.Actia_In_Copy_Right_Window.setMaximumSize(QSize(60, 30))
        self.Actia_In_Copy_Right_Window.setBaseSize(QSize(60, 0))
        self.Actia_In_Copy_Right_Window.setPixmap(QPixmap(u":/rsr/Logo-menu-actia (1).png"))
        self.Actia_In_Copy_Right_Window.setScaledContents(True)

        self.layout_for_actia_copyright_for_prj_management.addWidget(self.Actia_In_Copy_Right_Window)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_for_actia_copyright_for_prj_management.addItem(self.horizontalSpacer_3)

        self.Copy_right2023_2024 = QPushButton(self.Copyright_window)
        self.Copy_right2023_2024.setObjectName(u"Copy_right2023_2024")
        icon5 = QIcon()
        icon5.addFile(u":/rsr/download (1).jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Copy_right2023_2024.setIcon(icon5)
        self.Copy_right2023_2024.setIconSize(QSize(20, 20))

        self.layout_for_actia_copyright_for_prj_management.addWidget(self.Copy_right2023_2024)


        self.Grid_for_Copyright_actia.addLayout(self.layout_for_actia_copyright_for_prj_management, 0, 0, 1, 1)


        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.Copyright_window)

        self.stackedWidget.addWidget(self.Project_Management_Window)
        self.BT8Geneartion_Window = QWidget()
        self.BT8Geneartion_Window.setObjectName(u"BT8Geneartion_Window")
        self.BT8Geneartion_Window.setMinimumSize(QSize(150, 40))
        self.gridLayout_5 = QGridLayout(self.BT8Geneartion_Window)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.BT_Genr_Title = QLabel(self.BT8Geneartion_Window)
        self.BT_Genr_Title.setObjectName(u"BT_Genr_Title")
        self.BT_Genr_Title.setFont(font5)
        self.BT_Genr_Title.setStyleSheet(u"color: rgb(66, 255, 135);")
        self.BT_Genr_Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.BT_Genr_Title)

        self.horizontalSpacer_6 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 7, 1, 1)
        self.Signal_Label = QLabel(self.BT8Geneartion_Window)
        self.Signal_Label.setObjectName(u"Signal_Label")
        self.Signal_Label.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.gridLayout.addWidget(self.Signal_Label, 1, 0, 1, 1)

        self.comboBox_Signal = QComboBox(self.BT8Geneartion_Window)
        self.comboBox_Signal.setObjectName(u"comboBox_Signal")
        self.comboBox_Signal.setMinimumSize(QSize(40, 30))
        self.comboBox_Signal.setStyleSheet(u"background-color: #f0f0f0;")

        self.gridLayout.addWidget(self.comboBox_Signal, 1, 1, 1, 1)

        self.comboBox_operator = QComboBox(self.BT8Geneartion_Window)
        self.comboBox_operator.setObjectName(u"comboBox_operator")
        self.comboBox_operator.setMinimumSize(QSize(40, 30))
        self.comboBox_operator.setStyleSheet(u"background-color: #f0f0f0;")

        self.gridLayout.addWidget(self.comboBox_operator, 0, 1, 1, 1)

        self.Folder_Label = QLabel(self.BT8Geneartion_Window)
        self.Folder_Label.setObjectName(u"Folder_Label")
        self.Folder_Label.setStyleSheet(u"\n"
"color: rgb(0, 85, 255);")

        self.gridLayout.addWidget(self.Folder_Label, 2, 0, 1, 1)

        self.Choose_Report_Folder_Btn = QPushButton(self.BT8Geneartion_Window)
        self.Choose_Report_Folder_Btn.setObjectName(u"Choose_Report_Folder_Btn")
        self.Choose_Report_Folder_Btn.setMinimumSize(QSize(40, 30))
        self.Choose_Report_Folder_Btn.setStyleSheet(u"background-color: #f0f0f0;")

        self.gridLayout.addWidget(self.Choose_Report_Folder_Btn, 2, 1, 1, 1)

        self.Operator_Label = QLabel(self.BT8Geneartion_Window)
        self.Operator_Label.setObjectName(u"Operator_Label")
        self.Operator_Label.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.gridLayout.addWidget(self.Operator_Label, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Generate_Btn = QPushButton(self.BT8Geneartion_Window)
        self.Generate_Btn.setObjectName(u"Generate_Btn")
        self.Generate_Btn.setMinimumSize(QSize(40, 30))
        self.Generate_Btn.setStyleSheet(u"background-color: rgb(39, 255, 15);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.Generate_Btn)

        self.Clear_Btn = QPushButton(self.BT8Geneartion_Window)
        self.Clear_Btn.setObjectName(u"Clear_Btn")
        self.Clear_Btn.setMinimumSize(QSize(40, 30))
        self.Clear_Btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"")

        self.horizontalLayout_5.addWidget(self.Clear_Btn)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)

        self.Console_Prjt_BT_Gener = QTextEdit(self.BT8Geneartion_Window)
        self.Console_Prjt_BT_Gener.setObjectName(u"Console_Prjt_BT_Gener")
        self.Console_Prjt_BT_Gener.setStyleSheet(u"background-color: #f0f0f0;")

        self.gridLayout_5.addWidget(self.Console_Prjt_BT_Gener, 4, 0, 1, 2)

        self.Actia_Copyright = QWidget(self.BT8Geneartion_Window)
        self.Actia_Copyright.setObjectName(u"Actia_Copyright")
        self.Actia_Copyright.setMinimumSize(QSize(0, 50))
        self.Actia_Copyright.setMaximumSize(QSize(16777215, 50))
        self.Actia_Copyright.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.gridLayout_7 = QGridLayout(self.Actia_Copyright)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.Actia_Copyright)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(50, 25))
        self.label_2.setMaximumSize(QSize(60, 25))
        self.label_2.setBaseSize(QSize(60, 25))
        self.label_2.setPixmap(QPixmap(u":/rsr/Logo-menu-actia (1).png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.pushButton = QPushButton(self.Actia_Copyright)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.Actia_Copyright, 5, 0, 1, 2)

        self.stackedWidget.addWidget(self.BT8Geneartion_Window)
        self.Widget_a_eliminer = QWidget()
        self.Widget_a_eliminer.setObjectName(u"Widget_a_eliminer")
        self.label_4 = QLabel(self.Widget_a_eliminer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 140, 141, 16))
        self.stackedWidget.addWidget(self.Widget_a_eliminer)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.gridLayout_6.addWidget(self.Main, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.side_bar_icon.toggled.connect(self.Icon_only.setHidden)
        self.side_bar_icon.toggled.connect(self.Icon_Name.setVisible)
        self.Menu_Icon.toggled.connect(self.Menu_buuton_name.setChecked)
        self.add_project_icon.toggled.connect(self.Prj_Mng_button.setChecked)
        self.generate_icon.toggled.connect(self.Generate_Nmae_btn.setChecked)
        self.log_outicon.toggled.connect(self.logout_name.setChecked)
        self.logout_name.toggled.connect(self.log_outicon.setChecked)
        self.Generate_Nmae_btn.toggled.connect(self.generate_icon.setChecked)
        self.Prj_Mng_button.toggled.connect(self.add_project_icon.setChecked)
        self.Menu_buuton_name.toggled.connect(self.Menu_Icon.setChecked)
        self.log_outicon.toggled.connect(MainWindow.close)
        self.logout_name.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_icon.setText("")
        self.Menu_Icon.setText("")
        self.add_project_icon.setText("")
        self.generate_icon.setText("")
        self.log_outicon.setText("")
        self.name.setText("")
        self.Side_Menu_Bar.setText(QCoreApplication.translate("MainWindow", u"Side Menu Bar", None))
        self.Menu_buuton_name.setText(QCoreApplication.translate("MainWindow", u"   Menu", None))
        self.Prj_Mng_button.setText(QCoreApplication.translate("MainWindow", u"Project Management", None))
        self.Generate_Nmae_btn.setText(QCoreApplication.translate("MainWindow", u"Backtracing Generation", None))
        self.logout_name.setText(QCoreApplication.translate("MainWindow", u"sign out", None))
        self.side_bar_icon.setText("")
        self.Backtracing_generator.setText(QCoreApplication.translate("MainWindow", u"Backtracing Generator", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Menu ", None))
        self.Project_Manageent_Title.setText(QCoreApplication.translate("MainWindow", u"Project Management", None))
        self.Load_Project_Button.setText(QCoreApplication.translate("MainWindow", u"Load Project", None))
        self.Upload_DS_File_Button.setText(QCoreApplication.translate("MainWindow", u"Upload Direct Settabel File", None))
        self.ADD_Project_Button.setText(QCoreApplication.translate("MainWindow", u"Add Project", None))
        self.Clear8project_Button.setText(QCoreApplication.translate("MainWindow", u"Clear Project", None))
        self.Actia_In_Copy_Right_Window.setText("")
        self.Copy_right2023_2024.setText(QCoreApplication.translate("MainWindow", u"2023-2024", None))
        self.BT_Genr_Title.setText(QCoreApplication.translate("MainWindow", u" Report Generation", None))
        self.Signal_Label.setText(QCoreApplication.translate("MainWindow", u"Signal", None))
        self.Folder_Label.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.Choose_Report_Folder_Btn.setText(QCoreApplication.translate("MainWindow", u"Choose Report Folder", None))
        self.Operator_Label.setText(QCoreApplication.translate("MainWindow", u"Operator", None))
        self.Generate_Btn.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.Clear_Btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"2023-2024", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Backtracing_generator", None))
    # retranslateUi

