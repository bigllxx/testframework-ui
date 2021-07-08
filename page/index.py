from selenium.webdriver.common.by import By
from common.base_page import BasePage
from page.home import Home
from page.content import Content
from page.label_navigation import Label, LabelGroup, Navigation
from common.action import get_config
from page.topic import Topic, TopicGroup


class Access(BasePage):
    # setup class，access the link and login.
    cf = get_config('/config.ini', 'all_config')
    _base_url = cf['url']
    _username = cf['username']
    _password = cf['password']

    _location = {
        '用户名': 'input[name="username"]',
        '密码': 'input[name="password"]',
        '登录按钮': '//button[text()="Log in"]',
    }

    def login(self):
        self.log_name = 'Access.login'
        self.find(locator=self._location['用户名']).send_keys(self._username)
        self.find(locator=self._location['密码']).send_keys(self._password)
        self.find(By.XPATH, self._location['登录按钮']).click()
        return Index(self.driver)


class Index(BasePage):
    # diver 将driver分发给各一级菜单
    _location = {
        '首页管理': '//p[text()="首页管理"]',
        '好物管理': '//p[text()="好物管理"]',
        '文章管理': '//p[text()="文章管理"]',
        '视频管理': '//p[text()="视频管理"]',
        '文章页导航管理': '//p[text()="文章页导航管理"]',
        '标签/栏目/二级标签': '//p[text()="标签/栏目/二级标签"]',
        '标签组/板块/一级标签': '//p[text()="标签组/板块/一级标签"]',
        '话题': '//p[text()="话题"]',
        '话题组': '//p[text()="话题组"]',
        '话题讨论管理': '//p[text()="话题讨论管理"]',
    }

    def up_home(self):
        self.log_name = 'Index.up_home'
        self.find(by=By.XPATH, locator=self._location['首页管理']).click()
        return Home(self.driver)

    def up_snack(self):
        self.log_name = 'Index.up_snack'
        self.find(by=By.XPATH, locator=self._location['好物管理']).click()
        return Content(self.driver)

    def up_post(self):
        self.log_name = 'Index.up_post'
        self.find(by=By.XPATH, locator=self._location['文章管理']).click()
        return Content(self.driver)

    def up_video(self):
        self.log_name = 'Index.up_video'
        self.find(by=By.XPATH, locator=self._location['视频管理']).click()
        return Content(self.driver)

    def up_navigation(self):
        self.log_name = 'Index.up_navigation'
        self.find(by=By.XPATH, locator=self._location['文章页导航管理']).click()
        return Navigation(self.driver)

    def up_label(self):
        self.log_name = 'Index.up_label'
        self.find(by=By.XPATH, locator=self._location['标签/栏目/二级标签']).click()
        return Label(self.driver)

    def up_label_group(self):
        self.log_name = 'Index.up_label_group'
        self.find(by=By.XPATH, locator=self._location['标签组/板块/一级标签']).click()
        return LabelGroup(self.driver)

    def up_topic(self):
        self.log_name = 'Index.up_topic'
        self.find(by=By.XPATH, locator=self._location['话题']).click()
        return Topic(self.driver)

    def up_topic_group(self):
        self.log_name = 'Index.up_topic_group'
        self.find(by=By.XPATH, locator=self._location['话题组']).click()
        return TopicGroup(self.driver)

    def up_topic_discuss(self):
        self.log_name = 'Index.up_topic_discuss'
        self.find(by=By.XPATH, locator=self._location['话题讨论管理']).click()
        return Content(self.driver)
