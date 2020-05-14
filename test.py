import os
import sys
dirname, filename = os.path.split((os.path.abspath(sys.argv[0]))) # 获取当前主运行文件绝对地址
targetpath = dirname + os.path.sep + 'image'+ os.path.sep+'Left_hand'+ os.path.sep+'users_l.txt'# 构造文件路径
if not os.path.exists(targetpath):  # 判断路径是否存在，不存在则创建
    print(1)
else:
    with open(targetpath,'r',encoding='UTF-8') as f:
        length = f.readlines()
        print(1+len(length)//5)