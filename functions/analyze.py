import pandas as pd
import matplotlib.pyplot as plt
from functions.home import getStoreFile

fileName = getStoreFile()

def doAnalytics(self):
    dfImports = pd.read_excel(fileName, 1)
    dfExports = pd.read_excel(fileName, 2)
    importsTotal = dfImports['Total'].sum(skipna=True)
    exportsTotal = dfExports['Total'].sum(skipna=True)
    result = exportsTotal - importsTotal
    percentage = ( result /importsTotal)*100
    
    self.ui.totalAnalyticsImportsLabel.setText(str(importsTotal))
    self.ui.totalAnalyticsExportsLabel.setText(str(exportsTotal))
    self.ui.profitAnalyticsLabel.setText(str(result)+'  ('+str(percentage)+'%'+'  )')
    

def doImportsAnalytics(self):
    dfImports = pd.read_excel(fileName, 1)
    result = dfImports.groupby('Product')['Total'].sum()
    ax = result.plot(kind='bar')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.title("Imports Transactions")
    plt.xticks(rotation=30,horizontalalignment='center')
    plt.xlabel("Prodcuts")
    plt.ylabel("Rupees")
    plt.tight_layout()
    plt.show()


def doExportsAnalytics(self):
    dfExports = pd.read_excel(fileName,2)
    result = dfExports.groupby('Product')['Total'].sum()
    ax = result.plot(kind='bar')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.title("Exports Transactions")
    plt.xticks(rotation=30,horizontalalignment='center')
    plt.xlabel("Prodcuts")
    plt.ylabel("Rupees")
    plt.tight_layout()
    plt.show()
