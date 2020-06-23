import unittest
from page.page_system_manage.page_user_manage import TestPageUserManage
from parameterized import parameterized
# from tools.read_json import read_json
from tools.read_txt import read_txt
from base.get_driver import GetDriver
import pytest
import page
import allure
import time


class TestUserManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.um = TestPageUserManage(cls.driver)
        cls.um.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增

    @parameterized.expand(read_txt("system_manage/system_user.txt"))
    @allure.step(title="用户管理新增参数化(等价类边界值)")
    @pytest.mark.run(order=1)
    def test_user_manage_insert(self, username, password, sure_password, success):
        self.um.user_manage_insert(username, password, sure_password)
        if success:
            try:
                self.um.page_user_manage_insert_return_button()
            except:
                self.um.base_get_image()

    # 测试用户管理新增、查询、编辑
    @allure.step(title="用户管理的新增到编辑")
    @pytest.mark.run(order=2)
    def test_user_manage_edit(self):
        self.um.user_manage_edit(page.public_value, page.public_password, page.public_password)

    # 测试用户管理的重置
    @allure.step(title="用户管理重置")
    @pytest.mark.run(order=3)
    def test_user_manage_reset(self):
        self.um.user_manage_reset()

    # 测试用户管理的禁用
    @allure.step(title="用户管理禁用")
    @pytest.mark.run(order=4)
    def test_user_manage_ban(self):
        self.um.user_manage_ban(page.public_value2, page.public_password, page.public_password)


if __name__ == '__main__':
    pytest.main()
