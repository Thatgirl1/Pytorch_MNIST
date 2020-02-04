"""
导入必要的头文件
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from test import get_result
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class test_UI(QWidget):
    def __init__(self):
        super(test_UI,self).__init__()

    def setupUi(self, Form):
            self.form = Form  # 用户添加代码
            Form.setObjectName("Form")
            Form.setMinimumSize(QtCore.QSize(401, 221))
            Form.setMaximumSize(QtCore.QSize(1001, 221))
            Form.setStyleSheet("")

            self.times=0
            self.correct=0

            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(9, 135, 119, 16))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label.setFont(font)
            self.label.setObjectName("label")

            self.label2 = QtWidgets.QLabel(Form)
            self.label2.setGeometry(QtCore.QRect(50, 13, 300, 106))
            font = QtGui.QFont()
            font.setPointSize(50)
            self.label2.setFont(font)
            self.label2.setObjectName("label2")

            self.label_1 = QtWidgets.QLabel(Form)
            self.label_1.setGeometry(QtCore.QRect(40, 25, 119, 96))
            font = QtGui.QFont()
            font.setPointSize(80)
            self.label_1.setFont(font)
            self.label_1.setObjectName("label_1")

            self.label3 = QtWidgets.QLabel(Form)
            self.label3.setGeometry(QtCore.QRect(106, 33, 300, 80))
            font = QtGui.QFont()
            font.setPointSize(18)
            self.label3.setFont(font)
            self.label3.setObjectName("label3")

            self.label4 = QtWidgets.QLabel(Form)
            self.label4.setGeometry(QtCore.QRect(280, 20, 119, 100))

            self.label5 = QtWidgets.QLabel(Form)
            self.label5.setGeometry(QtCore.QRect(30, 175, 90, 30))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label5.setFont(font)
            self.label5.setObjectName("label5")

            self.label6 = QtWidgets.QLabel(Form)
            self.label6.setGeometry(QtCore.QRect(300, 175, 80, 30))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label6.setFont(font)
            self.label6.setObjectName("label6")

            self.pushButton = QtWidgets.QPushButton(Form)
            self.pushButton.setGeometry(QtCore.QRect(160, 175, 75, 23))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton.setFont(font)
            self.pushButton.setCheckable(True)
            self.pushButton.setStyleSheet(_fromUtf8(
                "QPushButton{\n"
                "color: rgb(137, 221, 255);\n"
                "background-color: rgb(37, 121, 290);\n"
                "border-style:none;\n"
                "border:1px solid #3f3f3f; \n"
                "\n"
                "padding:5px;\n"
                "min-height:20px;\n"
                "border-radius:15px;\n"
                "}\n"

                "QPushButton:hover{\n"
                "color: rgb(0,0,0);\n"
                "background-color: rgb(65, 105, 225);\n"
                "border-style:none;\n"
                "border:1px solid #3f3f3f; \n"
                "\n"
                "padding:5px;\n"
                "min-height:20px;\n"
                "border-radius:15px;\n"
                "}\n"
            ))
            self.pushButton.setObjectName("pushButton")

            self.lineEdit_3 = QtWidgets.QLineEdit(Form)
            self.lineEdit_3.setGeometry(QtCore.QRect(138, 132, 245, 25))
            self.lineEdit_3.setObjectName("lineEdit_3")

            palette1 = QPalette()
            palette1.setBrush(Form.backgroundRole(), QBrush(QPixmap('./backgroud.jpg')))
            Form.setPalette(palette1)

            self.retranslateUi(Form)

            self.pushButton.clicked.connect(self.get_root)


    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "MNIST数字识别实战"))
            self.label.setText(_translate("label", "请输入根目录："))
            self.label2.setText(_translate("label2", "Let's GO!"))
            self.lineEdit_3.setText(_translate("lineEdit_3","./test_data"))
            #"C:/Users\FDL\Desktop/test"is my dataset files and directories,and you can change it to yours
            self.pushButton.setText(_translate("Form", "开始"))


    def get_root(self):
        self.label2.close()
        self.times +=1
        root_get = self.lineEdit_3.text()
        root_get=root_get+'/'
        result=get_result(root_get)
        _translate = QtCore.QCoreApplication.translate
        self.label_1.setText(_translate("Form", "%d"%result[0]))
        pixmap = QtGui.QPixmap(result[1]).scaled(100, 100)
        self.label4.setPixmap(pixmap)
        self.label4.show()
        pre,_,num=result
        if pre==num:
            self.correct+=1
            self.label3.setText(_translate("Form", "＜（＾－＾）＞" ))
            self.label5.setText(_translate("Form", "correct:%d"%self.correct))
            self.label6.setText(_translate("Form", "times:%d"%self.times))
            self.label3.setStyleSheet(
                "color: rgb(34, 139, 34);\n"
            )
            self.label6.setStyleSheet(
                "color: rgb(255, 0, 0);\n"
            )
        else:
            self.label3.setText(_translate("Form", "！( T _ T ) ！" ))
            self.label3.setStyleSheet(
                "color: rgb(255, 0, 0);\n"
            )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = test_UI()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
