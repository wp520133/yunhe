import unittest
from page.page_base_info_mange.page_units_class_manage import PageUnitsClassManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pucm = PageUnitsClassManage(cls.driver)
        cls.pucm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查询、编辑
    def test_units_class_manage_edit(self):
        self.pucm.units_class_manage_edit()

    # 测试重置
    def test_units_class_manage_reset(self):
        self.pucm.units_class_manage_reset()


if __name__ == '__main__':
    unittest.main()
