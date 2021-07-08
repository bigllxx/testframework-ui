import allure
import pytest
from common.action import PgSql, yaml_load, my_assert
from page.index import Access
from common.all_api import *


@allure.feature('广告位相关')
class TestHome:
    data = yaml_load('/data/test_home_data.yaml')

    def setup_class(self):
        self.th = Access().login()
        try:
            PgSql().clear_home()
        except:
            print('清除数据失败')

    def teardown_class(self):
        self.th.driver.quit()

    @allure.story('新增广告位')
    @pytest.mark.parametrize('locate_type, jump_type, image_url, title', data['test_add_homepage'])
    def test_home_add(self, locate_type, jump_type, image_url, title):
        res = self.th.up_home().add_homepage(locate_type, jump_type, image_url, title)
        my_assert('assert args[1] in args[0]', res, '/en/admin/ttp/homepage/')
        if locate_type == 0 or locate_type == 1:
            res = banner_grid_api()
            my_assert('assert args[1] in args[0]', res, title)
        elif locate_type == 2:
            res = recommend_grid_api()
            my_assert('assert args[1] in args[0]', res, title)
        elif locate_type == 3:
            res = hottest_api()
            my_assert('assert args[1] in args[0]', res, title)

    @allure.story('搜索广告位')
    @pytest.mark.parametrize('locate_type, jump_type, shelve_type', data['test_home_search'])
    def test_home_search(self, locate_type, jump_type, shelve_type):
        res = self.th.up_home().search(locate_type, jump_type, shelve_type)
        if locate_type == 2:
            my_assert('assert args[0] == args[1]', res, '轮播图')
        elif locate_type == 3:
            my_assert('assert args[0] == args[1]', res, '瓦片区')
        elif locate_type == 4:
            my_assert('assert args[0] == args[1]', res, '推荐页瓦片区')
        elif locate_type == 5:
            my_assert('assert args[1] in args[0]', res, '当前最热')

    @allure.story('下架广告位')
    @pytest.mark.parametrize('locate_type', data['test_home_down_shelve'])
    def test_home_down_shelve(self, locate_type):
        exc = self.th.up_home().down_shelve(locate_type)
        if locate_type == 2 or locate_type == 3:
            res = banner_grid_api()
            my_assert('assert args[1] not in args[0]', res, exc)
        elif locate_type == 4:
            res = recommend_grid_api()
            my_assert('assert args[0] != args[1]', res, exc)
        elif locate_type == 5:
            res = hottest_api()
            my_assert('assert args[0] != args[1]', res, exc)

    @allure.story('更新广告位')
    @pytest.mark.parametrize('locate_type, title', data['test_home_update'])
    def test_home_update(self, locate_type, title):
        res = self.th.up_home().update_homepage(locate_type, title)
        my_assert('assert args[0] == args[1]', res, title)

    # def test_home_order(self):
    #     # todo: 完善拖动排序用例
    #     pass
