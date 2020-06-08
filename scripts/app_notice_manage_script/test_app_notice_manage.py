import unittest
from page.page_app_notice_manage.page_app_notice_manage import PageAppNoticeManage
from base.get_driver import GetDriver
import page
import allure
import pytest
from parameterized import parameterized
from tools.read_txt import read_txt
# 已经完成,缺新增校验
class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.panm = PageAppNoticeManage(cls.driver)
        cls.panm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # # 测试新增
    # @pytest.mark.run(order=1)
    # @allure.step(title="App公告管理新增")
    # def test_app_notice_manage_insert(self):
    #     self.panm.app_notice_manage_insert(page.public_value, page.public_value2)

    # 对新增字段做校验处理
    @parameterized.expand([(page.public_value_51,page.public_value_256),("","")])
    def test_app_notice_manage_insert_test(self,title, content):
        self.panm.app_notice_manage_insert(title, content)
        print(self.panm.page_app_notice_manage_insert_content_hint)
        title=self.panm.page_app_notice_manage_insert_title_hint()
        content=self.panm.page_app_notice_manage_insert_content_hint()
        type=self.panm.page_app_notice_manage_insert_type_hint()
        if title=="不能大于50个字符" and content=="不能大于255个字符":
            self.panm.base_back()
        elif title=="请输入公告标题" and content=="请输入公告内容" and type=="请输入公告类型":
            self.panm.base_back()
        else:
            pass
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
