from main import *
from functions.home import showData


class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_leftMenu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                maxExtended = maxExtend
            else:
                maxExtended = standard

            self.animation = QPropertyAnimation(
                self.ui.frame_leftMenu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(maxExtended)
            self.animation.start()

    def changeStackPage(self, page, index):
        self.ui.Btn_Menu_Home.setChecked(False)
        self.ui.Btn_Menu_Imports.setChecked(False)
        self.ui.Btn_Menu_Exports.setChecked(False)
        self.ui.Btn_Menu_Search.setChecked(False)
        self.ui.Btn_Menu_Products.setChecked(False)

        if(index == 1):
            self.ui.Btn_Menu_Home.setChecked(True)
            showData(self)
        if(index == 2):
            self.ui.Btn_Menu_Imports.setChecked(True)
        if(index == 3):
            self.ui.Btn_Menu_Exports.setChecked(True)
        if(index == 4):
            self.ui.Btn_Menu_Search.setChecked(True)
        if(index == 5):
            self.ui.Btn_Menu_Products.setChecked(True)

        self.ui.stack_pages.setCurrentWidget(page)