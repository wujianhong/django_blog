#!/usr/bin/python3
# coding: utf-8
import datetime
import os
import sqlite3
import platform
from pprint import pprint

import xpinyin
from bs4 import BeautifulSoup
from django.utils.text import slugify

file_db = os.path.join(os.getcwd(), 'db.sqlite3')
# path_txt = '/root/code/python3/txt'
path_txt = r'E:\PycharmProjects\blog_move\txt'

pinyin = xpinyin.Pinyin()


def clear_title(title):
    for d in '，.() ':
        title = str(title).replace(d, '')
    return title.replace('_', ' ')


def clear_time(date_time):
    y, m, d, h, mm, s = str(date_time).split('_')
    return datetime.datetime(int(y), int(m), int(d), int(h), int(mm), int(s))


def clear_content(content):
    if '<' in content:
        soup = BeautifulSoup(content, 'html.parser')
        return soup.get_text()
    else:
        return content


def gen_slug(title):
    title = pinyin.get_pinyin(title)
    return slugify(title).replace('_', '-').replace(' ', '-')


def fetch(result):
    total = []

    for index, item in enumerate(result):
        title = clear_title(item[1])
        slug = gen_slug(title)
        category = item[2]
        date_time = clear_time(item[3])
        content = clear_content(item[4])
        total.append([str(index + 1), title, slug, category, date_time, content])
    return total


def insert_data(items):
    sql = """
    insert into blog_blog(id, title, slug, category, date_time, content) values (?, ?, ?, ?, ?, ?)
    """

    conn = sqlite3.connect(file_db)
    cur = conn.cursor()

    cur.executemany(sql, items)
    conn.commit()
    conn.close()


def get_category_os(category):
    if platform.system() == 'Windows':
        slash = '\\'
    else:
        slash = '/'
    return category.split(slash)[-1]


def read_each_text_file(txt):
    category = txt.split('-')[0]
    category = get_category_os(category)
    title = txt.split('-')[1]
    date_time = txt.split('-')[2].split('.')[0]

    with open(txt, encoding='utf-8') as f:
        content = f.read()

    return [title, category, date_time, content]


def read_source():
    items = []
    root, dirs, files = next(os.walk(path_txt))
    for d in dirs:
        for sub_root, sub_dirs, sub_files in os.walk(os.path.join(root, d)):
            for sf in sub_files:
                item = read_each_text_file(os.path.join(sub_root, sf))
                items.append(item)
    return items


def main():
    items = read_source()

    item_list = []
    for index, data in enumerate(items):
        item_list.append([index + 1] + data)

    result = fetch(item_list)
    pprint(result)

    insert_data(result)


if __name__ == '__main__':
    main()
