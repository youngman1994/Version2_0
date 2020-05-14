# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collect_sample.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
import sys
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1098, 690)
        self.SystemTitle = QtWidgets.QLabel(Dialog)
        self.SystemTitle.setGeometry(QtCore.QRect(250, 20, 571, 41))
        self.SystemTitle.setMaximumSize(QtCore.QSize(571, 41))
        self.SystemTitle.setTextFormat(QtCore.Qt.PlainText)
        self.SystemTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.SystemTitle.setWordWrap(True)
        self.SystemTitle.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.SystemTitle.setObjectName("SystemTitle")
        self.Verify_InfraedPhoto = QtWidgets.QLabel(Dialog)
        self.Verify_InfraedPhoto.setGeometry(QtCore.QRect(50, 380, 101, 121))
        self.Verify_InfraedPhoto.setTextFormat(QtCore.Qt.PlainText)
        self.Verify_InfraedPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.Verify_InfraedPhoto.setObjectName("Verify_InfraedPhoto")
        self.Verify_VisiblePhoto_2 = QtWidgets.QLabel(Dialog)
        self.Verify_VisiblePhoto_2.setGeometry(QtCore.QRect(910, 380, 101, 121))
        self.Verify_VisiblePhoto_2.setTextFormat(QtCore.Qt.PlainText)
        self.Verify_VisiblePhoto_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Verify_VisiblePhoto_2.setObjectName("Verify_VisiblePhoto_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(900, 90, 181, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.VisiblePhoto_1 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_1.setAlignment(QtCore.Qt.AlignCenter)
        self.VisiblePhoto_1.setObjectName("VisiblePhoto_1")
        self.gridLayout_2.addWidget(self.VisiblePhoto_1, 0, 0, 1, 1)
        self.VisiblePhoto_2 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_2.setObjectName("VisiblePhoto_2")
        self.gridLayout_2.addWidget(self.VisiblePhoto_2, 0, 1, 1, 1)
        self.VisiblePhoto_3 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_3.setAlignment(QtCore.Qt.AlignCenter)
        self.VisiblePhoto_3.setObjectName("VisiblePhoto_3")
        self.gridLayout_2.addWidget(self.VisiblePhoto_3, 1, 0, 1, 1)
        self.VisiblePhoto_4 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_4.setAlignment(QtCore.Qt.AlignCenter)
        self.VisiblePhoto_4.setObjectName("VisiblePhoto_4")
        self.gridLayout_2.addWidget(self.VisiblePhoto_4, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(230, 80, 651, 281))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VisibleVideo = QtWidgets.QLabel(self.widget)
        self.VisibleVideo.setText("")
        self.VisibleVideo.setObjectName("VisibleVideo")
        self.horizontalLayout.addWidget(self.VisibleVideo)
        self.InfraedVideo = QtWidgets.QLabel(self.widget)
        self.InfraedVideo.setText("")
        self.InfraedVideo.setObjectName("InfraedVideo")
        self.horizontalLayout.addWidget(self.InfraedVideo)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(30, 80, 181, 211))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.InfraedPhoto_1 = QtWidgets.QLabel(self.widget1)
        self.InfraedPhoto_1.setAlignment(QtCore.Qt.AlignCenter)
        self.InfraedPhoto_1.setObjectName("InfraedPhoto_1")
        self.gridLayout.addWidget(self.InfraedPhoto_1, 0, 0, 1, 1)
        self.InfraedPhoto_2 = QtWidgets.QLabel(self.widget1)
        self.InfraedPhoto_2.setObjectName("InfraedPhoto_2")
        self.gridLayout.addWidget(self.InfraedPhoto_2, 0, 1, 1, 1)
        self.InfraedPhoto_3 = QtWidgets.QLabel(self.widget1)
        self.InfraedPhoto_3.setAlignment(QtCore.Qt.AlignCenter)
        self.InfraedPhoto_3.setObjectName("InfraedPhoto_3")
        self.gridLayout.addWidget(self.InfraedPhoto_3, 1, 0, 1, 1)
        self.InfraedPhoto_4 = QtWidgets.QLabel(self.widget1)
        self.InfraedPhoto_4.setAlignment(QtCore.Qt.AlignCenter)
        self.InfraedPhoto_4.setObjectName("InfraedPhoto_4")
        self.gridLayout.addWidget(self.InfraedPhoto_4, 1, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(232, 380, 651, 71))
        self.widget2.setObjectName("widget2")
        self.Button_function = QtWidgets.QHBoxLayout(self.widget2)
        self.Button_function.setContentsMargins(0, 0, 0, 0)
        self.Button_function.setObjectName("Button_function")
        self.Collect_image = QtWidgets.QPushButton(self.widget2)
        self.Collect_image.setObjectName("Collect_image")
        self.Button_function.addWidget(self.Collect_image)
        self.Clear = QtWidgets.QPushButton(self.widget2)
        self.Clear.setObjectName("Clear")
        self.Button_function.addWidget(self.Clear)
        self.register_2 = QtWidgets.QPushButton(self.widget2)
        self.register_2.setObjectName("register_2")
        self.Button_function.addWidget(self.register_2)
        self.verify = QtWidgets.QPushButton(self.widget2)
        self.verify.setEnabled(True)
        self.verify.setObjectName("verify")
        self.Button_function.addWidget(self.verify)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "身份验证系统"))
        self.SystemTitle.setText(_translate("Dialog", "掌纹掌静脉身份识别系统"))
        self.Verify_InfraedPhoto.setText(_translate("Dialog", "验证红外图像"))
        self.Verify_VisiblePhoto_2.setText(_translate("Dialog", "验证可见图像"))
        self.VisiblePhoto_1.setText(_translate("Dialog", "可见图像1"))
        self.VisiblePhoto_2.setText(_translate("Dialog", "可见图像2"))
        self.VisiblePhoto_3.setText(_translate("Dialog", "可见图像3"))
        self.VisiblePhoto_4.setText(_translate("Dialog", "可见图像4"))
        self.InfraedPhoto_1.setText(_translate("Dialog", "红外图像1"))
        self.InfraedPhoto_2.setText(_translate("Dialog", "红外图像2"))
        self.InfraedPhoto_3.setText(_translate("Dialog", "红外图像3"))
        self.InfraedPhoto_4.setText(_translate("Dialog", "红外图像4"))
        self.Collect_image.setText(_translate("Dialog", "采集"))
        self.Clear.setText(_translate("Dialog", "清空"))
        self.register_2.setText(_translate("Dialog", "注册"))
        self.verify.setText(_translate("Dialog", "验证"))
class myWindow(Ui_Dialog,QtWidgets.QWidget):

    def __init__(self):
        super(myWindow,self).__init__()
        self.setupUi(self)

        self.cap1, self.cap2 = cv.VideoCapture(1), cv.VideoCapture(2)  # cap1是红外，cap2是可见
        if not (self.cap1.isOpened() and self.cap2.isOpened()):
            QtWidgets.QMessageBox.warning(self, "警告", "未成功打开摄像头！")
        self.video_timer = QtCore.QTimer()#用于定时采集视频的帧
        self.Collect_image.clicked.connect(self.video_play_slot)  # 显示每一帧图像。Y
        self.captureImg_flag = False  # 截图控制符
        self.captureImg_count = 0  # 截图数目
        self.img_list = []  # 保存截图,用于保存图像
        self.captureImg_num = 0  # 截图数量

        #self.save_pb.clicked.connect(self.save_info)  # 保存信息

        self.Clear.clicked.connect(self.clear_content)
    def video_play_slot(self):
        if not (self.cap1.isOpened() and self.cap2.isOpened()):
            QtWidgets.QMessageBox.warning(self, "警告", "未成功打开摄像头！请关闭界面并重新打开！")
        else:
            if not self.video_timer.isActive():
                self.video_timer.start(30)
                self.video_timer.timeout.connect(self.display_img)
            else:
                self.captureImg_flag = True

    def closeEvent(self, QCloseEvent):
        '''
        窗口关闭事件
        :param QCloseEvent:
        :return:
        '''
        reply = QtWidgets.QMessageBox.question(self, "确认", "确认退出吗?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.video_timer.stop()
            self.cap1.release()
            self.cap2.release()
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    def display_img(self):#显示每一帧图像
        #self.photo_num.setText(str(len(self.img_list)))  # 显示当前采集的照片数量
        ret1, frame1 = self.cap1.read()
        ret2, frame2 = self.cap2.read()
        if not (ret1 and ret2):
            print("cannot receive this frame.")
        else:
            frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2RGB)
            height1, width1, bytesPerComponent = frame1.shape
            bytesPerLine = bytesPerComponent * width1
            q_image = QtGui.QImage(frame1.data, width1, height1, bytesPerLine,
                                   QtGui.QImage.Format_RGB888).scaled(self.InfraedVideo.width(), self.InfraedVideo.height())
            self.InfraedVideo.setPixmap(QtGui.QPixmap.fromImage(q_image))
            # 新添加内容
            frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2RGB)
            height2, width2, bytesPerComponent = frame2.shape
            bytesPerLine = bytesPerComponent * width2
            q_image1 = QtGui.QImage(frame2.data, width2, height2, bytesPerLine,
                                    QtGui.QImage.Format_RGB888).scaled(self.VisibleVideo.width(), self.VisibleVideo.height())
            self.VisibleVideo.setPixmap(QtGui.QPixmap.fromImage(q_image1))
        if self.captureImg_flag:

            # if self.captureImg_count == 1:
            #     QtWidgets.QMessageBox.information(self, "提醒", "请尽量保持所采集的照片人脸姿态多样性！")

            if len(self.img_list_h) >= 4:
                self.img_list_h.pop(0)
                self.img_list_k.pop(0)

            frame1 = frame.copy()
            frame3 = frame2.copy()


            temp = self.captureImg_count % 4
            height, width, bytesPerComponent = frame1.shape
            bytesPerLine = bytesPerComponent * width
            q_image = QtGui.QImage(frame1.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).scaled(
                self.InfraedPhoto_1.width(), self.InfraedPhoto_1.height())
            q_image2 = QtGui.QImage(frame3.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).scaled(
                self.VisiblePhoto_1.width(), self.VisiblePhoto_1.height())
            if temp == 0:
                self.InfraedPhoto_1.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list_h.append(frame1)
                # print(len(self.img_list))
                self.VisiblePhoto_1.setPixmap(QtGui.QPixmap.fromImage(q_image2))
                self.img_list_k.append(frame3)
            elif temp == 1:
                self.InfraedPhoto_2.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list_h.append(frame1)
                # print(len(self.img_list))
                self.VisiblePhoto_2.setPixmap(QtGui.QPixmap.fromImage(q_image2))
                self.img_list_k.append(frame3)
            elif temp == 2:
                self.InfraedPhoto_3.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list_h.append(frame1)
                # print(len(self.img_list))
                self.VisiblePhoto_3.setPixmap(QtGui.QPixmap.fromImage(q_image2))
                self.img_list_k.append(frame3)
            elif temp == 3:
                self.InfraedPhoto_4.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list_h.append(frame1)
                self.VisiblePhoto_4.setPixmap(QtGui.QPixmap.fromImage(q_image2))
                self.img_list_k.append(frame3)

            self.captureImg_flag = False
            self.captureImg_count += 1

    def clear_content(self):
        reply = QtWidgets.QMessageBox.question(self, "清空", "确认清空所有吗?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.VisiblePhoto_1.clear()
            self.VisiblePhoto_2.clear()
            self.VisiblePhoto_3.clear()
            self.VisiblePhoto_4.clear()
            self.InfraedPhoto_1.clear()
            self.InfraedPhoto_2.clear()
            self.InfraedPhoto_3.clear()
            self.InfraedPhoto_4.clear()
            self.img_list.clear()
            self.name.clear()
            self.captureImg_count = 0
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = myWindow()
    w.Collect_image.clicked.connect(w.display_img)
    w.show()
    sys.exit(app.exec_())

