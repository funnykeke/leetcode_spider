import promblem.Problem_Detail
import label.Label_List
import dir.MakeDir
import promblem.Problem_Url_Queue
import threading

if __name__ == '__main__':
    # 为所有题目标签创建对应文件夹
    dir.MakeDir.makepath()
    # 获取标签列表
    lablelist = label.Label_List.getlabellist()
    # 遍历并为每个标签开启一个线程
    for i in lablelist:
        threading.Thread(target=promblem.Problem_Detail.getproblem_detals, args=(i,)).start()
