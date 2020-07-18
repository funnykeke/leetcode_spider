import requests
import promblem.Problem_Url_Queue
import json
import dir.MakeDir

# 填写您尊贵的cookie
ck = ""


def getproblem_detals(i):
    print("爬取-" + i + "-标签进程开启成功")
    q = promblem.Problem_Url_Queue.creatproblem_queue(i)
    while not q.empty():
        titleSlug = str(q.get())
        data_temp = {"operationName": "questionData", "variables": {"titleSlug": titleSlug},
                     "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    "
                              "questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    "
                              "content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n  "
                              "  likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      "
                              "username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    "
                              "langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n "
                              "     __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      "
                              "langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n  "
                              "    id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n  "
                              "  metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n  "
                              "  envInfo\n    book {\n      id\n      bookName\n      pressName\n      source\n      "
                              "shortDescription\n      fullDescription\n      bookImgUrl\n      pressImgUrl\n      "
                              "productUrl\n      __typename\n    }\n    isSubscribed\n    isDailyQuestion\n    "
                              "dailyRecordStatus\n    editorType\n    ugcQuestionId\n    style\n    __typename\n  "
                              "}\n}\n"}
        url = "https://leetcode-cn.com/graphql/"
        headers = {'Host': 'leetcode-cn.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                   'Accept': '*/*',
                   'Accept-Language': 'zh-CN',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Content-Type': 'application/json',
                   'Content-Length': '1294',
                   'X-CSRFToken': 'qtLc74RuimYYxrBLGEEdoGrOpePAvCGjRFw1AIBciWerUoNtvhpscqa2gg9Kz5WB',
                   'x-operation-name': 'getTagQuestions',
                   'x-definition-name': 'topicTag',
                   'x-timezone': 'Asia/Shanghai',
                   'Origin': 'https://leetcode-cn.com',
                   'Referer': 'https://leetcode-cn.com/problems/' + titleSlug + '/',
                   'Connection': 'keep-alive',
                   'Cookie': ck,
                   'TE': 'Trailers'}
        data = json.dumps(data_temp)
        try:
            response = requests.post(url=url, headers=headers, data=data)
            result = json.loads(response.text)
            translatedContent = result['data']['question']['translatedContent']
            difficulty = result['data']['question']['difficulty']
            translatedTitle = result['data']['question']['translatedTitle']
            problem_url = "https://leetcode-cn.com/problems/" + result['data']['question']['titleSlug']
            fieldir = dir.MakeDir.path + "\\" + i + "\\" + translatedTitle + ".txt"
            fp = open(fieldir, 'w', encoding="utf-8")
            fp.write("translatedContent:\n" + str(translatedContent) + '\n')
            fp.write('\n难度：' + str(difficulty) + '\n')
            fp.write("\n链接：" + str(problem_url))
            fp.close()
            print("Successfully get " + titleSlug)
        except:
            print(titleSlug + "-爬取失败！！！")
    print(i + "标签线程爬取完毕")
