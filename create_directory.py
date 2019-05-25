import os

# 创建文件夹，存储csv文件
def Create_dir(filename_1,filename_2):

    curpath = os.getcwd()
    targetpath_1 = curpath + os.path.sep + filename_1  # 确定文件夹路径
    targetpath_2 = targetpath_1 + '/'+filename_2
    if not os.path.exists(targetpath_1):  # 判断是否已存在该文件夹
        os.makedirs(targetpath_1)  # 创建文件夹，包括文件夹的上级目录也会创建，这里是创建在当前目录下
    else:
        print('文件夹1已经存在')

    if not os.path.exists(targetpath_2):  # 判断是否已存在该文件夹
        os.makedirs(targetpath_2)
    else:
        print('文件夹2已经存在')
