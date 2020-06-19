import unittest
from page.page_system_manage.page_dept_manage import PageDeptManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pd = PageDeptManage(cls.driver)
        cls.pd.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试部门管理新增
    def test_dept_manage_insert(self):
        self.pd.dept_manage_insert()

    # 测试部门管理编辑
    def test_dept_manage_edit(self):
        self.pd.dept_manage_edit()

    # 测试部门管理查看
    def test_dept_manage_watch(self):
        self.pd.dept_manage_watch()


if __name__ == '__main__':
    unittest.main()
