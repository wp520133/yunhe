import unittest
from page.page_base_info_mange.page_units_type_manage import PageUnitsTypeManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.putm = PageUnitsTypeManage(cls.driver)
        cls.putm.system_login("dym6", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查询、编辑
    def test_units_type_manage_edit(self):
        self.putm.units_type_manage_edit()

    # 测试查看
    def test_units_type_manage_watch(self):
        self.putm.units_type_manage_watch()

    # 测试重置
    def test_units_type_manage_reset(self):
        self.putm.units_type_manage_reset()


if __name__ == '__main__':
    unittest.main()
