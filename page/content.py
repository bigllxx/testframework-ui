import inspect
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class Content(BasePage):

    def search(self, audit_state: int = None, shelve_state: int = None):
        """
        搜索
        :param audit_state: 2 正常，4 等待手动审核，7 手动审核拒绝
        :param shelve_state: 2 上架，3 即将上架，4 已下架
        :return: 审核状态
        """
        self.log_name = 'Content.search'
        _elem = {
            '审核状态': 'span[title="审核状态"]',
            '上架状态': 'span[title="上架状态"]',
            '状态选择': 'li.select2-results__option',
            '搜索按钮': '//button[text()="Search"]',
            '搜索结果审核状态': 'td.field-state',
            '搜索结果上架状态': 'td.field-upshelve_status',
        }
        self.find(locator=_elem['审核状态']).click()
        self.finds(locator=_elem['状态选择'])[audit_state].click()
        if inspect.stack()[1][3] != 'test_topic_discuss_search':
            self.find(locator=_elem['上架状态']).click()
            self.finds(locator=_elem['状态选择'])[shelve_state].click()
        self.find(By.XPATH, _elem['搜索按钮']).click()
        try:
            res = self.finds(locator=_elem['搜索结果审核状态'])[0].text
        except TypeError:
            return None
        else:
            return res

    def refuse_audit(self):
        """
        拒绝审核第一篇
        :return: 审核状态
        """
        self.log_name = 'Content.refuse_audit'
        _elem = {
            '内容选中': 'input[name="_selected_action"]',
            '操作框': 'select[name="action"]',
            '拒绝审核': 'option[value="reject_published"]',
            'GO': 'button[title = "Run the selected action"]',
            '搜索结果审核状态': 'td.field-state',
        }
        self.finds(locator=_elem['内容选中'])[0].click()
        self.find(locator=_elem['操作框']).click()
        self.find(locator=_elem['拒绝审核']).click()
        self.find(locator=_elem['GO']).click()
        res = self.finds(locator=_elem['搜索结果审核状态'])[0].text
        return res

    def agree_audit(self):
        """
        通过审核第一篇
        :return: 审核状态
        """
        self.log_name = 'Content.agree_audit'
        _elem = {
            '内容选中': 'input[name="_selected_action"]',
            '操作框': 'select[name="action"]',
            '通过审核': 'option[value="make_published"]',
            'GO': 'button[title = "Run the selected action"]',
            '搜索结果审核状态': 'td.field-state',
        }
        self.finds(locator=_elem['内容选中'])[0].click()
        self.find(locator=_elem['操作框']).click()
        self.find(locator=_elem['通过审核']).click()
        self.find(locator=_elem['GO']).click()
        res = self.finds(locator=_elem['搜索结果审核状态'])[0].text
        return res

    def preview(self, audit_state):
        """
        预览
        :param audit_state: 审核状态
        :return:
        """
        self.log_name = 'Content.preview'
        _elem = {
            '标题': 'td.field-title',
            '话题': 'td.field-topic',
            '审核状态': 'span[title="审核状态"]',
            '状态选择': 'li.select2-results__option',
            '搜索按钮': '//button[text()="Search"]',
            '预览': '//a[text()="预览"]',
            '头像': 'img._2MPl-uOjTQqEjiB7-jYa9c',
            '当前内容无法查看': '//h2[text()="当前内容无法查看~"]'
        }
        self.find(locator=_elem['审核状态']).click()
        self.finds(locator=_elem['状态选择'])[audit_state].click()
        self.find(By.XPATH, _elem['搜索按钮']).click()
        if inspect.stack()[1][3] == 'test_topic_discuss_preview':
            exc_title = '呼啦宝贝-' + self.finds(locator=_elem['话题'])[0].text  # 获取当前内容title
        else:
            exc_title = '呼啦宝贝-' + self.finds(locator=_elem['标题'])[0].text  # 获取当前内容title
        self.finds(by=By.XPATH, locator=_elem['预览'])[0].click()  # 打开了新的标签页
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到第2个标签页
        res_title = self.driver.title  # 获取页面title
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到第1个标签页
        return exc_title == res_title
