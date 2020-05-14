# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collect_sample2_0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1098, 690)
        self.SystemTitle = QtWidgets.QLabel(Dialog)
        self.SystemTitle.setGeometry(QtCore.QRect(250, 20, 571, 41))
        self.SystemTitle.setMaximumSize(QtCore.QSize(571, 41))
        self.SystemTitle.setStyleSheet("\n"
"font: 24pt \"黑体\";")
        self.SystemTitle.setTextFormat(QtCore.Qt.PlainText)
        self.SystemTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.SystemTitle.setWordWrap(True)
        self.SystemTitle.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.SystemTitle.setObjectName("SystemTitle")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(900, 90, 181, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.VisiblePhoto_1 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_1.setStyleSheet("font: 6pt \"Arial\";")
        self.VisiblePhoto_1.setAlignment(QtCore.Qt.AlignCenter)
        self.VisiblePhoto_1.setObjectName("VisiblePhoto_1")
        self.gridLayout_2.addWidget(self.VisiblePhoto_1, 0, 0, 1, 1)
        self.VisiblePhoto_2 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_2.setStyleSheet("font: 6pt \"Arial\";")
        self.VisiblePhoto_2.setObjectName("VisiblePhoto_2")
        self.gridLayout_2.addWidget(self.VisiblePhoto_2, 0, 1, 1, 1)
        self.VisiblePhoto_3 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_3.setStyleSheet("font: 6pt \"Arial\";")
        self.VisiblePhoto_3.setAlignment(QtCore.Qt.AlignCenter)
        self.VisiblePhoto_3.setObjectName("VisiblePhoto_3")
        self.gridLayout_2.addWidget(self.VisiblePhoto_3, 1, 0, 1, 1)
        self.VisiblePhoto_4 = QtWidgets.QLabel(self.layoutWidget)
        self.VisiblePhoto_4.setStyleSheet("font: 6pt \"Arial\";")
        self.VisiblePhoto_4.setAlignment(QtCore.Qt.AlignCenter)
        self.VisiblePhoto_4.setObjectName("VisiblePhoto_4")
        self.gridLayout_2.addWidget(self.VisiblePhoto_4, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 80, 651, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VisibleVideo = QtWidgets.QLabel(self.layoutWidget1)
        self.VisibleVideo.setText("")
        self.VisibleVideo.setObjectName("VisibleVideo")
        self.horizontalLayout.addWidget(self.VisibleVideo)
        self.InfraedVideo = QtWidgets.QLabel(self.layoutWidget1)
        self.InfraedVideo.setText("")
        self.InfraedVideo.setObjectName("InfraedVideo")
        self.horizontalLayout.addWidget(self.InfraedVideo)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 80, 181, 211))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.InfraedPhoto_1 = QtWidgets.QLabel(self.layoutWidget2)
        self.InfraedPhoto_1.setStyleSheet("font: 6pt \"Arial\";")
        self.InfraedPhoto_1.setAlignment(QtCore.Qt.AlignCenter)
        self.InfraedPhoto_1.setObjectName("InfraedPhoto_1")
        self.gridLayout.addWidget(self.InfraedPhoto_1, 0, 0, 1, 1)
        self.InfraedPhoto_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.InfraedPhoto_2.setStyleSheet("font: 6pt \"Arial\";")
        self.InfraedPhoto_2.setObjectName("InfraedPhoto_2")
        self.gridLayout.addWidget(self.InfraedPhoto_2, 0, 1, 1, 1)
        self.InfraedPhoto_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.InfraedPhoto_3.setStyleSheet("font: 6pt \"Arial\";")
        self.InfraedPhoto_3.setAlignment(QtCore.Qt.AlignCenter)
        self.InfraedPhoto_3.setObjectName("InfraedPhoto_3")
        self.gridLayout.addWidget(self.InfraedPhoto_3, 1, 0, 1, 1)
        self.InfraedPhoto_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.InfraedPhoto_4.setStyleSheet("font: 6pt \"Arial\";")
        self.InfraedPhoto_4.setAlignment(QtCore.Qt.AlignCenter)
        self.InfraedPhoto_4.setObjectName("InfraedPhoto_4")
        self.gridLayout.addWidget(self.InfraedPhoto_4, 1, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(232, 380, 651, 71))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.Button_function = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.Button_function.setContentsMargins(0, 0, 0, 0)
        self.Button_function.setObjectName("Button_function")
        self.Collect_image = QtWidgets.QPushButton(self.layoutWidget3)
        self.Collect_image.setStyleSheet("font: 20pt \"Arial\";")
        self.Collect_image.setObjectName("Collect_image")
        self.Button_function.addWidget(self.Collect_image)
        self.register_2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.register_2.setStyleSheet("font: 20pt \"Arial\";")
        self.register_2.setObjectName("register_2")
        self.Button_function.addWidget(self.register_2)
        self.verify = QtWidgets.QPushButton(self.layoutWidget3)
        self.verify.setEnabled(True)
        self.verify.setStyleSheet("font: 20pt \"Arial\";")
        self.verify.setObjectName("verify")
        self.Button_function.addWidget(self.verify)
        self.label_output = QtWidgets.QLabel(Dialog)
        self.label_output.setGeometry(QtCore.QRect(770, 490, 281, 161))
        self.label_output.setMouseTracking(False)
        self.label_output.setTabletTracking(False)
        self.label_output.setText("")
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.layoutWidget4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget4.setGeometry(QtCore.QRect(910, 370, 171, 91))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.infraed_varify = QtWidgets.QLabel(self.layoutWidget4)
        self.infraed_varify.setText("")
        self.infraed_varify.setObjectName("infraed_varify")
        self.horizontalLayout_2.addWidget(self.infraed_varify)
        self.visible_varify = QtWidgets.QLabel(self.layoutWidget4)
        self.visible_varify.setText("")
        self.visible_varify.setObjectName("visible_varify")
        self.horizontalLayout_2.addWidget(self.visible_varify)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(12, 362, 191, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.image_count = QtWidgets.QLabel(self.splitter)
        self.image_count.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.image_count.setObjectName("image_count")
        self.label_image_number = QtWidgets.QLabel(self.splitter)
        self.label_image_number.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.label_image_number.setText("")
        self.label_image_number.setObjectName("label_image_number")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(420, 460, 261, 161))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.name.setObjectName("name")
        self.gridLayout_3.addWidget(self.name, 0, 0, 1, 1)
        self.gender = QtWidgets.QLabel(self.widget)
        self.gender.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.gender.setObjectName("gender")
        self.gridLayout_3.addWidget(self.gender, 1, 0, 1, 1)
        self.radioButton_man = QtWidgets.QRadioButton(self.widget)
        self.radioButton_man.setStyleSheet("font: 12pt \"Arial\";")
        self.radioButton_man.setObjectName("radioButton_man")
        self.gridLayout_3.addWidget(self.radioButton_man, 1, 1, 1, 1)
        self.radioButton_woman = QtWidgets.QRadioButton(self.widget)
        self.radioButton_woman.setStyleSheet("font: 12pt \"Arial\";")
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.gridLayout_3.addWidget(self.radioButton_woman, 1, 2, 1, 1)
        self.age = QtWidgets.QLabel(self.widget)
        self.age.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.age.setObjectName("age")
        self.gridLayout_3.addWidget(self.age, 2, 0, 1, 1)
        self.palm = QtWidgets.QLabel(self.widget)
        self.palm.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.palm.setObjectName("palm")
        self.gridLayout_3.addWidget(self.palm, 3, 0, 1, 1)
        self.radioButton_l = QtWidgets.QRadioButton(self.widget)
        self.radioButton_l.setStyleSheet("font: 12pt \"Arial\";")
        self.radioButton_l.setObjectName("radioButton_l")
        self.gridLayout_3.addWidget(self.radioButton_l, 3, 1, 1, 1)
        self.radioButton_r = QtWidgets.QRadioButton(self.widget)
        self.radioButton_r.setStyleSheet("font: 12pt \"Arial\";")
        self.radioButton_r.setObjectName("radioButton_r")
        self.gridLayout_3.addWidget(self.radioButton_r, 3, 2, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_3.addWidget(self.lineEdit_name, 0, 1, 1, 2)
        self.lineEdit_age = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_age.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.gridLayout_3.addWidget(self.lineEdit_age, 2, 1, 1, 2)
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(453, 630, 191, 51))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_save = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_save.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_clear = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_clear.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "身份验证系统"))
        self.SystemTitle.setText(_translate("Dialog", "掌纹掌静脉身份识别系统"))
        self.VisiblePhoto_1.setText(_translate("Dialog", "可见图像1"))
        self.VisiblePhoto_2.setText(_translate("Dialog", "可见图像2"))
        self.VisiblePhoto_3.setText(_translate("Dialog", "可见图像3"))
        self.VisiblePhoto_4.setText(_translate("Dialog", "可见图像4"))
        self.InfraedPhoto_1.setText(_translate("Dialog", "红外图像1"))
        self.InfraedPhoto_2.setText(_translate("Dialog", "红外图像2"))
        self.InfraedPhoto_3.setText(_translate("Dialog", "红外图像3"))
        self.InfraedPhoto_4.setText(_translate("Dialog", "红外图像4"))
        self.Collect_image.setText(_translate("Dialog", "采集"))
        self.register_2.setText(_translate("Dialog", "注册"))
        self.verify.setText(_translate("Dialog", "验证"))
        self.image_count.setText(_translate("Dialog", "图像数量为："))
        self.name.setText(_translate("Dialog", "姓名："))
        self.gender.setText(_translate("Dialog", "性别："))
        self.radioButton_man.setText(_translate("Dialog", "男"))
        self.radioButton_woman.setText(_translate("Dialog", "女"))
        self.age.setText(_translate("Dialog", "年龄："))
        self.palm.setText(_translate("Dialog", "手掌："))
        self.radioButton_l.setText(_translate("Dialog", "左手"))
        self.radioButton_r.setText(_translate("Dialog", "右手"))
        self.pushButton_save.setText(_translate("Dialog", "保存"))
        self.pushButton_clear.setText(_translate("Dialog", "清空"))
class myWindow(Ui_Dialog,QtWidgets.QWidget):

    def __init__(self,id=0):#id用来给用户分配序号
        super(myWindow,self).__init__()
        self.setupUi(self)
        self.id = id

        self.cap1, self.cap2 = cv.VideoCapture(1), cv.VideoCapture(2)  # cap1是红外，cap2是可见
        if not (self.cap1.isOpened() and self.cap2.isOpened()):
            QtWidgets.QMessageBox.warning(self, "警告", "未成功打开摄像头！")
        self.video_timer = QtCore.QTimer()#用于定时采集视频的帧
        self.Collect_image.clicked.connect(self.video_play_slot)  # 显示每一帧图像。Y
        self.captureImg_flag = False  # 截图控制符
        self.captureImg_count = 0  # 截图数目
        self.img_list_h = []  # 保存截图,用于保存红外图像
        self.img_list_k = []  # 保存截图,用于保存红外图像
        self.captureImg_num = 0  # 截图数量
        #这后面可以加入信号与槽的方法
        self.pushButton_save.clicked.connect(self.save_image)#保存信息
    def video_play_slot(self):#236行的槽方法
        if not (self.cap1.isOpened() and self.cap2.isOpened()):
            QtWidgets.QMessageBox.warning(self, "警告", "未成功打开摄像头！请关闭界面并重新打开！")
        else:
            if not self.video_timer.isActive():
                self.video_timer.start(30)
                self.video_timer.timeout.connect(self.display_img)
            else:
                self.captureImg_flag = True
    def display_img(self):#显示每一帧图像，242行
        self.label_image_number.setText(str(len(self.img_list_h)))  # 显示当前采集的照片数量
        ret1, frame1 = self.cap1.read()#红外
        ret2, frame2 = self.cap2.read()#可见
        if not (ret1 and ret2):
            print("cannot receive this frame.")
        else:
            frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2RGB)
            height1, width1, bytesPerComponent = frame1.shape
            bytesPerLine = bytesPerComponent * width1
            q_image_h = QtGui.QImage(frame1.data, width1, height1, bytesPerLine,
                                   QtGui.QImage.Format_RGB888).scaled(self.InfraedVideo.width(), self.InfraedVideo.height())
            self.InfraedVideo.setPixmap(QtGui.QPixmap.fromImage(q_image_h))
            # 新添加内容
            frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2RGB)
            height2, width2, bytesPerComponent = frame2.shape
            bytesPerLine = bytesPerComponent * width2
            q_image_k = QtGui.QImage(frame2.data, width2, height2, bytesPerLine,
                                    QtGui.QImage.Format_RGB888).scaled(self.VisibleVideo.width(), self.VisibleVideo.height())
            self.VisibleVideo.setPixmap(QtGui.QPixmap.fromImage(q_image_k))
        if self.captureImg_flag:

            # if self.captureImg_count == 1:
            #     QtWidgets.QMessageBox.information(self, "提醒", "请尽量保持所采集的照片人脸姿态多样性！")

            if len(self.img_list_h) >= 4:
                self.img_list_h.pop(0)
                self.img_list_k.pop(0)

            frame3 = frame1.copy()
            frame4 = frame2.copy()


            temp = self.captureImg_count % 4
            height, width, bytesPerComponent = frame1.shape
            bytesPerLine = bytesPerComponent * width
            q_image_h= QtGui.QImage(frame3.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).scaled(
                self.InfraedPhoto_1.width(), self.InfraedPhoto_1.height())
            q_image_k = QtGui.QImage(frame4.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).scaled(
                self.VisiblePhoto_1.width(), self.VisiblePhoto_1.height())
            if temp == 0:
                self.InfraedPhoto_1.setPixmap(QtGui.QPixmap.fromImage(q_image_h))
                self.img_list_h.append(frame3)
                # print(len(self.img_list))
                self.VisiblePhoto_1.setPixmap(QtGui.QPixmap.fromImage(q_image_k))
                self.img_list_k.append(frame4)
            elif temp == 1:
                self.InfraedPhoto_2.setPixmap(QtGui.QPixmap.fromImage(q_image_h))
                self.img_list_h.append(frame3)
                # print(len(self.img_list))
                self.VisiblePhoto_2.setPixmap(QtGui.QPixmap.fromImage(q_image_k))
                self.img_list_k.append(frame4)
            elif temp == 2:
                self.InfraedPhoto_3.setPixmap(QtGui.QPixmap.fromImage(q_image_h))
                self.img_list_h.append(frame3)
                # print(len(self.img_list))
                self.VisiblePhoto_3.setPixmap(QtGui.QPixmap.fromImage(q_image_k))
                self.img_list_k.append(frame4)
            elif temp == 3:
                self.InfraedPhoto_4.setPixmap(QtGui.QPixmap.fromImage(q_image_h))
                self.img_list_h.append(frame3)
                self.VisiblePhoto_4.setPixmap(QtGui.QPixmap.fromImage(q_image_k))
                self.img_list_k.append(frame4)

            self.captureImg_flag = False
            self.captureImg_count += 1
    def save_image(self):
        flag1 = False
        flag2 = False
        flag3 = False
        flag = False
        if len(self.img_list_h) < 4:  # 判断照片数量
            QtWidgets.QMessageBox.warning(self, "警告", "照片数量小于四张！")
        else:
            flag1 = True
        name_str = self.lineEdit_name.text()
        if len(name_str) == 0:  # 判断是否输入姓名
            QtWidgets.QMessageBox.warning(self, "警告", "姓名为空！")
        else:
            flag2 = True
        if self.radioButton_man.isChecked() == self.radioButton_woman.isChecked():  # 判断是否选择性别
            QtWidgets.QMessageBox.warning(self, "警告", "未选择性别！")
        else:
            flag3 = True
        if self.radioButton_l.isChecked() == self.radioButton_r.isChecked():  # 判断是否选择左右手
            QtWidgets.QMessageBox.warning(self, "警告", "未选择走右手！")
        else:
            flag4 = True
        age_str = self.lineEdit_age.text()
        if len(age_str) == 0:  # 判断是否输入年龄
            QtWidgets.QMessageBox.warning(self, "警告", "年龄为空！")
        else:
            flag5 = True
        #保存信息到相应文件中
        if flag2 and flag1 and flag3 and flag4 and flag5:#只有当信息都填写完整才会保存
            self.id += 1  # 所有信息填写完毕，分配id
            dirname, filename = os.path.split((os.path.abspath(sys.argv[0])))           # 获取当前主运行文件绝对地址
            targetpath = dirname + os.path.sep + 'image'                                  # 构造文件路径
            if not os.path.exists(targetpath):  # 判断路径是否存在，不存在则创建
                os.makedirs(targetpath)
                LeftHand_path = targetpath + os.path.sep + 'Left_hand'  # 左手路径
                RightHand_path = targetpath + os.path.sep + 'Right_hand'  # 右手路径
                if not (os.path.exists(LeftHand_path) and os.path.exists(RightHand_path)):
                    os.makedirs(LeftHand_path)
                    os.makedirs(RightHand_path)
                    LeftHand_path_H = LeftHand_path + os.path.sep + 'H'  # 左手红外路径
                    LeftHand_path_K = LeftHand_path + os.path.sep + 'K'  # 左手可见路径
                    if not (os.path.exists(LeftHand_path_H) and os.path.exists(LeftHand_path_K)):
                        os.makedirs(LeftHand_path_H)
                        os.makedirs(LeftHand_path_K)
                    RightHand_path_H = RightHand_path + os.path.sep + 'H'  # 右手红外路径
                    RightHand_path_K = RightHand_path + os.path.sep + 'K'  # 右手红外路径
                    if not (os.path.exists(RightHand_path_H) and os.path.exists(RightHand_path_K)):
                        os.makedirs(RightHand_path_H)
                        os.makedirs(RightHand_path_K)
                    # os.chdir(targetpath)                                                        # 设置当前工作路径
                users_LeftHand = open(LeftHand_path + os.path.sep + 'users_l.txt', 'x+')  # 记录用户左手的信息
                users_RightHand = open(RightHand_path + os.path.sep + 'users_r.txt', 'x+')  # 记录用户右手的信息
                users_LeftHand.close()
                users_RightHand.close()
            os.chdir(targetpath + os.path.sep + 'Left_hand')  # 可直接访问
            os.chdir(targetpath + os.path.sep + 'Right_hand')
            Left_text = open('users_l.txt', 'a')  # 将用户信息写入这个文件
            Right_text = open('users_r.txt', 'a')  # 将用户信息写入这个文件
            #首先，判断左右手，将决定保存到那个文件中

            if self.radioButton_l.isChecked():#如果是左手
                user_data = name_str + ' '
                if self.radioButton_man.isChecked():  # 男女
                    user_data += 'man' + ' '
                elif self.radioButton_woman.isChecked():
                    user_data += 'woman' + ' '
                user_data += age_str + ' ' + 'LeftHand'  # 加入年龄及左右手类型
                Right_text.write(user_data)
                Right_text.write('\n')
                for _num in range(1,len(self.img_list_h)+1):
                    imgname_h = self.id + '_' +'h' + str(_num)+ '.jpg'
                    imgname_k = self.id + '_' + 'k' + str(_num) + '.jpg'
                    tempimg_h = cv.cvtColor(self.img_list_h[(len(self.img_list_h) - _num - 1)], cv.COLOR_RGB2BGR)
                    cv.imencode('.jpg', tempimg)[1].tofile(imgname_h)
                    temppath_h = targetpath + os.path.sep +'Left_hand'+'H'+ imgname_h + '#'
                    Left_text.write(temppath_h)#写左手，红外
                    #写左手，可见
                    tempimg_k = cv.cvtColor(self.img_list_k[(len(self.img_list_k) - _num - 1)], cv.COLOR_RGB2BGR)
                    cv.imencode('.jpg', tempimg)[1].tofile(imgname_k)
                    temppath_k = targetpath + os.path.sep + 'Left_hand' + 'K' + imgname_k
                    Left_text.write(temppath_k)  # 写左手，红外
                    Left_text.write('\n')
                Left_text.close()
                QtWidgets.QMessageBox.about(self, "保存", "保存成功！")
            elif self.radioButton_r.isChecked():#如果是右手
                user_data = name_str + ' '
                if self.radioButton_man.isChecked():#男女
                    user_data += 'man'+' '
                elif self.radioButton_woman.isChecked():
                    user_data += 'woman'+' '
                user_data += age_str+' '+ 'RightHand'#加入年龄及左右手类型
                Right_text.write(user_data)
                Right_text.write('\n')
                for _num in range(1,len(self.img_list_h)+1):
                    imgname_h = self.id + '_' +'h' + str(_num)+ '.jpg'
                    imgname_k = self.id + '_' + 'k' + str(_num) + '.jpg'
                    tempimg_h = cv.cvtColor(self.img_list_h[(len(self.img_list_h) - _num - 1)], cv.COLOR_RGB2BGR)
                    cv.imencode('.jpg', tempimg)[1].tofile(imgname_h)
                    temppath_h = targetpath + os.path.sep +'Right_hand'+'H'+ imgname_h + '#'
                    Right_text.write(temppath_h)#写右手，红外
                    #写右手，可见
                    tempimg_k = cv.cvtColor(self.img_list_k[(len(self.img_list_k) - _num - 1)], cv.COLOR_RGB2BGR)
                    cv.imencode('.jpg', tempimg)[1].tofile(imgname_k)
                    temppath_k = targetpath + os.path.sep + 'Right_hand' + 'K' + imgname_k
                    Right_text.write(temppath_k)  # 写左手，红外
                    Right_text.write('\n')
                Right_text.close()
                QtWidgets.QMessageBox.about(self, "保存", "保存成功！")
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
import sys
if __name__=="__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = myWindow()
        window.Collect_image.clicked.connect(window.display_img)
        window.show()
        sys.exit(app.exec_())
