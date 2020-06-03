import unittest
from page.pageBaseInfoMange.page_units_manage import PageUnitsManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pum = PageUnitsManage(cls.driver)
        cls.pum.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查询、编辑
    def test_units_manage_edit(self):
        self.pum.units_manage_edit()

    # 测试查看
    def test_units_manage_watch(self):
        self.pum.units_manage_watch()

    # 测试重置
    def test_units_manage_reset(self):
        self.pum.units_manage_reset()


if __name__ == '__main__':
    unittest.main()
