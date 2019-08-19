from bs4 import BeautifulSoup
import bs4
import requests
import re

USER_URL = "https://github.com/SwiftGGTeam/translation/blob/master/%E6%88%90%E5%91%98%E4%BB%8B%E7%BB%8D.md"


def excutor_user() -> list:
    r = requests.get(USER_URL)
    soup = BeautifulSoup(r.content, 'lxml')
    name_elements = soup.find_all(name="h2")

    ret = []

    for name_element in name_elements:
        ele_dic = {}
        full_name = name_element.text
        element = name_element.next_sibling
        ele_dic['full_name'] = full_name

        # 分组正则出 id
        p = re.compile('(.+)/(.+)')
        m = p.match(full_name)
        if m is None or len(m.groups()) < 2:
            ele_dic['id'] = full_name.strip()
        else:
            ele_dic['id'] = m.group(2).strip()

        while type(element) is bs4.element.NavigableString or \
            not (element.name == 'h2'):
            element = element.find_next_sibling()
            if element is None:
                break

            # 先判断是否为单字符串
            if type(element) is bs4.element.NavigableString:
                continue

            # 判断是否是头像
            if type(element) is bs4.element.Tag and \
                element.name == "p" and \
                len(element.find_all("img")) > 0:
                img = element.find_all("img")[0]
                ele_dic['avatar'] = img.attrs['src']
                continue

            # 判断个人介绍
            if type(element) is bs4.element.Tag and \
                element.name == "h4" and \
                "自我介绍" in element.text:
                intro = ""
                while not (type(element) is bs4.element.Tag and \
                            element.name == "h4" and \
                            "其他小伙伴贴的" in element.text):
                    if element is None:
                        break
                    if type(element) is bs4.element.Tag and \
                        element.name == "p":
                        intro += element.text
                    element = element.find_next_sibling()

                ele_dic['introduction'] = intro
                continue

            # 强制判断结束
            if 'avatar' in ele_dic.keys() and 'introduction' in ele_dic.keys():
                ret.append(ele_dic)
                break
    for item in ret:
        print(item)

    return ret

if __name__ == "__main__":
    excutor_user()
