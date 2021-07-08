import time
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from common.all_api import recommend_navbar_api


class Label(BasePage):

    def add_label(self, label_name, back_image):
        self.log_name = 'LabelNavigation.add_label'
        _elem = {
            '新增标签': 'div.col-12.col-sm-4>a',
            '标签名称': 'input[id="id_name"]',
            '背景图': 'input[id="id_bg_pic"]',
            '保存': 'input[name="_save"]',
            '返回结果': 'td.field-name',
        }
        self.find(locator=_elem['新增标签']).click()
        self.find(locator=_elem['标签名称']).send_keys(label_name)
        self.find(locator=_elem['背景图']).send_keys(back_image)
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['返回结果'])[0].text
        return res

    def search_label(self, label_name):
        self.log_name = 'LabelNavigation.search_label'
        _elem = {
            '搜索框': 'input[id="searchbar"]',
            '标签名称': '//button[text()="Search"]',
            '返回结果': 'td.field-name',
        }
        self.find(locator=_elem['搜索框']).send_keys(label_name)
        self.find(by=By.XPATH, locator=_elem['标签名称']).click()
        res = self.finds(locator=_elem['返回结果'])[0].text
        return res

    def update_label(self, label_name, back_image):
        self.log_name = 'LabelNavigation.update_label'
        _elem = {
            '列表图片': 'th.field-bg_pic_image>a>img',
            '内容标题': 'td.field-name',
            '标签名称': 'input[id="id_name"]',
            '背景图': 'input[id="id_bg_pic"]',
            '保存': 'input[name="_save"]',
        }
        self.finds(locator=_elem['列表图片'])[0].click()
        self.find(locator=_elem['标签名称']).clear()
        self.find(locator=_elem['标签名称']).send_keys(label_name)
        self.find(locator=_elem['背景图']).clear()
        self.find(locator=_elem['背景图']).send_keys(back_image)
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['内容标题'])[0].text
        return res


class LabelGroup(BasePage):

    def add_label_group(self, label_name, back_image):
        self.log_name = 'LabelGroup.add_label_group'
        _elem = {
            '新增标签': 'div.col-12.col-sm-4>a',
            '标签名称': 'input[id="id_name"]',
            '背景图': 'input[id="id_bg_pic"]',
            '保存': 'input[name="_save"]',
            '返回结果': 'td.field-name',
        }
        self.find(locator=_elem['新增标签']).click()
        self.find(locator=_elem['标签名称']).send_keys(label_name)
        self.find(locator=_elem['背景图']).send_keys(back_image)
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['返回结果'])[0].text
        return res

    def update_label_group(self):
        self.log_name = 'LabelNavigation.update_label_group'
        _elem = {
            '列表图片': 'th.field-bg_pic_image>a>img',
            '内容标题': 'td.field-name',
            '标签组关联': 'a[aria-controls="标签组关联-tab"]',
            '标签关系': '//a[text()="Add another 板块-栏目关系"]',
            '标签选择': 'span[class="select2-selection select2-selection--single"]',
            '标签确认': 'li.select2-results__option',
            '保存': 'input[name="_save"]',
            '标签/栏目/二级标签': '//p[text()="标签/栏目/二级标签"]',
            '所属板块': 'td.field-belongs_to>p'
        }
        self.finds(locator=_elem['列表图片'])[0].click()
        self.find(locator=_elem['标签组关联']).click()
        for i in range(3):
            self.find(by=By.XPATH, locator=_elem['标签关系']).click()
        for i in range(3):
            self.finds(locator=_elem['标签选择'])[i].click()
            time.sleep(1)
            self.finds(locator=_elem['标签确认'])[i].click()
            time.sleep(1)
        self.find(locator=_elem['保存']).click()
        self.find(by=By.XPATH, locator=_elem['标签/栏目/二级标签']).click()
        res = self.find(locator=_elem['所属板块']).text
        return res


class Navigation(BasePage):

    def add_navigation(self, navigation_name, navigation_description, navigation_type):
        self.log_name = 'LabelNavigation.add_navigation'
        _elem = {
            '新增按钮': 'div.col-12.col-sm-4>a',
            '名称': 'input[id="id_name"]',
            '描述': 'textarea[id="id_description"]',
            '标签组': 'input[id="id_point_to_1"]',
            '展开标签': 'span.select2-selection__arrow',
            '标签': 'li.select2-results__option',
            '保存': 'input[name="_save"]',
            '返回结果': 'td.field-name',
        }
        self.find(locator=_elem['新增按钮']).click()
        self.find(locator=_elem['名称']).send_keys(navigation_name)
        self.find(locator=_elem['描述']).send_keys(navigation_description)
        if navigation_type == '标签组':
            self.find(locator=_elem['标签组']).click()
            self.finds(locator=_elem['展开标签'])[1].click()
        else:
            self.finds(locator=_elem['展开标签'])[0].click()
        time.sleep(1)
        self.finds(locator=_elem['标签'])[0].click()
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['返回结果'])[-1].text
        return res

    def update_navigation(self, navigation_name, navigation_description, navigation_type):
        self.log_name = 'LabelNavigation.update_navigation'
        _elem = {
            '内容id': 'th.field-id>a',
            '内容标题': 'td.field-name',
            '名称': 'input[id="id_name"]',
            '描述': 'textarea[id="id_description"]',
            '选择标签': 'input[id="id_point_to_0"]',
            '标签组': 'input[id="id_point_to_1"]',
            '展开标签': 'span.select2-selection__arrow',
            '标签': 'li.select2-results__option',
            '保存': 'input[name="_save"]',
        }
        self.finds(locator=_elem['内容id'])[-1].click()
        self.find(locator=_elem['名称']).clear()
        self.find(locator=_elem['名称']).send_keys(navigation_name)
        self.find(locator=_elem['描述']).clear()
        self.find(locator=_elem['描述']).send_keys(navigation_description)
        if navigation_type == '标签组':
            self.find(locator=_elem['标签组']).click()
            self.finds(locator=_elem['展开标签'])[1].click()
        else:
            self.find(locator=_elem['选择标签']).click()
            self.finds(locator=_elem['展开标签'])[0].click()
        time.sleep(1)
        self.finds(locator=_elem['标签'])[0].click()
        self.find(locator=_elem['保存']).click()
        res = self.finds(locator=_elem['内容标题'])[-1].text
        return res

    def down_navigation(self):
        self.log_name = 'LabelNavigation.down_navigation'
        _elem = {
            '选中': 'input[name="_selected_action"]',
            '展开操作': 'select[name="action"]',
            '立即下架': 'option[value="downshelve_rightnow"]',
            'GO': 'button[title="Run the selected action"]',
            '名称': 'td.field-name',
        }
        res_b = recommend_navbar_api()
        self.finds(locator=_elem['选中'])[-1].click()
        self.find(locator=_elem['展开操作']).click()
        self.find(locator=_elem['立即下架']).click()
        self.find(locator=_elem['GO']).click()
        res_a = recommend_navbar_api()
        return res_b == res_a
