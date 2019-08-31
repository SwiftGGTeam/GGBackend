from app.models import Post, Category

from django.db import models
from datetime import datetime
import re
import json
import requests

POST_LIST_API_URL = "https://api.github.com/repos/SwiftGGTeam/source/contents/_posts?ref=master"

TEST_TOKEN = "adc33ddb0505ece9a9fdb3b58327871fa49c6a15"


def excutor_post() -> list:
    # TEST_TOKEN = input("private token: ")
    # 请求列表
    headers = {
        'Authorization': "token " + TEST_TOKEN,
        'cache-control': "no-cache",
    }
    requests.adapters.DEFAULT_RETRIES = 10
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


def resolve_header(raw: str) -> dict:
    # 模拟 raw 文件
    # r = requests.get("https://raw.githubusercontent.com/SwiftGGTeam/source/master/_posts/20151029_list-comprehensions-and-performance-with-swift.md")
    # raw = str(r.content, encoding="utf-8")
    info = {}
    preface = ''
    preface_start = False

    for line in raw.split("\n"):
        if not line:
            continue
        # print(line)
        # 匹配 title
        title_re_test = re.match(r'^title:.*?"(.+?)".*?$', line)
        if title_re_test:
            info['title'] = title_re_test.group(1)

        # 匹配时间
        date_re_test = re.match(r'^date:.*?(\d{4}-\d{1,2}-\d{1,2}).*?$', line)
        if date_re_test:
            info['date'] = date_re_test.group(1)

        # 匹配 permalink
        category_re_test = re.match(r'^permalink:(.+)$', line)
        if category_re_test:
            info['permalink'] = category_re_test.group(1).strip()

        # 匹配 categories
        categories_re_test = re.match(r'^categories:.*?\[(.*?)\].*?$', line)
        if categories_re_test:
            categories = categories_re_test.group(1).split(',')
            if len(categories) > 0 and len(categories[0]) > 0:
                info['category'] = categories[0]

        # 匹配 more
        if re.match(r'^\s*<\s*!-+\s*more\s*-+\s*>\s*$', line):
            # 移除最后一个 \n
            info['preface'] = preface[:-1]
            break

        if preface_start:
            preface += line + '\n'

        # 匹配正文开始
        if re.match(r'^\s*<\s*!-+\s*此处开始正文\s*-+\s*>\s*$', line):
            preface_start = True

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
    if 'category' in post.keys():
        print('category: %s' % post['category'])


def bulk_insert(res):
    flags = {}
    list_to_insert = list()
    for post_dic in res:
        if not 'title' in post_dic.keys():
            continue
        if post_dic['title'] in flags.keys():
            continue
        flags[post_dic['title']] = True
        list_to_insert.append(make_post(post_dic))
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
        if post_dic['title'] in flags.keys():
            continue
        flags[post_dic['title']] = True
        list_to_update.append(make_post(post_dic))
    Post.objects.bulk_update(list_to_update, ['body', 'category', 'preface'])


def make_post(post_dict: dict):
    try:
        post = Post.objects.get(title=post_dict['title'])
    except Post.DoesNotExist:
        post = Post(title=post_dict['title'])

    if 'date' in post_dict.keys():
        post.published_at = datetime.strptime(post_dict['date'], "%Y-%m-%d")
    if 'html_url' in post_dict.keys():
        post.html_url = post_dict['html_url']
    if 'category' in post_dict.keys():
        try:
            category = Category.objects.get(name=post_dict['category'])
        except Category.DoesNotExist:
            category = Category(name=post_dict['category'])
            category.save()
        post.category = category
    if 'preface' in post_dict.keys():
        post.preface = post_dict['preface']

    post.body = post_dict['body']
    return post


if __name__ == "__main__":
    # res = excutor_post()
    print("测试爬虫")
    res = resolve_header(None)
    print(res)
    # resolve_body(None)
    pass
