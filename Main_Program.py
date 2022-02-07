import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from LL_impt import * #Linked List Implementation

#First Window 
class StartWindow(QDialog):
    def __init__(self):
        super(StartWindow, self).__init__()
        loadUi("start.ui", self)
        self.start_btn.clicked.connect(self.next) #once clicked, redirects user to the next window

    #the function that allows the user to move to the next window
    def next(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

#Registration Window where we get data from the user
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        self.submitbutton.clicked.connect(self.submit)
        
    def submit(self):
        #gathers data from the user
        id = self.id.text()
        name = self.name.text()
        age = self.age.text()
        college = self.college.text()
        location = self.location.text()
        vaccine_status = self.select()
        dosage = self.dosage.currentText()
        vaccine_type = self.vaccine_type.currentText()
        val = [id, name, age, college, location, vaccine_status, dosage, vaccine_type]
        implement(val) #passes data a function in the file "LL_impt.py"

        #allows the user to move to the next window
        endwindow=EndWindow()
        widget.addWidget(endwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    #checks whether the user clicked Yes or No
    def select(self):
        if self.yes_btn.isChecked():
            return "Yes"
        elif self.no_btn.isChecked():
            return "No"

#Last window 
class EndWindow(QDialog):
    def __init__(self):
        super(EndWindow, self).__init__()
        loadUi("end.ui", self)
        self.resub_btn.clicked.connect(self.prevpage)

    def prevpage(self):
        mainwindow=MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
#responsible for starting the StartWindow
app=QApplication(sys.argv)
startwindow = StartWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(startwindow)
widget.setFixedHeight(550)
widget.setFixedWidth(600)
widget.show()
app.exec_() 