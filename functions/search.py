import pandas as pd
from openpyxl import load_workbook
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import QDate
from PySide2.QtGui import QFont


def setDate(self):
    date = QDate.currentDate()
    self.ui.inputDate.setDate(date)


def clearInputs(self):
    self.ui.inputProductSearch.setText("")
    self.ui.inputNameSearch.setText("")


def search(self):
    productName = self.ui.inputProductSearch.text()
    userName = self.ui.inputNameSearch.text()
    option = self.ui.optionsSearch.currentText()

    if(option == "Imports"):
        df = pd.read_excel('store/data.xlsx', 1)
    if(option == "Exports"):
        df = pd.read_excel('store/data.xlsx', 2)
    search = df[(df['Product'].str.contains(productName, case=False))
                & (df['Name'].str.contains(userName, case=False))]

    rowLength = len(search.index)
    self.ui.tableResultSearch.setRowCount(rowLength)
    self.ui.tableResultSearch.setColumnCount(5)
    # Column Widths
    self.ui.tableResultSearch.setColumnWidth(0, 10)
    self.ui.tableResultSearch.setColumnWidth(1, 180)
    self.ui.tableResultSearch.setColumnWidth(2, 150)
    self.ui.tableResultSearch.setColumnWidth(3, 130)
    self.ui.tableResultSearch.setColumnWidth(4, 150)

    self.ui.tableResultSearch.verticalHeader().setVisible(False)
    self.ui.tableResultSearch.setHorizontalHeaderLabels(search.head())
    for row in range(0, rowLength):
        self.ui.tableResultSearch.setRowHeight(row, 25)
        for col in range(0, 5):
            self.ui.tableResultSearch.setFont(QFont('Arial', 14))
            self.ui.tableResultSearch.setItem(
                row, col, QTableWidgetItem(str(search.values[row, col])))


def deleteRow(self):
    deleteIndex = self.ui.tableResultSearch.currentRow()
    option = self.ui.optionsSearch.currentText()
    wb = load_workbook('store/data.xlsx')
    ws = wb.get_sheet_by_name(str(option).lower())
    ws.delete_rows(deleteIndex+2)
    wb.save('store/data.xlsx')
    search(self)
