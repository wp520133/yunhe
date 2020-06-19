import unittest
from page.page_system_manage.page_user_manage import TestPageUserManage
from parameterized import parameterized
from tools.read_json import read_json
from tools.read_txt import read_txt
from base.get_driver import GetDriver
import pytest
import page


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
    @parameterized.expand(read_txt("system_user.txt"))
    def test_user_manage_insert(self, username, password, sure_password,success):
        self.um.user_manage_insert(username, password, sure_password)
        if success==True:
            try:
                # 判断是否新增
                self.assertTrue(self.um.page_user_manage_is_insert())
            except:
                self.um.base_get_image()
        else:
            try:
                self.um.page_user_manage_insert_return_button()
            except Exception as Error:
                print(Error)
    #
    # # 测试用户管理新增、查询、编辑
    # def test_user_manage_edit(self):
    #     self.um.user_manage_edit(page.public_value,page.public_password,page.public_password)
    #
    # # 测试用户管理的重置
    # def test_user_manage_reset(self):
    #     self.um.user_manage_reset()
    #
    # # 测试用户管理的禁用
    # def test_user_manage_ban(self):
    #     self.um.user_manage_ban(page.public_value,page.public_password,page.public_password)


if __name__ == '__main__':
    pytest.main()
