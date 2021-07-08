import configparser
import os
import shutil
import sys
from common.logs import Logger
import psycopg2
import yaml


def get_config(path, name):
    cf = configparser.ConfigParser()
    dir_path = cf.read(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + path)
    cf.read(dir_path)
    items = dict(cf.items(name))
    return items


def yaml_load(path):
    """
    封装yaml文件的解析
    :param path: yaml文件路径
    :return:python对象
    """
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(dir_path + path, encoding='UTF-8') as f:
        return yaml.safe_load(f)


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    try:
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    except FileNotFoundError:
        print('目录不存在')


def clear_file(filepath):
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(dir_path + filepath, 'r+') as f:
        f.truncate()


log = Logger()


def my_assert(ass, *args):
    """
    封装断言+日志
    """
    try:
        exec(ass)
        log.logger.info(
            '{}: 用例通过 \t 实际: {} \t 预期: {}'.format(sys._getframe().f_back.f_code.co_name, args[0], args[1]))
    except AssertionError:
        log.logger.error(
            '{}: 断言失败 \t 实际: {} \t 预期: {}'.format(sys._getframe().f_back.f_code.co_name, args[0], args[1]))
        raise AssertionError('断言失败')


class PgSql:
    def __init__(self):
        host = get_config('/config.ini', 'all_config')['host']
        self.conn = psycopg2.connect(database="hulattp", user="postgres", password="hb2gZVUos7vosADO", host=host,
                                     port="5432")

    def clear_home(self):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM homepage WHERE title like '%自动化%';")
        # self.cur.fetchall()  # 检索查询结果
        self.conn.commit()
        self.conn.close()

    def clear_label(self):
        cur = self.conn.cursor()
        cur.execute(
            "DELETE FROM label WHERE ID IN (SELECT ID FROM label RIGHT JOIN ( SELECT label_id FROM label_group_to_label WHERE group_id = ( SELECT ID FROM label_group WHERE NAME = '自动化标签组' ) ) AS son ON ID = label_id);")  # 先删标签
        cur.execute(
            "DELETE FROM label_group_to_label WHERE group_id = (SELECT id FROM label_group WHERE name='自动化标签组');")  # 再删关系
        cur.execute("DELETE FROM label_group WHERE name='自动化标签组';")  # 再删标签组
        cur.execute("DELETE FROM label WHERE name like '%自动化%';")  # 可能没有删干净，再删一次
        cur.execute("delete from nav_bar where NAME like '%自动化%';")  # 删除推荐页导航栏
        self.conn.commit()
        self.conn.close()

    def clear_topic(self):
        content_id = []
        cur = self.conn.cursor()
        # 根据话题名称获取所有content_id
        cur.execute(
            "select content_id from content_to_topic where topic_id in (select id from topic where title like '%自动化%');")
        rows = cur.fetchall()
        for i in rows:
            content_id.append(i[0])
        # 删除content_to_topic对应关系
        cur.execute("delete from content_to_topic where topic_id in (select id from topic where title like '%自动化%');")
        # 删除content
        for i in content_id:
            cur.execute("delete from content where id={};".format(i))

        # 删除topic_to_topic_group对应关系
        cur.execute(
            "delete from topic_to_topic_group where topic_id in (select id from topic where title like '%自动化%');")
        cur.execute(
            "delete from topic_to_topic_group where group_id in (select id from topic_group where title like '%自动化%');")
        # 删除author_follow_topic关注关系
        cur.execute(
            "delete from author_follow_topic where topic_id in (select id from topic where title like '%自动化%');")
        # 删除话题
        cur.execute("delete from topic where title like '%自动化%';")
        # 删除话题组
        cur.execute("delete from topic_group where title like '%自动化%';")

        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    PgSql().clear_home()
