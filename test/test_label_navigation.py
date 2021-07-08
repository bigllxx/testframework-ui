import allure
import pytest
from common.action import PgSql, yaml_load, my_assert
from page.index import Access
from common.all_api import recommend_navbar_api


@allure.feature('标签、导航栏相关')
class TestLabelNavigation:
    data = yaml_load('/data/test_label_navigation.yaml')

    def setup_class(self):
        try:
            PgSql().clear_label()
        except:
            print('清除数据失败')
        self.ts = Access().login()

    def teardown_class(self):
        self.ts.driver.quit()

    @allure.story('搜索标签')
    @pytest.mark.parametrize('label_name', data['test_search_label'])
    def test_search_label(self, label_name):
        res = self.ts.up_label().search_label(label_name)
        my_assert('assert args[1] in args[0]', res, label_name)

    @allure.story('新增标签')
    @pytest.mark.parametrize('label_name, back_image', data['test_add_label'])
    def test_add_label(self, label_name, back_image):
        res = self.ts.up_label().add_label(label_name, back_image)
        my_assert('assert args[0] == args[1]', res, label_name)

    @allure.story('修改标签')
    @pytest.mark.parametrize('label_name, back_image', data['test_update_label'])
    def test_update_label(self, label_name, back_image):
        res = self.ts.up_label().update_label(label_name, back_image)
        my_assert('assert args[0] == args[1]', res, label_name)

    @allure.story('新增标签组')
    @pytest.mark.parametrize('label_name, back_image', data['test_add_label_group'])
    def test_add_label_group(self, label_name, back_image):
        res = self.ts.up_label_group().add_label_group(label_name, back_image)
        my_assert('assert args[0] == args[1]', res, label_name)

    @allure.story('编辑标签组')
    def test_update_label_group(self):
        res = self.ts.up_label_group().update_label_group()
        my_assert('assert args[0] == args[1]', res, self.data['test_add_label_group'][0][0])

    @allure.story('新增推荐页导航栏')
    @pytest.mark.parametrize('navigation_name, navigation_description, navigation_type', data['test_add_navigation'])
    def test_add_navigation(self, navigation_name, navigation_description, navigation_type):
        res = self.ts.up_navigation().add_navigation(navigation_name, navigation_description, navigation_type)
        api_res = recommend_navbar_api()
        my_assert('assert args[0] == args[1] == args[2]', res, navigation_name, api_res)

    @allure.story('修改推荐页导航栏')
    @pytest.mark.parametrize('navigation_name, navigation_description, navigation_type', data['test_update_navigation'])
    def test_update_navigation(self, navigation_name, navigation_description, navigation_type):
        res = self.ts.up_navigation().update_navigation(navigation_name, navigation_description, navigation_type)
        api_res = recommend_navbar_api()
        my_assert('assert args[0] == args[1] == args[2]', res, navigation_name, api_res)

    @allure.story('下架推荐页导航栏')
    def test_down_navigation(self):
        res = self.ts.up_navigation().down_navigation()
        my_assert('assert args[0] == args[1]', res, False)
