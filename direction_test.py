import sys
import os
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