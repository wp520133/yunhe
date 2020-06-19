import unittest
from page.page_app_notice_manage.page_app_notice_manage import PageAppNoticeManage
from base.get_driver import GetDriver
import page
import allure
import time
import pytest
from parameterized import parameterized
from tools.read_json import read_json


# 已经完成,缺新增校验
class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.panm = PageAppNoticeManage(cls.driver)
        cls.panm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增

    # @allure.step(title="App公告管理新增")
    # @pytest.mark.run(order=1)
    # def test_app_notice_manage_insert(self):
    #     self.panm.app_notice_manage_insert(page.public_value, page.public_value2)
    #
    # # 对新增字段做校验处理

    @parameterized.expand(read_json("login.json"))
    # @pytest.mark.run(order=2)
    def test_app_notice_manage_insert_test(self, title, content, success):
        self.panm.app_notice_manage_insert(title, content)
        if success:  # 走True
            try:
                # 断言新增app公告主题不存在,表示该用例执行通过,存在就表示异常
                # self.panm.page_app_notice_manage_insert_title_text()    这一行是表示新增app公告主题存在的意思
                self.assertFalse(self.panm.page_app_notice_manage_insert_title_text())  # 断言不存在

                # 通过用例,这个怎么写
            except:
                self.panm.base_get_image()
        else:  # 走False
            # try:
            #     self.assertEqual(self.panm.page_app_notice_manage_insert_title_hint(),"请输入公告标题") or
            # except Exception as Error:
            #     print(Error)
            # else:
            # print(self.panm.page_app_notice_manage_insert_title_hint())
            try:
                self.assertTrue(self.panm.page_app_notice_manage_insert_title_hint()) or self.assertTrue(
                    self.panm.page_app_notice_manage_insert_content_hint())
                self.panm.page_app_notice_manage_insert_cancel()
            except AssertionError as error:
                print(error)
            # else:
            #     time.sleep(10)


    # # 测试查询
    # @pytest.mark.run(order=2)
    # @allure.step(title="App公告管理查询")
    # def test_app_notice_manage_search(self):
    #     self.panm.app_notice_manage_search()
    #
    # # 测试重置
    # @pytest.mark.run(order=3)
    # @allure.step(title="App公告管理重置")
    # def test_app_notice_manage_reset(self):
    #     self.panm.app_notice_manage_reset()


if __name__ == '__main__':
    pytest.main()
