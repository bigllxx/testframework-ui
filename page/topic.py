import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By


class Topic(BasePage):

    def add_topic(self, title, desc, max_hottest, image):
        self.log_name = 'Topic.add_topic'
        _elem = {
            '新增按钮': 'a[href="/en/admin/ttp/topic/add/"]',
            '标题': 'input[name="title"]',
            '描述': 'textarea[id="id_description"]',
            '最热': 'input[id="id_hot"]',
            '图片': 'input[id="id_image"]',
            '保存': 'input[name="_save"]',
            '返回结果': 'td.field-title',
        }
        self.find(locator=_elem['新增按钮']).click()
        self.find(locator=_elem['标题']).send_keys(title)
        self.find(locator=_elem['描述']).send_keys(desc)
        if max_hottest:
            self.find(locator=_elem['最热']).click()
        self.find(locator=_elem['图片']).send_keys(image)
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['返回结果'])[0].text
        return res

    def search_topic(self, title):
        self.log_name = 'Topic.search_topic'
        _elem = {
            '搜索框': 'input[id="searchbar"]',
            '话题名称': '//button[text()="Search"]',
            '返回结果': 'td.field-title',
        }
        self.find(locator=_elem['搜索框']).send_keys(title)
        self.find(by=By.XPATH, locator=_elem['话题名称']).click()
        res = self.finds(locator=_elem['返回结果'])[0].text
        return res

    def update_topic(self, title, desc, max_hottest, image):
        self.log_name = 'Topic.update_topic'
        _elem = {
            '列表图片': 'th.field-bg_pic_image>a>img',
            '列表标题': 'td.field-title',
            '话题标题': 'input[name="title"]',
            '描述': 'textarea[id="id_description"]',
            '最热': 'input[id="id_hot"]',
            '图片': 'input[id="id_image"]',
            '保存': 'input[name="_save"]',
        }
        self.finds(locator=_elem['列表图片'])[0].click()
        self.find(locator=_elem['话题标题']).clear()
        self.find(locator=_elem['话题标题']).send_keys(title)
        self.find(locator=_elem['描述']).clear()
        self.find(locator=_elem['描述']).send_keys(desc)
        if max_hottest:
            self.find(locator=_elem['最热']).click()
        self.find(locator=_elem['图片']).clear()
        self.find(locator=_elem['图片']).send_keys(image)
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['列表标题'])[1].text
        return res


class TopicGroup(BasePage):

    def add_topic_group(self, title, desc, image):
        self.log_name = 'Topic.add_topic_group'
        _elem = {
            '新增按钮': 'a[href="/en/admin/ttp/topicgroup/add/"]',
            '标题': 'input[name="title"]',
            '描述': 'textarea[id="id_description"]',
            '图片': 'input[id="id_image"]',
            '话题组关联': 'a[href="#话题组关联-tab"]',
            '新增关系': 'a.btn.btn-sm',
            '选择话题': 'span[aria-labelledby="select2-id_topictotopicgroup_set-0-topic_id-container"]',
            '添加话题': 'li.select2-results__option',
            '保存': 'input[name="_save"]',
            '返回结果': 'td.field-title',
        }
        self.find(locator=_elem['新增按钮']).click()
        self.find(locator=_elem['标题']).send_keys(title)
        self.find(locator=_elem['描述']).send_keys(desc)
        self.find(locator=_elem['图片']).send_keys(image)
        self.find(locator=_elem['话题组关联']).click()
        self.find(locator=_elem['新增关系']).click()
        self.find(locator=_elem['选择话题']).click()
        time.sleep(1)
        self.finds(locator=_elem['添加话题'])[0].click()
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['返回结果'])[-1].text
        return res

    def update_topic_group(self, title, desc, image):
        self.log_name = 'Topic.update_topic_group'
        _elem = {
            '列表图片': 'th.field-bg_pic_image>a>img',
            '列表标题': 'td.field-title',
            '标题': 'input[name="title"]',
            '描述': 'textarea[id="id_description"]',
            '图片': 'input[id="id_image"]',
            '保存': 'input[name="_save"]',
        }
        self.finds(locator=_elem['列表图片'])[-1].click()
        self.find(locator=_elem['标题']).clear()
        self.find(locator=_elem['标题']).send_keys(title)
        self.find(locator=_elem['描述']).clear()
        self.find(locator=_elem['描述']).send_keys(desc)
        self.find(locator=_elem['图片']).clear()
        self.find(locator=_elem['图片']).send_keys(image)
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['列表标题'])[-1].text
        return res

