import unittest
from page.pageBaseInfoMange.page_repair_class_manage import PageRepairClassManage
from base.get_driver import GetDriver


class TestSystemClassManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.prcm = PageRepairClassManage(cls.driver)
        cls.prcm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查询、修改
    def test_repair_class_manage_edit(self):
        self.prcm.repair_class_manage_edit()

    # 测试重置
    def test_repair_class_manage_reset(self):
        self.prcm.repair_class_manage_reset()


if __name__ == '__main__':
    unittest.main()
