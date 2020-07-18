import os
import label.Label_List

# 题目最终存储地址
path = "D:\\Codes\\Python\\leecode\\题库"


def makepath():
    global path
    label_list = label.Label_List.getlabellist()
    for i in label_list:
        mkpath = path + "\\" + i
        os.mkdir(mkpath)
