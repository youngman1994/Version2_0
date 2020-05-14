# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
import sys
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 480)
        Form.setMinimumSize(QtCore.QSize(480, 480))
        Form.setMaximumSize(QtCore.QSize(480, 480))
        self.photo_pb = QtWidgets.QPushButton(Form)
        self.photo_pb.setGeometry(QtCore.QRect(190, 290, 81, 31))
        self.photo_pb.setStyleSheet("font: 14pt \"华文行楷\";")
        self.photo_pb.setObjectName("photo_pb")
        self.save_pb = QtWidgets.QPushButton(Form)
        self.save_pb.setGeometry(QtCore.QRect(150, 440, 75, 31))
        self.save_pb.setStyleSheet("font: 14pt \"华文行楷\";")
        self.save_pb.setObjectName("save_pb")
        self.photo_lbl = QtWidgets.QLabel(Form)
        self.photo_lbl.setGeometry(QtCore.QRect(70, 30, 160, 251))
        self.photo_lbl.setMinimumSize(QtCore.QSize(160, 251))
        self.photo_lbl.setMaximumSize(QtCore.QSize(160, 251))
        self.photo_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.photo_lbl.setText("")
        self.photo_lbl.setObjectName("photo_lbl")
        #新加的内容
        self.photo_lbr = QtWidgets.QLabel(Form)
        self.photo_lbr.setGeometry(QtCore.QRect(230, 30, 160, 251))
        self.photo_lbr.setMinimumSize(QtCore.QSize(160, 251))
        self.photo_lbr.setMaximumSize(QtCore.QSize(160, 251))
        self.photo_lbr.setFrameShape(QtWidgets.QFrame.Box)
        self.photo_lbr.setText("")
        self.photo_lbr.setObjectName("photo_lbr")
        #结束
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 350, 51, 20))
        self.label.setStyleSheet("font: 14pt \"华文行楷\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 390, 51, 20))
        self.label_2.setStyleSheet("font: 14pt \"华文行楷\";")
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(180, 350, 113, 20))
        self.name.setObjectName("name")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(180, 390, 41, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 390, 41, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.photo1 = QtWidgets.QLabel(Form)
        self.photo1.setGeometry(QtCore.QRect(410, 30, 51, 71))
        self.photo1.setMinimumSize(QtCore.QSize(51, 71))
        self.photo1.setMaximumSize(QtCore.QSize(51, 71))
        self.photo1.setFrameShape(QtWidgets.QFrame.Box)
        self.photo1.setObjectName("photo1")
        self.photo2 = QtWidgets.QLabel(Form)
        self.photo2.setGeometry(QtCore.QRect(410, 120, 51, 71))
        self.photo2.setMinimumSize(QtCore.QSize(51, 71))
        self.photo2.setMaximumSize(QtCore.QSize(51, 71))
        self.photo2.setFrameShape(QtWidgets.QFrame.Box)
        self.photo2.setObjectName("photo2")
        self.photo3 = QtWidgets.QLabel(Form)
        self.photo3.setGeometry(QtCore.QRect(410, 210, 51, 71))
        self.photo3.setMinimumSize(QtCore.QSize(51, 71))
        self.photo3.setMaximumSize(QtCore.QSize(51, 71))
        self.photo3.setFrameShape(QtWidgets.QFrame.Box)
        self.photo3.setObjectName("photo3")
        self.clear_pb = QtWidgets.QPushButton(Form)
        self.clear_pb.setGeometry(QtCore.QRect(250, 440, 71, 31))
        self.clear_pb.setStyleSheet("font: 14pt \"华文行楷\";")
        self.clear_pb.setObjectName("clear_pb")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(365, 300, 101, 21))
        self.label_3.setStyleSheet("font: 75 9pt \"Adobe Arabic\";")
        self.label_3.setObjectName("label_3")
        self.photo_num = QtWidgets.QLabel(Form)
        self.photo_num.setGeometry(QtCore.QRect(430, 300, 21, 20))
        self.photo_num.setText("")
        self.photo_num.setObjectName("photo_num")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "采集界面"))
        self.photo_pb.setText(_translate("Form", "采集照片"))
        self.save_pb.setText(_translate("Form", "保存"))
        self.label.setText(_translate("Form", "姓名："))
        self.label_2.setText(_translate("Form", "性别："))
        self.radioButton.setText(_translate("Form", "男"))
        self.radioButton_2.setText(_translate("Form", "女"))
        self.photo1.setText(_translate("Form", "照片1"))
        self.photo2.setText(_translate("Form", "照片2"))
        self.photo3.setText(_translate("Form", "照片3"))
        self.clear_pb.setText(_translate("Form", "清空"))
        self.label_3.setText(_translate("Form", "照片数量："))

class mywindow(Ui_Form, QtWidgets.QWidget):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.cap1,self.cap2 = cv.VideoCapture(1),cv.VideoCapture(2)#cap1是红外，cap2是可见
        if not (self.cap1.isOpened() and self.cap2.isOpened()):
            QtWidgets.QMessageBox.warning(self, "警告", "未成功打开摄像头！")
        self.video_timer = QtCore.QTimer()
        self.photo_pb.clicked.connect(self.video_play_slot)    # 显示每一帧图像
        self.captureImg_flag = False                           # 截图控制符
        self.captureImg_count = 0                              # 截图数目
        self.img_list = []                                     # 保存截图
        self.captureImg_num = 0                                # 截图数量

        self.save_pb.clicked.connect(self.save_info)           # 保存信息

        self.clear_pb.clicked.connect(self.clear_content)#可以在这个地方加入需要的方法

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
        reply = QtWidgets.QMessageBox.question(self, "确认", "确认退出吗?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.video_timer.stop()
            self.cap1.release()
            self.cap2.release()
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def display_img(self):
        '''
        显示每一帧图像
        :return: 无
        '''
        self.photo_num.setText(str(len(self.img_list)))     # 显示当前采集的照片数量

        ret1, frame1 = self.cap1.read()
        ret2, frame2 = self.cap2.read()

        if not (ret1 and ret2):
            print("cannot receive this frame.")
        else:#显示摄像头视频
            frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2RGB)
            height1, width1, bytesPerComponent = frame1.shape
            bytesPerLine = bytesPerComponent * width1
            q_image = QtGui.QImage(frame1.data, width1, height1, bytesPerLine,
                             QtGui.QImage.Format_RGB888).scaled(self.photo_lbl.width(), self.photo_lbl.height())
            self.photo_lbl.setPixmap(QtGui.QPixmap.fromImage(q_image))
            #新添加内容
            frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2RGB)
            height2, width2, bytesPerComponent = frame2.shape
            bytesPerLine = bytesPerComponent * width2
            q_image1 = QtGui.QImage(frame2.data, width2, height2, bytesPerLine,
                                   QtGui.QImage.Format_RGB888).scaled(self.photo_lbr.width(), self.photo_lbr.height())
            self.photo_lbr.setPixmap(QtGui.QPixmap.fromImage(q_image1))

        if self.captureImg_flag:

            # if self.captureImg_count == 1:
            #     QtWidgets.QMessageBox.information(self, "提醒", "请尽量保持所采集的照片人脸姿态多样性！")

            if len(self.img_list) >= 3:
                self.img_list.pop(0)

            frame1 = frame.copy()

            temp = self.captureImg_count % 3
            height, width, bytesPerComponent = frame1.shape
            bytesPerLine = bytesPerComponent * width
            q_image = QtGui.QImage(frame1.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888).scaled(self.photo1.width(), self.photo1.height())
            if temp == 0:
                self.photo1.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list.append(frame1)
                # print(len(self.img_list))
            elif temp == 1:
                self.photo2.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list.append(frame1)
                # print(len(self.img_list))
            elif temp == 2:
                self.photo3.setPixmap(QtGui.QPixmap.fromImage(q_image))
                self.img_list.append(frame1)
                # print(len(self.img_list))

            self.captureImg_flag = False
            self.captureImg_count += 1

    def save_info(self):
        flag1 = False
        flag2 = False
        flag3 = False
        if len(self.img_list) < 3:                                                   # 判断照片数量
            QtWidgets.QMessageBox.warning(self, "警告", "照片数量小于四张！")
        else:
            flag1 = True
        name_str = self.name.text()
        if len(name_str) == 0:                                                      # 判断是否输入姓名
            QtWidgets.QMessageBox.warning(self, "警告", "姓名为空！")
        else:
            flag2 = True

        if self.radioButton.isChecked() == self.radioButton_2.isChecked():           # 判断是否选择性别
            QtWidgets.QMessageBox.warning(self, "警告", "未选择性别！")
        else:
            flag3 = True

        if flag2 and flag1 and flag3:
            dirname, filename = os.path.split((os.path.abspath(sys.argv[0])))           # 获取当前主运行文件绝对地址
            targetpath = dirname + os.path.sep + 'img'                                  # 构造文件路径
            if not os.path.exists(targetpath):                                          # 判断路径是否存在，不存在则创建
                os.makedirs(targetpath)
                # os.chdir(targetpath)                                                        # 设置当前工作路径
                temp_info_text = open(dirname + os.path.sep + 'img' + os.path.sep + 'info.txt', 'x+')
                temp_info_text.close()
            os.chdir(targetpath)
            info_text = open('info.txt','a')
            for _num in range(3):
                imgname = name_str + '_' + str(_num) + '.jpg'#图像命名
                tempimg = cv.cvtColor(self.img_list[(len(self.img_list) - _num - 1)],cv.COLOR_RGB2BGR)
                cv.imencode('.jpg', tempimg)[1].tofile(imgname)
                temppath = targetpath + os.path.sep + imgname + '#'
                info_text.write(temppath)                                               # 保存照片路径

            if self.radioButton.isChecked():
                gender = '男' + '#'
            elif self.radioButton_2.isChecked():
                gender = '女' + '#'
            info_text.write(gender)                                                     # 写入性别信息
            info_text.write('\n')
            info_text.close()
            QtWidgets.QMessageBox.about(self, "保存", "保存成功！")

    def clear_content(self):
        reply = QtWidgets.QMessageBox.question(self, "清空", "确认清空所有吗?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.photo1.clear()
            self.photo2.clear()
            self.photo3.clear()
            self.img_list.clear()
            self.name.clear()
            self.captureImg_count = 0

            # self.radioButton.setChecked(False)
            # self.radioButton_2.setChecked(False)