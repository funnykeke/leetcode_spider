import label.Label_Dic


def getlabellist():
    label_list = list(label.Label_Dic.getlabel_dic().keys())
    return label_list
