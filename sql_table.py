import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3

class MainWindow(QDialog):
  def __init__(self):
    super(MainWindow, self).__init__()
    loadUi("table.ui", self)
    self.tableWidget.setColumnWidth(0, 300)
    self.tableWidget.setColumnWidth(1, 300)
    self.tableWidget.setColumnWidth(2, 300)
    ## Changing header
    self.tableWidget.setHorizontalHeaderLabels(["Cidade", "País", "Estado"])

    self.load_data()

  def load_data(self):
    connection = sqlite3.connect("data.sqlite")
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM worldcities LIMIT 50"

    ## Catching the number of row in data table
    # cursor.execute("SELECT COUNT(*) FROM worldcities")
    # row_count = cursor.fetchone()[0]

    ## Setting number of rows in PyQt table 
    # self.tableWidget.setRowCount(row_count)

    ## Loading the data into PyQt table 
    # for row_number, row in enumerate(cursor.execute(sqlquery)):
    #     for column_number, data in enumerate(row):
    #         item = QtWidgets.QTableWidgetItem(str(data))
    #         self.tableWidget.setItem(row_number, column_number, item)

    ## Since we are limiting the select to 50, we can hard code the row count. The comment above is being kept to clarify how this would be dynamically
    
    self.tableWidget.setRowCount(50) 

    row_count = 0

    for row in cursor.execute(sqlquery):
      self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(row[0]))
      self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(row[1]))
      self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(row[2]))

      row_count += 1


app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
  sys.exit(app.exec_())
except:
  print("Exiting")