# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:19:53 2020

@author: YYN
"""


import os
import sys
dirname, filename = os.path.split((os.path.abspath(sys.argv[0]))) 
targetpath = dirname + os.path.sep + 'image' 
if not os.path.exists(targetpath):                                          # 判断路径是否存在，不存在则创建
    os.makedirs(targetpath)
    LeftHand_path = targetpath + os.path.sep + 'Left_hand' #左手路径
    RightHand_path = targetpath + os.path.sep + 'Right_hand'  #右手路径
    if not (os.path.exists(LeftHand_path) and os.path.exists(RightHand_path)):
        os.makedirs(LeftHand_path)
        os.makedirs(RightHand_path)
        # os.chdir(targetpath)                                                        # 设置当前工作路径
    users_LeftHand = open(LeftHand_path + os.path.sep + 'users_l.txt', 'x+')#记录用户左手的信息
    users_RightHand = open(RightHand_path + os.path.sep + 'users_r.txt', 'x+')#记录用户右手的信息
    users_LeftHand.close()
    users_RightHand.close()
os.chdir(targetpath + os.path.sep + 'Left_hand')#可直接访问
os.chdir(targetpath + os.path.sep + 'Right_hand')
Left_text = open('users_l.txt','a')#将用户信息写入这个文件
Right_text = open('users_r.txt','a')#将用户信息写入这个文件
