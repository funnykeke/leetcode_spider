from queue import Queue
import requests
import json
import lable.Label_Dic


def creatproblem_queue(label_name):
    url = 'https://leetcode-cn.com/graphql/'
    q = Queue(maxsize=1000)
    label_dic = lable.Label_Dic.getlabel_dic()
    # 英文名
    E_name = label_dic[label_name]
    data_temp = {"operationName": "getTagQuestions", "variables": {"slug": E_name},
                 "query": "query getTagQuestions($slug: String!) {\n  topicTag(slug: $slug) {\n    frequencies\n    "
                          "questions {\n      titleSlug\n      questionFrontendId\n      status\n      title\n      "
                          "translatedTitle\n      difficulty\n      stats\n      isPaidOnly\n      topicTags {\n "
                          "name\n        translatedName\n        slug\n        __typename\n      }\n      __typename\n "
                          "}\n    __typename\n  }\n}\n"}
    headers = {'Host': 'leetcode-cn.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
               'Accept': '*/*',
               'Accept-Language': 'zh-CN',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/json',
               'Content-Length': '482',
               'X-CSRFToken': 'qtLc74RuimYYxrBLGEEdoGrOpePAvCGjRFw1AIBciWerUoNtvhpscqa2gg9Kz5WB',
               'x-operation-name': 'getTagQuestions',
               'x-definition-name': 'topicTag',
               'x-timezone': 'Asia/Shanghai',
               'Origin': 'https://leetcode-cn.com',
               'Referer': 'https://leetcode-cn.com/tag/' + E_name + '/',
               'Connection': 'keep-alive',
               'TE': 'Trailers'}
    data = json.dumps(data_temp)
    response = requests.post(url=url, headers=headers, data=data)
    result = json.loads(response.text)
    for i in result["data"]["topicTag"]["questions"]:
        titleSlug = str(i["titleSlug"])
        q.put(titleSlug)
    return q
