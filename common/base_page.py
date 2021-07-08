import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logs import Logger


class BasePage:
    _base_url = ""
    driver = None
    log = Logger('Page')
    log_name = None

    def __init__(self, driver: WebDriver = None):
        """
        driver的封装
        :param driver:
        """
        if driver is None:
            # login_page页面会使用这个
            self.driver = webdriver.Chrome(executable_path='/Users/bigllxx/other/selenium/chromedriver')
            # self.driver.maximize_window()
        else:
            # 其他页面需要用这个方法
            self.driver = driver
            self.driver.implicitly_wait(3)
        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by=By.CSS_SELECTOR, locator=None):
        """
        定位方法及显示等待的封装
        :param by: 定位方法 如 By.CSS_SELECTOR
        :param locator: 定位元素
        :return:
        """

        el = (by, locator)
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(el))
        except TimeoutException:
            self.log.logger.error('{} - 定位失败：{}'.format(self.log_name, locator))
            return False
        else:
            self.log.logger.info('{} - 定位成功：{}'.format(self.log_name, locator))
            return self.driver.find_element(by, locator)

    def finds(self, by=By.CSS_SELECTOR, locator=None):
        """
        定位方法及显示等待的封装
        :param by: 定位方法 如 By.CSS_SELECTOR
        :param locator: 定位元素
        :return:
        """
        el = (by, locator)
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(el))
        except (TimeoutException, TypeError):
            self.log.logger.error('{} - 定位失败：{}'.format(self.log_name, locator))
            # self.log.logger.warn('{} - 定位失败：{}'.format(inspect.stack()[1][4][0], locator))
            return False
        else:
            self.log.logger.info('{} - 定位成功：{}'.format(self.log_name, locator))
            return self.driver.find_elements(by, locator)

    def set_records(self, css):
        """
        re 正则模块 返回记录总条数
        :param css: 定位
        :return: 总条数 int
        """
        ob = self.driver.find_element(By.CSS_SELECTOR, css).text
        res = re.search(r'共(.*)条', ob)
        return res.group(1)