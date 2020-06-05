import unittest
from page.page_system_manage.page_role_manage import PageRoleManage
# from parameterized import parameterized
from base.get_driver import GetDriver


class TestRoleManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pm = PageRoleManage(cls.driver)
        cls.pm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试角色管理新增
    def test_role_manage_insert(self):
        self.pm.role_manage_insert()

    # 测试角色管理查看
    def test_role_manage_watch(self):
        self.pm.role_manage_watch()

    # 测试角色权限
    def test_role_manage_power(self):
        self.pm.role_manage_power()

    # 测试角色编辑
    def test_role_manage_edit(self):
        self.pm.role_manage_edit()


if __name__ == '__main__':
    unittest.main()
