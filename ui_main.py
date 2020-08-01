# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledqtDzwl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QSize(750, 500))
        MainWindow.setMaximumSize(QSize(1366, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBar = QFrame(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setMaximumSize(QSize(16777215, 50))
        self.TopBar.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.TopBar.setFrameShape(QFrame.NoFrame)
        self.TopBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TopBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggleBar = QFrame(self.TopBar)
        self.frame_toggleBar.setObjectName(u"frame_toggleBar")
        self.frame_toggleBar.setMaximumSize(QSize(70, 50))
        self.frame_toggleBar.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border:0px solid;")
        self.frame_toggleBar.setFrameShape(QFrame.NoFrame)
        self.frame_toggleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toggleBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggleBar)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"border:0px solid;\n"
"outline:0;")

        self.horizontalLayout_3.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggleBar)

        self.frame_top = QFrame(self.TopBar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_top)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_top)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Droid Sans Mono")
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.TopBar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_leftMenu = QFrame(self.Content)
        self.frame_leftMenu.setObjectName(u"frame_leftMenu")
        self.frame_leftMenu.setMinimumSize(QSize(70, 0))
        self.frame_leftMenu.setMaximumSize(QSize(70, 16777215))
        self.frame_leftMenu.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.frame_leftMenu.setFrameShape(QFrame.NoFrame)
        self.frame_leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_leftMenu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_Menu_Home = QPushButton(self.frame_menus)
        self.Btn_Menu_Home.setObjectName(u"Btn_Menu_Home")
        self.Btn_Menu_Home.setMinimumSize(QSize(0, 50))
        self.Btn_Menu_Home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	border:0px solid;\n"
"	outline:0;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(0, 170, 127);\n"
"	border:0px solid;\n"
"	outline:0;\n"
"}")
        self.Btn_Menu_Home.setCheckable(True)
        self.Btn_Menu_Home.setChecked(False)

        self.verticalLayout_3.addWidget(self.Btn_Menu_Home)

        self.Btn_Menu_Imports = QPushButton(self.frame_menus)
        self.Btn_Menu_Imports.setObjectName(u"Btn_Menu_Imports")
        self.Btn_Menu_Imports.setMinimumSize(QSize(0, 50))
        self.Btn_Menu_Imports.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	border:0px solid;\n"
"	outline:0;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Menu_Imports.setCheckable(True)

        self.verticalLayout_3.addWidget(self.Btn_Menu_Imports)

        self.Btn_Menu_Exports = QPushButton(self.frame_menus)
        self.Btn_Menu_Exports.setObjectName(u"Btn_Menu_Exports")
        self.Btn_Menu_Exports.setMinimumSize(QSize(0, 50))
        self.Btn_Menu_Exports.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	border:0px solid;\n"
"	outline:0;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Menu_Exports.setCheckable(True)

        self.verticalLayout_3.addWidget(self.Btn_Menu_Exports)

        self.Btn_Menu_Search = QPushButton(self.frame_menus)
        self.Btn_Menu_Search.setObjectName(u"Btn_Menu_Search")
        self.Btn_Menu_Search.setMinimumSize(QSize(0, 50))
        self.Btn_Menu_Search.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	border:0px solid;\n"
"	outline:0;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Menu_Search.setCheckable(True)

        self.verticalLayout_3.addWidget(self.Btn_Menu_Search)

        self.Btn_Menu_Products = QPushButton(self.frame_menus)
        self.Btn_Menu_Products.setObjectName(u"Btn_Menu_Products")
        self.Btn_Menu_Products.setMinimumSize(QSize(0, 50))
        self.Btn_Menu_Products.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	border:0px solid;\n"
"	outline:0;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Menu_Products.setCheckable(True)

        self.verticalLayout_3.addWidget(self.Btn_Menu_Products)


        self.verticalLayout_2.addWidget(self.frame_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_leftMenu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setAutoFillBackground(True)
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stack_pages = QStackedWidget(self.frame_pages)
        self.stack_pages.setObjectName(u"stack_pages")
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.horizontalLayout_5 = QHBoxLayout(self.page_Home)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_pageHome = QFrame(self.page_Home)
        self.frame_pageHome.setObjectName(u"frame_pageHome")
        self.frame_pageHome.setFrameShape(QFrame.StyledPanel)
        self.frame_pageHome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_pageHome)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.table_pageHome = QTableWidget(self.frame_pageHome)
        if (self.table_pageHome.columnCount() < 3):
            self.table_pageHome.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(15)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.table_pageHome.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_pageHome.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_pageHome.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_pageHome.setObjectName(u"table_pageHome")
        self.table_pageHome.setFrameShape(QFrame.StyledPanel)
        self.table_pageHome.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_pageHome.setShowGrid(False)
        self.table_pageHome.horizontalHeader().setMinimumSectionSize(100)
        self.table_pageHome.horizontalHeader().setDefaultSectionSize(220)
        self.table_pageHome.horizontalHeader().setStretchLastSection(True)
        self.table_pageHome.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.table_pageHome)


        self.horizontalLayout_5.addWidget(self.frame_pageHome)

        self.stack_pages.addWidget(self.page_Home)
        self.page_Imports = QWidget()
        self.page_Imports.setObjectName(u"page_Imports")
        self.verticalLayout_8 = QVBoxLayout(self.page_Imports)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_pageImports = QFrame(self.page_Imports)
        self.frame_pageImports.setObjectName(u"frame_pageImports")
        self.frame_pageImports.setFrameShape(QFrame.StyledPanel)
        self.frame_pageImports.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_pageImports)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelProductImports = QLabel(self.frame_pageImports)
        self.labelProductImports.setObjectName(u"labelProductImports")

        self.gridLayout.addWidget(self.labelProductImports, 1, 0, 1, 1)

        self.inputProductImports = QLineEdit(self.frame_pageImports)
        self.inputProductImports.setObjectName(u"inputProductImports")

        self.gridLayout.addWidget(self.inputProductImports, 1, 2, 1, 1)

        self.labelNameImports = QLabel(self.frame_pageImports)
        self.labelNameImports.setObjectName(u"labelNameImports")

        self.gridLayout.addWidget(self.labelNameImports, 0, 0, 1, 1)

        self.labelPnoImports = QLabel(self.frame_pageImports)
        self.labelPnoImports.setObjectName(u"labelPnoImports")

        self.gridLayout.addWidget(self.labelPnoImports, 3, 0, 1, 1)

        self.inputTotalImports = QLineEdit(self.frame_pageImports)
        self.inputTotalImports.setObjectName(u"inputTotalImports")

        self.gridLayout.addWidget(self.inputTotalImports, 2, 2, 1, 1)

        self.inputNameImports = QLineEdit(self.frame_pageImports)
        self.inputNameImports.setObjectName(u"inputNameImports")

        self.gridLayout.addWidget(self.inputNameImports, 0, 2, 1, 1)

        self.inputPnoImports = QLineEdit(self.frame_pageImports)
        self.inputPnoImports.setObjectName(u"inputPnoImports")

        self.gridLayout.addWidget(self.inputPnoImports, 3, 2, 1, 1)

        self.labelTotalImports = QLabel(self.frame_pageImports)
        self.labelTotalImports.setObjectName(u"labelTotalImports")

        self.gridLayout.addWidget(self.labelTotalImports, 2, 0, 1, 1)

        self.btnResetImports = QPushButton(self.frame_pageImports)
        self.btnResetImports.setObjectName(u"btnResetImports")

        self.gridLayout.addWidget(self.btnResetImports, 4, 1, 1, 1)

        self.btnImports = QPushButton(self.frame_pageImports)
        self.btnImports.setObjectName(u"btnImports")

        self.gridLayout.addWidget(self.btnImports, 4, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_pageImports)

        self.stack_pages.addWidget(self.page_Imports)
        self.page_Exports = QWidget()
        self.page_Exports.setObjectName(u"page_Exports")
        self.verticalLayout_6 = QVBoxLayout(self.page_Exports)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_pageExports = QFrame(self.page_Exports)
        self.frame_pageExports.setObjectName(u"frame_pageExports")
        self.frame_pageExports.setFrameShape(QFrame.StyledPanel)
        self.frame_pageExports.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_pageExports)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelNameExports = QLabel(self.frame_pageExports)
        self.labelNameExports.setObjectName(u"labelNameExports")

        self.gridLayout_2.addWidget(self.labelNameExports, 0, 0, 1, 1)

        self.inputNameExports = QLineEdit(self.frame_pageExports)
        self.inputNameExports.setObjectName(u"inputNameExports")

        self.gridLayout_2.addWidget(self.inputNameExports, 0, 2, 1, 1)

        self.labelProductExports = QLabel(self.frame_pageExports)
        self.labelProductExports.setObjectName(u"labelProductExports")

        self.gridLayout_2.addWidget(self.labelProductExports, 1, 0, 1, 1)

        self.inputProductExports = QLineEdit(self.frame_pageExports)
        self.inputProductExports.setObjectName(u"inputProductExports")

        self.gridLayout_2.addWidget(self.inputProductExports, 1, 2, 1, 1)

        self.labelTotalExports = QLabel(self.frame_pageExports)
        self.labelTotalExports.setObjectName(u"labelTotalExports")

        self.gridLayout_2.addWidget(self.labelTotalExports, 2, 0, 1, 1)

        self.inputTotalExports = QLineEdit(self.frame_pageExports)
        self.inputTotalExports.setObjectName(u"inputTotalExports")

        self.gridLayout_2.addWidget(self.inputTotalExports, 2, 2, 1, 1)

        self.labelPnoExports = QLabel(self.frame_pageExports)
        self.labelPnoExports.setObjectName(u"labelPnoExports")

        self.gridLayout_2.addWidget(self.labelPnoExports, 3, 0, 1, 1)

        self.inputPnoExports = QLineEdit(self.frame_pageExports)
        self.inputPnoExports.setObjectName(u"inputPnoExports")

        self.gridLayout_2.addWidget(self.inputPnoExports, 3, 2, 1, 1)

        self.btnResetExports = QPushButton(self.frame_pageExports)
        self.btnResetExports.setObjectName(u"btnResetExports")

        self.gridLayout_2.addWidget(self.btnResetExports, 4, 1, 1, 1)

        self.btnExports = QPushButton(self.frame_pageExports)
        self.btnExports.setObjectName(u"btnExports")

        self.gridLayout_2.addWidget(self.btnExports, 4, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_pageExports)

        self.stack_pages.addWidget(self.page_Exports)
        self.page_Search = QWidget()
        self.page_Search.setObjectName(u"page_Search")
        self.verticalLayout_9 = QVBoxLayout(self.page_Search)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_pageSearch = QFrame(self.page_Search)
        self.frame_pageSearch.setObjectName(u"frame_pageSearch")
        self.frame_pageSearch.setFrameShape(QFrame.StyledPanel)
        self.frame_pageSearch.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_pageSearch)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.inputDate = QDateEdit(self.frame_pageSearch)
        self.inputDate.setObjectName(u"inputDate")

        self.gridLayout_3.addWidget(self.inputDate, 1, 0, 1, 1)

        self.inputProductSearch = QLineEdit(self.frame_pageSearch)
        self.inputProductSearch.setObjectName(u"inputProductSearch")

        self.gridLayout_3.addWidget(self.inputProductSearch, 1, 1, 1, 2)

        self.tabelResultSearch = QTableView(self.frame_pageSearch)
        self.tabelResultSearch.setObjectName(u"tabelResultSearch")

        self.gridLayout_3.addWidget(self.tabelResultSearch, 4, 0, 1, 5)

        self.labelDateSearch = QLabel(self.frame_pageSearch)
        self.labelDateSearch.setObjectName(u"labelDateSearch")

        self.gridLayout_3.addWidget(self.labelDateSearch, 0, 0, 1, 1)

        self.labelNameSearch = QLabel(self.frame_pageSearch)
        self.labelNameSearch.setObjectName(u"labelNameSearch")

        self.gridLayout_3.addWidget(self.labelNameSearch, 0, 4, 1, 1)

        self.inputNameSearch = QLineEdit(self.frame_pageSearch)
        self.inputNameSearch.setObjectName(u"inputNameSearch")

        self.gridLayout_3.addWidget(self.inputNameSearch, 1, 4, 1, 1)

        self.btnSearch = QPushButton(self.frame_pageSearch)
        self.btnSearch.setObjectName(u"btnSearch")

        self.gridLayout_3.addWidget(self.btnSearch, 3, 4, 1, 1)

        self.btnRessetSearch = QPushButton(self.frame_pageSearch)
        self.btnRessetSearch.setObjectName(u"btnRessetSearch")

        self.gridLayout_3.addWidget(self.btnRessetSearch, 3, 2, 1, 1)

        self.btnDelSearch = QPushButton(self.frame_pageSearch)
        self.btnDelSearch.setObjectName(u"btnDelSearch")

        self.gridLayout_3.addWidget(self.btnDelSearch, 3, 1, 1, 1)

        self.labelProductSearch = QLabel(self.frame_pageSearch)
        self.labelProductSearch.setObjectName(u"labelProductSearch")

        self.gridLayout_3.addWidget(self.labelProductSearch, 0, 1, 1, 2)


        self.verticalLayout_9.addWidget(self.frame_pageSearch)

        self.stack_pages.addWidget(self.page_Search)
        self.page_Products = QWidget()
        self.page_Products.setObjectName(u"page_Products")
        self.verticalLayout_7 = QVBoxLayout(self.page_Products)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_pageProducts = QFrame(self.page_Products)
        self.frame_pageProducts.setObjectName(u"frame_pageProducts")
        self.frame_pageProducts.setFrameShape(QFrame.StyledPanel)
        self.frame_pageProducts.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_pageProducts)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelProductProducts = QLabel(self.frame_pageProducts)
        self.labelProductProducts.setObjectName(u"labelProductProducts")

        self.gridLayout_4.addWidget(self.labelProductProducts, 0, 0, 1, 1)

        self.inputProductProducts = QLineEdit(self.frame_pageProducts)
        self.inputProductProducts.setObjectName(u"inputProductProducts")

        self.gridLayout_4.addWidget(self.inputProductProducts, 0, 1, 1, 1)

        self.labelPriceProducts = QLabel(self.frame_pageProducts)
        self.labelPriceProducts.setObjectName(u"labelPriceProducts")

        self.gridLayout_4.addWidget(self.labelPriceProducts, 0, 2, 1, 1)

        self.inputPriceProducts = QLineEdit(self.frame_pageProducts)
        self.inputPriceProducts.setObjectName(u"inputPriceProducts")

        self.gridLayout_4.addWidget(self.inputPriceProducts, 0, 3, 1, 1)

        self.labelAvlProducts = QLabel(self.frame_pageProducts)
        self.labelAvlProducts.setObjectName(u"labelAvlProducts")

        self.gridLayout_4.addWidget(self.labelAvlProducts, 0, 4, 1, 1)

        self.inputAvlProducts = QLineEdit(self.frame_pageProducts)
        self.inputAvlProducts.setObjectName(u"inputAvlProducts")

        self.gridLayout_4.addWidget(self.inputAvlProducts, 0, 5, 1, 1)

        self.btnDelProducts = QPushButton(self.frame_pageProducts)
        self.btnDelProducts.setObjectName(u"btnDelProducts")

        self.gridLayout_4.addWidget(self.btnDelProducts, 1, 1, 1, 1)

        self.btnResetProducts = QPushButton(self.frame_pageProducts)
        self.btnResetProducts.setObjectName(u"btnResetProducts")

        self.gridLayout_4.addWidget(self.btnResetProducts, 1, 3, 1, 1)

        self.btnAddProducts = QPushButton(self.frame_pageProducts)
        self.btnAddProducts.setObjectName(u"btnAddProducts")

        self.gridLayout_4.addWidget(self.btnAddProducts, 1, 4, 1, 2)

        self.tableProducts = QTableWidget(self.frame_pageProducts)
        if (self.tableProducts.columnCount() < 3):
            self.tableProducts.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableProducts.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableProducts.setObjectName(u"tableProducts")
        self.tableProducts.setFrameShape(QFrame.StyledPanel)
        self.tableProducts.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableProducts.setShowGrid(False)
        self.tableProducts.horizontalHeader().setMinimumSectionSize(100)
        self.tableProducts.horizontalHeader().setDefaultSectionSize(220)
        self.tableProducts.horizontalHeader().setStretchLastSection(True)
        self.tableProducts.verticalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableProducts, 2, 0, 1, 6)


        self.verticalLayout_7.addWidget(self.frame_pageProducts)

        self.stack_pages.addWidget(self.page_Products)

        self.verticalLayout_4.addWidget(self.stack_pages)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stack_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Shree", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"| | |", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shree Poultry Farm", None))
        self.Btn_Menu_Home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.Btn_Menu_Imports.setText(QCoreApplication.translate("MainWindow", u"IMPORTS", None))
        self.Btn_Menu_Exports.setText(QCoreApplication.translate("MainWindow", u"EXPORTS", None))
        self.Btn_Menu_Search.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.Btn_Menu_Products.setText(QCoreApplication.translate("MainWindow", u"PRODUCTS", None))
        ___qtablewidgetitem = self.table_pageHome.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product", None));
        ___qtablewidgetitem1 = self.table_pageHome.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        ___qtablewidgetitem2 = self.table_pageHome.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Available", None));
        self.labelProductImports.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.labelNameImports.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.labelPnoImports.setText(QCoreApplication.translate("MainWindow", u"Phone No", None))
        self.labelTotalImports.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.btnResetImports.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnImports.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.labelNameExports.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.labelProductExports.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.labelTotalExports.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.labelPnoExports.setText(QCoreApplication.translate("MainWindow", u"Phone No", None))
        self.btnResetExports.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnExports.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.labelDateSearch.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.labelNameSearch.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btnRessetSearch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnDelSearch.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.labelProductSearch.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.labelProductProducts.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.labelPriceProducts.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.labelAvlProducts.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.btnDelProducts.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btnResetProducts.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnAddProducts.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        ___qtablewidgetitem3 = self.tableProducts.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Product", None));
        ___qtablewidgetitem4 = self.tableProducts.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        ___qtablewidgetitem5 = self.tableProducts.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Available", None));
    # retranslateUi

