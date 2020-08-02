from openpyxl import load_workbook


def addImports(self):
    name = self.ui.inputNameImports.text()
    product = self.ui.inputProductImports.text()
    total = self.ui.inputTotalImports.text()
    pno = self.ui.inputPnoImports.text()

    data = []
    data.append(name)
    data.append(product)
    data.append(int(total))
    data.append(int(pno))

    wb = load_workbook('store/data.xlsx')
    ws = wb.get_sheet_by_name('imports')
    rowLen = len(ws['A'])
    for col in range(1, 6):
        cell = ws.cell(row=rowLen+1, column=col)
        if(col == 1):
            cell.value = rowLen
            continue
        cell.value = data[col-2]
    wb.save('store/data.xlsx')

    clearInputsImports(self)

def clearInputsImports(self):
    self.ui.inputNameImports.setText("")
    self.ui.inputProductImports.setText("")
    self.ui.inputTotalImports.setText("")
    self.ui.inputPnoImports.setText("")
