import pandas as pd
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtGui import QFont


def showData(self):
   dataFrame = pd.read_excel('store/data.xlsx', 0)
   rowLength = len(dataFrame.index)
   # Setting max row count in table
   self.ui.table_pageHome.setRowCount(rowLength+1)
   # Showing Data in table
   for row in range(0, rowLength):
       self.ui.table_pageHome.setRowHeight(row, 60)
       for col in range(0, 3):
           self.ui.table_pageHome.setFont(QFont('Arial',15))
           self.ui.table_pageHome.setItem(
               row, col, QTableWidgetItem(str(dataFrame.values[row, col+1])))
