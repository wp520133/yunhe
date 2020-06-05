import unittest
from page.page_system_manage.page_user_manage import TestPageUserManage
# from parameterized import parameterized
from base.get_driver import GetDriver
import pytest


class TestUserManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.um = TestPageUserManage(cls.driver)
        cls.um.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试用户管理新增、查询、编辑
    def test_user_manage_edit(self):
        self.um.user_manage_edit()

    # 测试用户管理的重置
    def test_user_manage_reset(self):
        self.um.user_manage_reset()

    # 测试用户管理的禁用
    def test_user_manage_ban(self):
        self.um.user_manage_ban()


if __name__ == '__main__':
    pytest.main()
