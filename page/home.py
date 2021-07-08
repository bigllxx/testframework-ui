from common.base_page import BasePage
from selenium.webdriver.common.by import By


class Home(BasePage):
    # 一级菜单"首页管理"

    def search(self, locate_type: int = None, jump_type: int = None, shelve_type: int = None):
        """
        搜索功能
        :param locate_type: 2 banner，3 grid_cell，4 grid_cell_for_recommend，5 weekly_hottest
        :param jump_type: 2 label，3 label_group，4 post，5 snack，6 video，7 checklist，8 url
        :param shelve_type: 2 上架，3 即将上架，4 上架或即将上架，5 已下架
        :return: list 第一个搜索结果的位置类型和上架状态
        """
        self.log_name = 'Home.search'
        _elem = {
            '位置类型': 'span[title="位置类型"]',
            '跳转类型': 'span[title="跳转类型"]',
            '上架状态': 'span[title="上架状态"]',
            '类型选择': 'span.select2-results>ul>li',
            '搜索按钮': '//button[text()="Search"]',
            '搜索结果位置类型': 'td.field-position_type',
        }
        self.find(locator=_elem['位置类型']).click()
        self.finds(locator=_elem['类型选择'])[locate_type].click()
        self.find(locator=_elem['跳转类型']).click()
        self.finds(locator=_elem['类型选择'])[jump_type].click()
        self.find(locator=_elem['上架状态']).click()
        self.finds(locator=_elem['类型选择'])[shelve_type].click()
        self.find(By.XPATH, _elem['搜索按钮']).click()
        try:
            res = self.finds(locator=_elem['搜索结果位置类型'])[0].text
        except TypeError:
            return None
        else:
            return res

    def add_homepage(self, locate_type: int = None, jump_type: int = None, image_url: str = None, title: str = None):
        """
        新增广告位
        :param locate_type: 位置类型 0 banner，1 grid_cell，2 grid_cell_for_recommend，3 weekly_hottest
        :param jump_type: 跳转类型 0 文章，1 好物，2 视频，3 清单，4 标签，5 标签组
        :param image_url: 图片地址
        :param title: 标题
        :return:
        """
        self.log_name = 'Home.add_homepage'
        _elem = {
            '新增按钮': 'a[href="/en/admin/ttp/homepage/add/"]',
            '位置类型': 'span[id="select2-id_type-container"]',
            "位置类型选择": 'ul[id="select2-id_type-results"]>li',
            '跳转类型': 'span[id="select2-id_route_type-container"]',
            '跳转类型选择': 'ul[id="select2-id_route_type-results"]>li',
            '内容': 'div.form-group',
            '内容选择': 'li[class="select2-results__option select2-results__option--highlighted"]',
            '图片': 'input[id="id_image"]',
            '标题': 'input[id="id_title"]',
            '保存': 'input[name="_save"]',
        }
        self.find(locator=_elem['新增按钮']).click()
        self.find(locator=_elem['位置类型']).click()
        self.finds(locator=_elem['位置类型选择'])[locate_type].click()
        self.find(locator=_elem['跳转类型']).click()
        self.finds(locator=_elem['跳转类型选择'])[jump_type].click()
        if jump_type == 0:
            self.finds(locator=_elem['内容'])[3].click()
        elif jump_type == 1:
            self.finds(locator=_elem['内容'])[4].click()
        elif jump_type == 2:
            self.finds(locator=_elem['内容'])[5].click()
        elif jump_type == 3:
            self.finds(locator=_elem['内容'])[6].click()
        elif jump_type == 4:
            self.finds(locator=_elem['内容'])[7].click()
        elif jump_type == 5:
            self.finds(locator=_elem['内容'])[8].click()
        elif jump_type == 6:
            self.finds(locator=_elem['内容'])[9].click()
        self.find(locator=_elem['内容选择']).click()  # 选择第一个内容
        self.find(locator=_elem['图片']).send_keys(image_url)
        self.find(locator=_elem['标题']).send_keys(title)
        self.find(locator=_elem['保存']).click()
        return self.driver.current_url

    def down_shelve(self, locate_type):
        """
        下架，下架第第一一个广告位
        :param locate_type: 位置类型 2 banner，3 grid_cell，4 grid_cell_for_recommend，5 weekly_hottest
        :return: 被下架广告位的标题
        """
        self.log_name = 'Home.down_shelve'
        _elem = {
            '位置类型': 'span[title="位置类型"]',
            '上架状态': 'span[title="上架状态"]',
            '类型选择': 'span.select2-results>ul>li',
            '搜索按钮': '//button[text()="Search"]',
            '内容选中': 'input[name="_selected_action"]',
            '操作框': 'select[name="action"]',
            '立即下架': 'option[value="downshelve_rightnow"]',
            'GO': 'button[title = "Run the selected action"]'
        }
        self.find(locator=_elem['位置类型']).click()
        self.finds(locator=_elem['类型选择'])[locate_type].click()
        self.find(locator=_elem['上架状态']).click()
        self.finds(locator=_elem['类型选择'])[2].click()  # 选择上架状态
        self.find(By.XPATH, _elem['搜索按钮']).click()
        res_title = self.finds(locator='td.field-title_short')[0].text
        self.finds(locator=_elem['内容选中'])[0].click()  # 选中第一条内容
        self.find(locator=_elem['操作框']).click()
        self.find(locator=_elem['立即下架']).click()
        self.find(locator=_elem['GO']).click()
        return res_title

    def update_homepage(self, locate_type, title):
        """
        编辑广告位
        :param locate_type:
        :param title:
        :return:
        """
        self.log_name = 'Home.update_homepage'
        _elem = {
            '列表图片': 'th.field-logo_image>a>img',
            '内容标题': 'td.field-title_short',
            '位置类型': 'span[id="select2-id_type-container"]',
            "位置类型选择": 'ul[id="select2-id_type-results"]>li',
            '标题': 'input[id="id_title"]',
            '保存': 'input[name="_save"]',
        }
        self.finds(locator=_elem['列表图片'])[0].click()
        self.find(locator=_elem['位置类型']).click()
        self.finds(locator=_elem['位置类型选择'])[locate_type].click()
        self.find(locator=_elem['标题']).clear()
        self.find(locator=_elem['标题']).send_keys(title)
        self.find(locator=_elem['保存']).click()
        a = self.finds(locator=_elem['内容标题'])[0].text
        return a
