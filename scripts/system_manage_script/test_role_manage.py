import unittest
from page.page_system_manage.page_role_manage import PageRoleManage
from parameterized import parameterized
from base.get_driver import GetDriver
from tools.read_txt import read_txt
import page
import pytest
import allure


class TestRoleManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pm = PageRoleManage(cls.driver)
        cls.pm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试角色管理新增
    @allure.step(title="角色管理新增成功")
    @pytest.mark.run(order=1)
    def test_role_manage_insert(self):
        self.pm.role_manage_insert(page.public_value, page.public_value, page.public_value)

    # 测试角色管理异常新增
    @parameterized.expand(read_txt("system_manage/system_role.txt"))
    @allure.step(title="角色管理异常新增,预期失败")
    @pytest.mark.run(order=2)
    def test_role_manage_except_insert(self, rolename, rolecode, roledesc):
        self.pm.role_manage_insert(rolename, rolecode, roledesc)
        try:
            self.pm.page_role_manage_input_return()
        except:
            self.pm.base_get_image()

    # 测试角色管理查看
    @allure.step(title="角色管理查看")
    @pytest.mark.run(order=3)
    def test_role_manage_watch(self):
        self.pm.role_manage_watch()

    # 测试角色权限
    @allure.step(title="角色管理权限")
    @pytest.mark.run(order=4)
    def test_role_manage_power(self):
        self.pm.role_manage_power()

    # 测试角色编辑
    @allure.step(title="角色管理编辑")
    @pytest.mark.run(order=5)
    def test_role_manage_edit(self):
        self.pm.role_manage_edit()


if __name__ == '__main__':
    unittest.main()
