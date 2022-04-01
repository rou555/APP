import sys
import re
from PyQt5.uic import loadUi ,loadUiType
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import os
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import cv2
from datetime import date
from datetime import datetime
import numpy as np
import pandas as pd
from PIL import Image

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_companyinfo import Ui_Form

# IMPORT FUNCTIONS
from ui_functions import *



class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("./GUI/welcome.ui",self) # load the GUI file
        self.login_btn.clicked.connect(self.gotologin) # event handel for button login 
        self.setWindowTitle("Welcome Screen")
        #self.setGeometry(0,0,1487,973)
       # self.setFixedWidth(371)
        #self.setFixedHeight(661)
        #self.setGeometry(50,50,371,661) #set fixed size for window 
    
    def gotologin(self):

        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1) # showing the next widget (screen) that in the above line (loginScreen)
       # widget.setFixedWidth(548)
      #  widget.setFixedHeight(755)
        #widget.setGeometry(50,50,1538,926)
        widget.setWindowTitle("Login Screen")



######################################################## StartUpWondow #############################################

######################################################## LoginScreen #############################################
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("./GUI/login.ui",self)
        #self.setFixedWidth(548)
        #self.setFixedHeight(755)
        #self.setGeometry(50,50,548,755)

        #self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login.clicked.connect(self.loginfunction)
        #self.CancelButton.clicked.connect(self.goBack)

        self.setWindowTitle("Login")

        #self.mainwin=MainWin()


    def loginfunction(self):

        self.user = self.user_line.text()

        self.password = self.pass_line.text()


        if len(self.user)==0 or len(self.password)==0:
            self.error.setText("Please input all fields.")

        else:
            
            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()

            query = 'SELECT User_Password FROM Users WHERE User_Name =\''+self.user+"\'"
            cur.execute(query)
            query_result  = cur.fetchone()
            #print(result_pass)
           # result_pass = query_result[0]

            if query_result is not None:
                if query_result[0] == self.password:
                    QMessageBox.about(self, "alert", "Successfully logged in \n"+self.user)
                    print("Successfully logged in.")
                    self.gotomaintest()
                else:
                    self.error.setText("Invalid username or password")
            else:        
                self.error.setText("Invalid username or password")
                


    def gotomaintest(self):
        mainwint=MainWin()
        widget.addWidget(mainwint)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)
        widget.setGeometry(50,50,861,605)
        widget.setWindowTitle("Main Screen")

######################################################## EndCompanyInformationWindow #############################################   
                 
######################################################## MainWindow #############################################

class MainWin(QDialog):
    def __init__(self):    
        super(MainWin, self).__init__()
        loadUi("./GUI/MainMenue.ui",self)
        self.pushButton.clicked.connect(self.gotoemp)
        self.pushButton_2.clicked.connect(self.gotoCompanyInfo)
        self.AddNewAdminButton.clicked.connect(self.gotoAddUser)
        #self.TrainButton.clicked.connect(Trainmodle)
        #self.TakeAtt.clicked.connect(Attendace)
        #self.logoutButton.clicked.connect(self.gotoWelcome)
        #self.Exit.clicked.connect(self.Exitsys)


    def gotoAddUser(self):  
        createProfile=AddNewUser()
        widget.addWidget(createProfile)
        widget.setWindowTitle("Add User")

    def gotoemp(self):
        EmpScreen = EmployeeMenu()
        widget.addWidget(EmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
       
  
   

    def gotoCompanyInfo(self):
        CompInfo = CompanyInfo()
        widget.addWidget(CompInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
        widget.setWindowTitle("Company Information ")
    
   # def gotoWelcome(self):
      #  back2Welcome = WelcomeScreen()
       # widget.addWidget(back2Welcome)
       # widget.setCurrentIndex(widget.currentIndex()+1)
        #widget.setFixedWidth(371)
        #widget.setFixedHeight(661)
        #widget.setGeometry(50,50,371,661)
      #  widget.setWindowTitle("Welcome Screen")

    def Exitsys(self):
        exit(0)

############################################################################################################

class EmployeeMenu(QDialog):
    def __init__(self):    
        super(EmployeeMenu, self).__init__()
        loadUi("./GUI/employee.ui",self)
        self.add_btn.clicked.connect(self.gotonewemployee)
        self.edit_btn.clicked.connect(self.gotoeditemployee)
        self.check_btn.clicked.connect(self.gotoCheck)
        

    def gotonewemployee(self):
        NewEmpScreen = NewEmployee()
        widget.addWidget(NewEmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("New Employee")
    
    
    #def gotoeditemployee(self):
        #EditEmployeescreen = EditEmployee()
        #widget.addWidget(EditEmployeescreen)
        #widget.setCurrentIndex(widget.currentIndex() + 1)
        #widget.setWindowTitle("Edit Employee")
    


##########################################################################

class NewEmployee(QDialog):
    def __init__(self):
        super(NewEmployee, self).__init__()
        loadUi("./GUI/newemployee.ui",self)
        self.next_btn.clicked.connect(self.gotonewemployee2)
        self.back_btn.clicked.connect(self.gotoempmenu)
        self.search_btn.clicked.connect(self.gotoeditemployee)
        self.handel_Lines()
        self.firstname1=self.first_line.text()
        self.middlename1=self.middle_line.text()
        self.lastname1=self.last_line.text()
        self.gender=self.radioButton.isChecked()
        self.address=self.address_line.text()

        self.DOB=self.dateEdit.date()
        self.var_name = self.DOB.toPyDate()


    def gotonewemployee2(self):
        NewEmpScreen2 = NewEmployee2()
        widget.addWidget(NewEmpScreen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("New Employee2")

    def gotoempmenu(self):
        EmpScreen = EmployeeMenu()
        widget.addWidget(EmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle(" Employee Menu")
    
    
    def handel_Lines(self):
        self.first_line.clear()
        self.middle_line.clear()
        self.last_line.clear()
        self.address_line.clear()
        self.phone_line.clear()
        self.email_line.clear()

       

        
      
    def DB(self):
            conn = sqlite3.connect("./DataBaseTabletest.db")
            conn.text_factory=str
            cursor = conn.cursor()
            
            self.firstname1=self.first_line.text()
            self.middlename1=self.middle_line.text()
            self.lastname1=self.last_line.text()
            self.gender=self.radioButton.isChecked()
            self.address=self.address_line.text()
            self.DOB=self.dateEdit.date()
            self.var_name = self.DOB.toPyDate()

    def gotoeditemployee(self):
        pass





###############################################################################


class NewEmployee2(QDialog):
    def __init__(self):
        super(NewEmployee2, self).__init__()
        loadUi("./GUI/newemployee2.ui",self)
        self.back_btn.clicked.connect(self.gotonewemployee)
        self.save_btn.clicked.connect(self.DB)
        self.cancel_btn.clicked.connect(self.gotonewemployee2)
        self.addphoto_btn.clicked.connect(self.gotonewemployee2)
        self.handel_Lines()

    def gotonewemployee(self):
        NewEmpScreen = NewEmployee()
        widget.addWidget(NewEmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.getCompayinfo()  

    def getCompayinfo(self):

        conn = sqlite3.connect("./DataBaseTabletest.db")
        conn.text_factory=str
        cursor = conn.cursor()
            
        cursor.execute('SELECT Dept_Name FROM DepartmentsTable;')
        dept_names=cursor.fetchall()
        dept_names1=[r[0] for r in dept_names]

        cursor.execute('SELECT JobDesc FROM JobTittle;')
        JobTitles=cursor.fetchall()
        JobTitles1=[r[0] for r in JobTitles]

        cursor.execute('SELECT AttendanceDesc FROM Attendance_Schemes_Table;')
        attendanceSchem=cursor.fetchall()
        attendanceSchem1=[r[0] for r in attendanceSchem]

        cursor.execute('SELECT Category FROM AccessScheme;')
        accesSchem=cursor.fetchall()
        accesSchem1=[r[0] for r in accesSchem]


        deptlen=len(dept_names1)
        joblen=len(JobTitles1)
        attendanceSchLen=len(attendanceSchem1)
        accesSchemLen=len(accesSchem1)
        
        if dept_names1 == []:
            print("you cant add New Employee you must First ADD Company Dept's")
            self.E2.setText("Go To Company Information To Add Dept")
            self.save_button.setEnabled(False)   
        else:
            count=0
            for i in range (deptlen):
                self.dep_drop.addItem(dept_names1[count])
                count+=1


        if  JobTitles == []:
            print("you cant add New Employee you must First ADD Company Job Titles's")
            self.E2.setText("Go To Company Information To Add Job Tiltle")
            self.save_button.setEnabled(False)     
        else:
            count=0
            for i in range (joblen):
                self.job_drop.addItem(JobTitles1[count])
                count+=1      

        if attendanceSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company attendance Schem")
            self.E2.setText("Go To Company Information To Add attendance Schem") 
            self.save_button.setEnabled(False)     
        else:
            count=0 
            for i in range (attendanceSchLen):
                self.attend_drop.addItem(attendanceSchem1[count])
                count+=1    

        if accesSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company Access Schem")  
            self.E2.setText("Go To Company Information To Add Access Schem") 
            self.save_button.setEnabled(False)      
        else:
            count=0 
            for i in range (accesSchemLen):
                self.access_drop.addItem(accesSchem1[count])
                count+=1  

    
    def DB(self):
            conn = sqlite3.connect("./DataBaseTabletest.db")
            conn.text_factory=str
            cursor = conn.cursor()
            

            self.dep=self.dep_drop.currentText()
            self.jobTitle=self.job_drop.currentText()
            self.attendSch=self.attend_drop.currentText()
            self.accessCat=self.access_drop.currentText()


            dep_query = 'SELECT Dept_ID FROM DepartmentsTable WHERE Dept_Name =\''+self.dep+"\'"
            cursor.execute(dep_query)
            dep_query_result  = cursor.fetchone()
           # dep_query_result_str=[r[0] for r in dep_query_result]

            Job_query = 'SELECT Emp_Job_ID FROM JobTittle WHERE JobDesc =\''+self.jobTitle+"\'"
            cursor.execute(Job_query)
            Job_query_result  = cursor.fetchone()
            #Job_query_result_str=[r[0] for r in Job_query_result]

            attendSch_query = 'SELECT AttendanceSchemes_ID FROM Attendance_Schemes_Table WHERE AttendanceDesc =\''+self.attendSch+"\'"
            cursor.execute(attendSch_query)
            attendSch_query_result  = cursor.fetchone()
            #attendSch_query_result_str=[r[0] for r in attendSch_query_result]

            AccessCat_query = 'SELECT AccessSchemID FROM AccessScheme WHERE Category =\''+self.accessCat+"\'"
            cursor.execute(AccessCat_query)
            AccessCat_query_result  = cursor.fetchone()
            #AccessCat_query_result_str=[r[0] for r in AccessCat_query_result]


            #aa=dep_query_result[0]
            if dep_query_result is None :
                QMessageBox.about(self, "alert", "please Fill All the Missing Parts ")
                self.error.setText("Please Fill the Missing Parts")

            elif dep_query_result is not None:
                Emp_info=[self.firstname1,self.middlename1,self.lastname1,self.address,self.var_name,dep_query_result[0],Job_query_result[0],attendSch_query_result[0],AccessCat_query_result[0]]

                cursor.execute("INSERT INTO Employees (Emp_First_Name, Emp_Middle_Name, Emp_Last_Name,Emp_Address,Emp_DOB,Emp_Dpet_ID,Emp_Job_ID,Emp_Attendace_SchemeID,Emp_Access_ID) VALUES (?,?,?,?,?,?,?,?,?);",Emp_info)
            for row in cursor.execute('SELECT Emp_ID FROM Employees ORDER BY Emp_ID DESC LIMIT 1;'):
                #print(row)
                printIDint=int(row[0])
                #printIDint+=1
                printIDstr=str(printIDint)
                self.capture_Emp_ID=printIDstr  
                QMessageBox.about(self, "alert", "Employee Added its ID"+self.capture_Emp_ID)
               


            else:
                QMessageBox.about(self, "alert", "please Fill All the Missing Parts ")
                self.error.setText("Please Fill the Missing Parts")
    
                conn.commit()
                conn.close()
    

##################################################################################################3

class EditEmployee(QDialog):
    def __init__(self) -> None:
        super().__init__()
        pass






########################################################################################

class AddNewUser(QDialog):
    def __init__(self):
        super(AddNewUser, self).__init__()
        loadUi("./GUI/newuser.ui",self)
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CancelButton.clicked.connect(self.goBack)
        self.save_btn.clicked.connect(self.save)

        
    def signupfunction(self):
        EmpId=self.id.text()
        user = self.user_line.text()
        password = self.pass_line.text()
        confirmpassword = self.confirmpass_line.text()

         
        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")

        else:
            conn = sqlite3.connect("./DataBaseTabletest.db")
            cur = conn.cursor()

            for EmpId in (EmpId):
                cur.execute("SELECT rowid FROM Employees WHERE Emp_ID = ?", (EmpId, ))
            data = cur.fetchall()
            if len(EmpId) ==0:
                print('There is No Employee With This ID %s' % EmpId)
                QMessageBox.about(self, "alert", 'There is No Employee With This ID %s' % EmpId)
            else :
               # print('Employee Found Adding his admin account  %s' % (EmpId, ','.join(map(str, next(zip( * data))))))

                user_info = [user,password,EmpId]
                cur.execute('INSERT INTO Users (User_Name, User_Password,Emp_ID) VALUES (?,?,?)', user_info)

                conn.commit()
                conn.close()
                QMessageBox.about(self, "alert", 'Employee With This ID  %s ->> Admin account Added' % EmpId)

    def goBack(self):
        back2wle = MainWin()
        widget.addWidget(back2wle)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Main Screen")

##############################################################################################
class CompanyInfo(QDialog):
   def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back_btn.clicked.connect(self.gotomainmenu)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.toggle_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.dep_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page0))

        # PAGE 2
        self.ui.jd_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page1))

        # PAGE 3
        self.ui.att_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page2))
        # page 4
        self.ui.acc_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page3)) 
       
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
    
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    sys.exit(app.exec_())
        





    