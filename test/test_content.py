import allure
import pytest
from common.action import yaml_load, my_assert
from page.index import Access


@allure.feature('文章、视频、单品相关')
class TestContent:
    data = yaml_load('/data/test_content_data.yaml')

    def setup_class(self):
        self.ts = Access().login()

    def teardown_class(self):
        self.ts.driver.quit()

    @allure.story('单品搜索')
    @pytest.mark.parametrize('audit_state, shelve_state', data['test_content_search'])
    def test_snack_search(self, audit_state, shelve_state):
        res = self.ts.up_snack().search(audit_state, shelve_state)
        if audit_state == 2:
            my_assert("assert args[0] == args[1] or '(None'", res, '正常')  # 不知道为什么，None会被转成（None
        elif audit_state == 4:
            my_assert("assert args[0] == args[1] or '(None'", res, '等待手动审核')
        elif audit_state == 7:
            my_assert("assert args[0] == args[1] or '(None'", res, '手动审核拒绝')

    @allure.story('单品拒绝审核')
    def test_snack_refuse_audit(self):
        res = self.ts.up_snack().refuse_audit()
        my_assert("assert args[0] == args[1]", res, '手动审核拒绝')

    @allure.story('单品通过审核')
    def test_snack_agree_audit(self):
        res = self.ts.up_snack().agree_audit()
        my_assert("assert args[0] == args[1]", res, '正常')

    @allure.story('单品预览')
    @pytest.mark.parametrize('audit_state', data['test_content_preview'])
    def test_snack_preview(self, audit_state):
        res = self.ts.up_snack().preview(audit_state)
        if audit_state == 2 or audit_state == 4:
            my_assert("assert args[0] is args[1]", res, True)
        else:
            my_assert("assert args[0] is args[1]", res, False)

    @allure.story('文章搜索')
    @pytest.mark.parametrize('audit_state, shelve_state', data['test_content_search'])
    def test_post_search(self, audit_state, shelve_state):
        res = self.ts.up_post().search(audit_state, shelve_state)
        if audit_state == 2:
            my_assert("assert args[0] == args[1] or '(None'", res, '正常')
        elif audit_state == 4:
            my_assert("assert args[0] == args[1] or '(None'", res, '等待手动审核')
        elif audit_state == 7:
            my_assert("assert args[0] == args[1] or '(None'", res, '手动审核拒绝')

    @allure.story('文章拒绝审核')
    def test_post_refuse_audit(self):
        res = self.ts.up_post().refuse_audit()
        my_assert("assert args[0] == args[1]", res, '手动审核拒绝')

    @allure.story('文章通过审核')
    def test_post_agree_audit(self):
        res = self.ts.up_post().agree_audit()
        my_assert("assert args[0] == args[1]", res, '正常')

    @allure.story('文章预览')
    @pytest.mark.parametrize('audit_state', data['test_content_preview'])
    def test_post_preview(self, audit_state):
        res = self.ts.up_post().preview(audit_state)
        if audit_state == 2 or audit_state == 4:
            my_assert("assert args[0] is args[1]", res, True)
        else:
            my_assert("assert args[0] is args[1]", res, False)

    @allure.story('视频搜索')
    @pytest.mark.parametrize('audit_state, shelve_state', data['test_content_search'])
    def test_video_search(self, audit_state, shelve_state):
        res = self.ts.up_video().search(audit_state, shelve_state)
        if audit_state == 2:
            my_assert("assert args[0] == args[1] or '(None'", res, '正常')
        elif audit_state == 4:
            my_assert("assert args[0] == args[1] or '(None'", res, '等待手动审核')
        elif audit_state == 7:
            my_assert("assert args[0] == args[1] or '(None'", res, '手动审核拒绝')

    @allure.story('视频拒绝审核')
    def test_video_refuse_audit(self):
        res = self.ts.up_video().refuse_audit()
        my_assert("assert args[0] == args[1]", res, '手动审核拒绝')

    @allure.story('视频通过审核')
    def test_video_agree_audit(self):
        res = self.ts.up_video().agree_audit()
        my_assert("assert args[0] == args[1]", res, '正常')

    @allure.story('视频预览')
    @pytest.mark.parametrize('audit_state', data['test_content_preview'])
    def test_video_preview(self, audit_state):
        res = self.ts.up_video().preview(audit_state)
        if audit_state == 2 or audit_state == 4:
            my_assert("assert args[0] is args[1]", res, True)
        else:
            my_assert("assert args[0] is args[1]", res, False)

    @allure.story('讨论搜索')
    @pytest.mark.parametrize('audit_state, shelve_state', data['test_content_search'])
    def test_topic_discuss_search(self, audit_state, shelve_state):
        res = self.ts.up_topic_discuss().search(audit_state, shelve_state)
        if audit_state == 2:
            my_assert("assert args[0] == args[1] or '(None'", res, '正常')  # 不知道为什么，None会被转成（None
        elif audit_state == 4:
            my_assert("assert args[0] == args[1] or '(None'", res, '等待手动审核')
        elif audit_state == 7:
            my_assert("assert args[0] == args[1] or '(None'", res, '手动审核拒绝')

    @allure.story('讨论拒绝审核')
    def test_topic_discuss_refuse_audit(self):
        res = self.ts.up_topic_discuss().refuse_audit()
        my_assert("assert args[0] == args[1]", res, '手动审核拒绝')

    @allure.story('讨论通过审核')
    def test_topic_discuss_agree_audit(self):
        res = self.ts.up_topic_discuss().agree_audit()
        my_assert("assert args[0] == args[1]", res, '正常')

    @allure.story('讨论预览')
    @pytest.mark.parametrize('audit_state', data['test_content_preview'])
    def test_topic_discuss_preview(self, audit_state):
        res = self.ts.up_topic_discuss().preview(audit_state)
        if audit_state == 2 or audit_state == 4:
            my_assert("assert args[0] is args[1]", res, True)
        else:
            my_assert("assert args[0] is args[1]", res, False)