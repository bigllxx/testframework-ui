import allure
import pytest
from common.action import PgSql, yaml_load, my_assert
from page.index import Access


@allure.feature('话题、话题组相关')
class TestTopic:
    data = yaml_load('/data/test_topic_data.yaml')

    def setup_class(self):
        try:
            PgSql().clear_topic()
        except:
            print('清除数据失败')
        self.tt = Access().login()

    def teardown_class(self):
        self.tt.driver.quit()

    @allure.story('新增话题')
    @pytest.mark.parametrize('title, desc, max_hottest, image', data['test_add_topic'])
    def test_add_topic(self, title, desc, max_hottest, image):
        res = self.tt.up_topic().add_topic(title, desc, bool(max_hottest), image)
        my_assert('assert args[0] == args[1]', res, title)

    @allure.story('搜索话题')
    @pytest.mark.parametrize('title', data['test_search_topic'])
    def test_search_topic(self, title):
        res = self.tt.up_topic().search_topic(title)
        my_assert('assert args[0] == args[1]', res, title)

    @allure.story('更新话题')
    @pytest.mark.parametrize('title, desc, max_hottest, image', data['test_update_topic'])
    def test_update_topic(self, title, desc, max_hottest, image):
        res = self.tt.up_topic().update_topic(title, desc, bool(max_hottest), image)
        my_assert('assert args[0] == args[1]', res, title)

    @allure.story('新增话题组')
    @pytest.mark.parametrize('title, desc, image', data['test_add_topic_group'])
    def test_add_topic_group(self, title, desc, image):
        res = self.tt.up_topic_group().add_topic_group(title, desc, image)
        my_assert('assert args[0] == args[1]', res, title)

    @allure.story('更新话题组')
    @pytest.mark.parametrize('title, desc, image', data['test_update_topic_group'])
    def test_update_topic_group(self, title, desc, image):
        res = self.tt.up_topic_group().update_topic_group(title, desc, image)
        my_assert('assert args[0] == args[1]', res, title)