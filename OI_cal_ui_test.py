# Python OIcalc program PyQt5 in Python

# import the required modules
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import oi_cal
# creating a window class
class Window(QMainWindow):

    # using a constructor
    def __init__(self):
        super().__init__()

        # setting the title of the window
        self.setWindowTitle("Python ")

        # setting the width of the window
        self.wd_width = 400

        # setting the height of the window
        self.wd_height = 700

        # setting geometry
        self.setGeometry(100, 100, self.wd_width, self.wd_height)

        # calling the function
        self.UiComponents()

        # displaying all the widgets
        self.show()

    # function for inserting components
    def UiComponents(self):
        # defining a new heading label
        heading = QLabel("Orbital integral Calculator", self)

        # Mentioning the geometry for the heading
        heading.setGeometry(0, 10, 400, 60)

        # setting the font
        font = QFont('Times', 15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # Mentioning font for the heading
        heading.setFont(font)

        # Giving the alignment for the heading
        heading.setAlignment(Qt.AlignCenter)

        # Mentioning the color effect for the heading
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        heading.setGraphicsEffect(color)
########################################################################################################################3
        # Defining label for lambda
        int_label = QLabel(" λ ", self)
        # Mentioning the properties for lambda
        int_label.setAlignment(Qt.AlignCenter)
        int_label.setGeometry(20, 100, 170, 40)
        int_label.setStyleSheet("QLabel"
                            "{"
                            "border : 2px solid black;"
                            "background : rgba(70, 70, 70, 35);"
                            "}")
        int_label.setFont(QFont('Times', 15))
        # Mentioning a QLineEdit object for getting the interest
        self.rate = QLineEdit(self)
        # taking in only the numbers as input
        intOnly = QIntValidator()
        self.rate.setValidator(intOnly)
        # Mentioning properties for the rate line edit
        self.rate.setGeometry(200, 100, 180, 40)
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFont(QFont('Times', 15))
############################################################################################################################################3
        # Defining a label for the number of years
        num_label = QLabel(" μ", self)
        # Adding properties for the years label
        num_label.setAlignment(Qt.AlignCenter)
        num_label.setGeometry(20, 150, 170, 40)
        num_label.setStyleSheet("QLabel"
                            "{"
                            "border : 2px solid black;"
                            "background : rgba(70, 70, 70, 35);"
                            "}")
        num_label.setFont(QFont('Times', 15))
        # Defining a new QLineEdit object to get the years
        self.years = QLineEdit(self)
        # taking input as the numbers only
        intOnly = QIntValidator()
        self.years.setValidator(intOnly)
        # Mentioning the properties for the rate line edit
        self.years.setGeometry(200, 150, 180, 40)
        self.years.setAlignment(Qt.AlignCenter)
        self.years.setFont(QFont('Times', 15))
########################################################################################################################################
        # Defining a 𝝑 label
        amt_label = QLabel("𝝑 ", self)
        # Mentioning the properties for the amount label
        amt_label.setAlignment(Qt.AlignCenter)
        amt_label.setGeometry(20, 200, 170, 40)
        amt_label.setStyleSheet("QLabel"
                            "{"
                            "border : 2px solid black;"
                            "background : rgba(70, 70, 70, 35);"
                            "}")
        amt_label.setFont(QFont('Times', 15))
        # Defining a new QLineEdit object for getting the amount
        self.amount = QLineEdit(self)
        # Taking input as numbers only
        doubleOnly = QDoubleValidator()
        self.amount.setValidator(doubleOnly)
        # Adding properties for the rate line edit
        self.amount.setGeometry(200, 200, 180, 40)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setFont(QFont('Times', 15))
###########################################################################################################################################
# Defining label for lambda
        nt_label = QLabel(" 10ξ ", self)
        # Mentioning the properties for ξ
        nt_label.setAlignment(Qt.AlignCenter)
        nt_label.setGeometry(20, 250, 170, 40)
        nt_label.setStyleSheet("QLabel"
                            "{"
                            "border : 2px solid black;"
                            "background : rgba(70, 70, 70, 35);"
                            "}")
        nt_label.setFont(QFont('Times', 15))
        # Mentioning a QLineEdit object for getting the interest
        self.rate2 = QLineEdit(self)
        # taking in only the numbers as input
        doubleOnly = QDoubleValidator()
        self.rate2.setValidator(doubleOnly)
        # Mentioning properties for the rate line edit
        self.rate2.setGeometry(200, 250, 180, 40)
        self.rate2.setAlignment(Qt.AlignCenter)
        self.rate2.setFont(QFont('Times', 15))       
##########################################################################################################################################      
        # Defining a new push button
        #clc = QLabel("Compute I<sub>λμ</sub>(𝝑,ξ)", self)
        calc = QPushButton("Calculate ",self)
        # Mentioning the geometry  for the push button
        calc.setGeometry(125, 325, 175, 60)
        # Inserting action to the calc button
        calc.clicked.connect(self.calc_action)
        # Defining a new label to display monthly payment
        self.mp_payment = QLabel(self)
        # Adding properties to the m payment label
        self.mp_payment.setAlignment(Qt.AlignCenter)
        #self.mp_payment.setGeometry(50, 350, 300, 60)
        #self.mp_payment.setStyleSheet("QLabel"
                                    #"{"
                                    #"border : 3px solid black;"
                                    #"background : white;"
                                    #"}")
        #self.mp_payment.setFont(QFont('Arial', 11))
###########################################################################################################################################
        # Defining a new label to display monthly payment
        self.yp_payment = QLabel(self)
        # Adding some properties to the y payment label
        self.yp_payment.setAlignment(Qt.AlignCenter)
        self.yp_payment.setGeometry(50, 400, 300, 60)
        self.yp_payment.setStyleSheet("QLabel"
                                    "{"
                                    "border : 3px solid black;"
                                    "background : white;"
                                    "}")
        self.yp_payment.setFont(QFont('Arial', 11))
########################################################################################################################################3
    # function for calculating the monthly
    # and the annual payments
    def calc_action(self):
        # displaying the annual interest rate
        annualIntrstRate = self.rate.text()
        # condition for when there is no number entered
        if len(annualIntrstRate) == 0 or annualIntrstRate == '0':
            return
        # Showing the number of years
        numOfYrs = self.years.text()
        # condition for when there is no number entered
        if len(numOfYrs) == 0 or numOfYrs == '0':
            return
        # taking the loan amount
        loanAmt = self.amount.text()
        # if there is no number is entered
        if len(loanAmt) == 0 or loanAmt == '0':
            return
        # Showing the number of years
        xi = self.rate2.text()
        # condition for when there is no number entered
        if len(xi) == 0 or xi == '0':
            return
        # converting the text to integers
        annualIntrstRate = int(annualIntrstRate)
        numOfYrs = int(numOfYrs)
        loanAmt = float(loanAmt)
        xi = float(xi)
        # getting the monthly rate for interest
        mnthlyIntrstRate = annualIntrstRate / 1200
        # Analysing the monthly payemnt
        mnthlyPaymnt = loanAmt * mnthlyIntrstRate / (1 - 1 / (1 + mnthlyIntrstRate) ** (numOfYrs * 12))
        # Defining the formatting
        mnthlyPaymnt = "{:.2f}".format(mnthlyPaymnt)
        # setting text to the label
        self.mp_payment.setText("Monthly Payment : " + str(mnthlyPaymnt))
        # getting the total payment
        #ttlPayment = float(mnthlyPaymnt) * 12 * numOfYrs
        ttlPayment = oi_cal.get_oi(annualIntrstRate,numOfYrs,0.0175*loanAmt,0.1*xi)
        ttlPayment = "{:.4f}".format(ttlPayment)
        # Mentioning the text for the label
        self.yp_payment.setText(str(ttlPayment))
##################################################################################################################################
# creating the pyqt5 application
base = QApplication(sys.argv)
# creating an instance of the Window
window = Window()
# starting the application
sys.exit(base.exec())
