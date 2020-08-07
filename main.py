import sys
import platform
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
from functions.home import showData
from functions.imports import addImports,clearInputsImports
from functions.exports import addExports,clearInputsExports
from functions.search import search,clearInputs,deleteRow
from functions.products import addProduct,deleteProduct,updateProduct,resetInputs

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        self.ui.Btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        self.ui.Btn_Menu_Home.clicked.connect(
            lambda: UIFunctions.changeStackPage(self, self.ui.page_Home, 1))
        self.ui.Btn_Menu_Imports.clicked.connect(
            lambda: UIFunctions.changeStackPage(self, self.ui.page_Imports, 2))
        self.ui.Btn_Menu_Exports.clicked.connect(
            lambda: UIFunctions.changeStackPage(self, self.ui.page_Exports, 3))
        self.ui.Btn_Menu_Search.clicked.connect(
            lambda: UIFunctions.changeStackPage(self, self.ui.page_Search, 4))
        self.ui.Btn_Menu_Products.clicked.connect(
            lambda: UIFunctions.changeStackPage(self, self.ui.page_Products, 5))

        ## Home Function
        showData(self)
        ## Import Functions
        self.ui.btnImports.clicked.connect(lambda: addImports(self))
        self.ui.btnResetImports.clicked.connect(lambda:clearInputsImports(self))
        ## Export Functions
        self.ui.btnExports.clicked.connect(lambda:addExports(self))
        self.ui.btnResetExports.clicked.connect(lambda:clearInputsExports(self))
        ## Search Functions
        self.ui.btnSearch.clicked.connect(lambda:search(self))
        self.ui.btnRessetSearch.clicked.connect(lambda:clearInputs(self))
        self.ui.btnDelSearch.clicked.connect(lambda:deleteRow(self))
        ## Products Functions
        self.ui.btnAddProducts.clicked.connect(lambda:addProduct(self))
        self.ui.btnDelProducts.clicked.connect(lambda:deleteProduct(self))
        self.ui.btnResetProducts.clicked.connect(lambda:resetInputs(self))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
