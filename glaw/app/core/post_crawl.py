from app.models import Post

from datetime import datetime
import requests
import re
import json

POST_LIST_API_URL = "https://gateway.github.com/repos/SwiftGGTeam/source/contents/_posts?ref=master"
TEST_TOKEN = "2cd2424bd7018f8a33a0fac5255343a3dbef13bc"
post_ret = []


def excutor_post() -> list:
    TEST_TOKEN = input("private token: ")
    # 请求列表
    headers = {
        'Authorization': "token " + TEST_TOKEN,
        'cache-control': "no-cache",
    }
    r = requests.get(POST_LIST_API_URL, headers=headers)
    data_content = r.content
    post_list = json.loads(s=data_content)
    print(post_list)
    ret = []
    if type(post_list) is list:
        for post in post_list:
            if type(post) is dict and 'download_url' in post.keys():
                raw_req = requests.get(post['download_url'])
                raw = str(raw_req.content, encoding="utf-8")
                info = dict(resolve_header(raw))
                info.update(resolve_body(raw))
                ret.append(info)
                # 测试输出
                ptr_post_dict(info)
    return ret


def resolve_header(raw) -> dict:
    # 模拟 raw 文件
    # r = requests.get("https://raw.githubusercontent.com/SwiftGGTeam/source/master/_posts/20151029_list-comprehensions-and-performance-with-swift.md")
    # raw = str(r.content, encoding="utf-8")
    info = {}
    for line in raw.split("\n"):
        # print(line)
        # 匹配 title
        title_re_test = re.match(r'^title:.*?"(.+?)".*?$', line)
        if title_re_test:
            info['title'] = title_re_test.group(1)
        # 匹配时间
        date_re_test = re.match(r'^date:.*?(\d{4}-\d{2}-\d{2}).*?$', line)
        if date_re_test:
            info['date'] = date_re_test.group(1)
        # 匹配 permalink
        category_re_test = re.match(r'^permalink:(.+)$', line)
        if category_re_test:
            info['permalink'] = category_re_test.group(1).strip()
        # 匹配结束
        body_start_re_test = re.match(r'^---.*?$', line)
        if body_start_re_test:
            break
    # 拼 web_url
    if "date" in info.keys() and "permalink" in info.keys():
        date_split = info['date'].split('-')
        if len(date_split) == 3:
            url_templete = "https://swift.gg/{d1}/{d2}/{d3}/{d4}"
            info['html_url'] = url_templete.format(d1=date_split[0],
                                                   d2=date_split[1],
                                                   d3=date_split[2],
                                                   d4=info['permalink'])

    return info


def resolve_body(raw) -> dict:
    # 模拟 raw 文件
    # r = requests.get("https://raw.githubusercontent.com/SwiftGGTeam/source/master/_posts/20151029_list-comprehensions-and-performance-with-swift.md")
    # raw = str(r.content, encoding="utf-8")
    info, is_body_line = {}, False
    info['body'] = ""
    for line in raw.split("\n"):
        if is_body_line:
            info['body'] += line + '\n'
            continue
        body_start_re_test = re.match(r'^---.*?$', line)
        if body_start_re_test:
            is_body_line = True
    return info


def ptr_post_dict(post: dict):
    print('\n')
    if 'title' in post.keys():
        print("标题：%s" % post['title'])
    if 'date' in post.keys():
        print("发布日期：%s" % post['date'])
    if 'permalink' in post.keys():
        print("后缀：%s" % post['permalink'])
    if 'html_url' in post.keys():
        print("html：%s" % post['html_url'])


def bulk_insert():
    list_to_insert = list()
    for post_dic in post_ret:
        if not 'title' in post_dic.keys():
            continue
        post = Post(title=post['title'])
        if 'date' in post_dic.keys():
            post.published_at = datetime.strptime(post_dic['date'], "%Y-%m-%d")
        if 'html_url' in post_dic.keys():
            post.html_url = post_dic['html_url']
        list_to_insert.append(post)
    # BD
    Post.objects.bulk_create(list_to_insert)


def bulk_update(res):
    """
    爬虫更新策略
    :param res: 传入 excutor_post 爬虫结果
    :return:
    """
    flags = {}
    list_to_update = list()
    for post_dic in res:
        if not 'title' in post_dic.keys():
            continue
        if post['title'] in flags.keys():
            continue
        flags[post['title']] = True
        post = Post.objects.get(title=post['title'])
        if 'date' in post_dic.keys():
            post.published_at = datetime.strptime(post_dic['date'], "%Y-%m-%d")
        if 'html_url' in post_dic.keys():
            post.html_url = post_dic['html_url']
        list_to_update.append(post)
    Post.objects.bulk_update(list_to_update)

if __name__ == "__main__":
    excutor_post()
    print("测试爬虫")
    # resolve_header(None)
    # resolve_body(None)
    pass
